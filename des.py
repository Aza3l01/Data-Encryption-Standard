from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def encrypt_msg(plain_text,key):
  cipher = DES.new(key,DES.MODE_ECB)
  # Padding to ensure plain text is a multiple of block size.
  pad_msg = pad(plain_text.encode(),DES.block_size)
  cipher_text = cipher.encrypt(pad_msg)
  return cipher_text

def decrypt_msg(cipher_text,key):
  cipher = DES.new(key,DES.MODE_ECB)
  decrypted_msg = unpad(cipher.decrypt(cipher_text),DES.block_size)
  return decrypted_msg.decode()

plain_text = input("Enter the Message:")
print(plain_text)
key = get_random_bytes(8)
cipher_text = encrypt_msg(plain_text,key)
print("Encrypted Message:",cipher_text)

decrypted_msg = decrypt_msg(cipher_text,key)
print("Decrypted Message:",decrypted_msg)