#Random Password Generator
from random import shuffle
import string
import random

#a password can have letters,digits and special characters
letters = string.ascii_letters
digits = string.digits
S_characters = string.punctuation


#store the characters in a list to generate password from
password = list(letters + digits + S_characters)

#Function to generate random passwords
def generate_random_password():
	#Enter length of password
	length = int(input("Enter length of password: "))

	#shuffle the characters
	random.shuffle(password)
	
	## picking random characters from the list
	password_list = []
	for i in range(length):
		#append the characters in password list
		password_list.append(random.choice(password))

	random.shuffle(password_list)

	#converting the list to string
	print("".join(password_list))



#Function Call
if __name__ == '__main__':
	generate_random_password()
