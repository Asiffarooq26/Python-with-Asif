# pip install cryptography 3.4.8
from cryptography.fernet import Fernet
key=Fernet.generate_key()
# print("Key=",key)
# cipher = Fernet(key)
# print(cipher)
# # message = b"hello world"
# message = "hello world"
# # print(type(message))
# # encrypted = cipher.encrypt(message)
# encrypted=cipher.encrypt(message.encode())
# print("Encrypted:", encrypted)
# decrypted=cipher.decrypt(encrypted)
# # print("Decrypted Message=",decrypted)
# print("Decrypted Message=",decrypted.decode())

# with open("secret.key", "wb") as f:
#     f.write(key)
# with open("secret.key", "rb") as f:
#     key = f.read()
# cipher = Fernet(key)
# print(cipher)

#Pip install rsa
#Asymmetric Encryption
# import rsa
# public_key,private_key=rsa.newkeys(512)
# print("Private Key",private_key)
# print("Public Key",public_key)
# message="Hello world"
# encrypted=rsa.encrypt(message.encode(),public_key)
# decrypted=rsa.decrypt(encrypted,private_key).decode()
# print("Encrypted Message=",encrypted)
# print("Decrypted Message=",decrypted)

#Hashing 
# import hashlib
# password = "mypassword"
# hashed=hashlib.sha256(password.encode()).hexdigest()
# # print("Hashed=",hashed)
# user_password=input("Enter your password")
# user_hashed=hashlib.sha256(user_password.encode()).hexdigest()
# if user_hashed==hashed:
#     print("Access Granted")
# else:
#     print("Acess Denied")

#Salting
import os, hashlib
# password = "mypassword"
# salt = os.urandom(16)
# print(salt)
# salted = salt + password.encode()
# hashed = hashlib.sha256(salted).hexdigest()
# # print("Salt:", salt)
# # print("Salted Hash:", hashed)
# user_password=input("Enter your password")
# user_hashed=hashlib.sha256(user_password.encode()).hexdigest()
# if user_hashed==hashed:
#     print("Access Granted")
# else:
#     print("Acess Denied")

with open("sample.txt", "rb") as f:
    data = f.read()
print(hashlib.sha256(data).hexdigest()) 