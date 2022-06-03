#pip install cryptography

#import required modules
from cryptography.fernet import Fernet

#Enter a string to be encrypted
s = "This string must be encrypted"

#Now use Fernet to generate a key
key = Fernet.generate_key()

F = Fernet(key)

#encoding string into byte string
E_string = F.encrypt(s.encode())

print("Original String: ", s)
print("Encrypted String: ", E_string)

#Now decrypt the string
D_string = F.decrypt(E_string).decode()
 
print("Decrypted String: ", D_string)