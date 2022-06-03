#pip install cryptography

#import required modules
from cryptography.fernet import Fernet

#generate a key file
key = Fernet.generate_key()
with open('filekey.key', 'wb') as f:
    f.write(key)

with open('filekey.key', 'rb') as f:
    key = f.read()

fernet = Fernet(key)

#open a csv file and encrypt it using the key file
with open('CSVtoExcel.csv', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

#File Encrypted
with open('CSVtoExcel.csv', 'wb') as E_file:
    E_file.write(encrypted)