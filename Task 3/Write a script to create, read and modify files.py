#Files
#Create a file and add some text to it
FileTask = open('FileTask.txt',mode ='w')
FileTask.write('This is the file for Task 3, which is to create, read and modify files')
FileTask.close()

#Read the file and print the data in file
with open('FileTask.txt', mode ='r') as f:
    print(f.read())
    
#Modify the file by adding some more text to it
with open('FileTask.txt', mode ='a') as f:
    f.write('The file is modified by adding this line to it.')
