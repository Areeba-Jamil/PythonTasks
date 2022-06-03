import re


#Text Written in File is as Follows:
#'Try to find any string in this file.
#This file also contains integers as 123456789.
#Hello from the other side.'


#Read the file and print the data in file
FileOpen = open('StringinFile.txt', mode ='r')
StringinFile = FileOpen.read()

#Method 1: By giving the string to search in file
search = 'file'
re.search(search,'text')
if search in StringinFile:
	print('The string you searched in file is found')
	print(search +'\n')
else:
	print('string not found')


#Method 2: By asking user to enter a string and then search in the file
search = input('Enter the string you want to search in the file:')
re.search(search,'text')
if search in StringinFile:
	print(f'The string you searched in file is found: {search}')
else:
	print('string not found')