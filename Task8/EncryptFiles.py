#Encrypt Files and Folders

#import required libraries or modules
from cryptography.fernet import Fernet

#generate a key using Fernet
key = Fernet.generate_key()

#include the key in a file
with open('Filekey.key','wb') as file_key:
	file_key.write(key)

#Now Encrypt a File using the file_key
F = Fernet(key)

#encoding string into byte string
with open('CSVtoExcel.csv','rb') as file:
	Original_file = file.read()

E_File = F.encrypt(Original_file)

#open
with open('CSVtoExcel.csv', 'wb') as encrypted_file:
    encrypted_file.write(E_File)
