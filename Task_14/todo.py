#CLI based todo Application


#Create a symbolic link to the executable file:
#In Windows CMD, Run as administrator and give the following command:
#mklink todo todo.bat

#import required modules
import sys
import datetime

#This method uses nec() as a main controller to read and store todo.txt (items on todo list) and done.txt (items completed) in arrays that can be later manipulated
  
#Function to help users understand the options
def help():
    menu = """Usage :-
$ ./todo add "todo item"  | Add a new todo
$ ./todo ls               | Show remaining todos
$ ./todo del NUMBER       | Delete a todo
$ ./todo done NUMBER      | Complete a todo
$ ./todo help             | Show usage
$ ./todo report           | Statistics"""
    sys.stdout.buffer.write(menu.encode('utf8'))
  
#Function to add a task on the list
def add(s):
    f = open('todo.txt', 'a') #Opens todo file
    f.write(s) #Writes item to list
    f.write("\n") #Adds space between items for readability
    f.close()
    print(f"Added todo: {s} ")
  
#Function to print the the complete todo list
def ls():
    try:
  
        nec() #Opens and retrieves array from main controller
        l = len(d)
        k = l
  
        for i in d: #Prints all items based items added to  array in nec()
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l-1
  
    except Exception as e:
        raise e
  
#Function to delete a task from the list  
def deL(no):
    try:
        no = int(no) #Casting user input to int
        nec() #Opens main controller
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i) #Method traverses through file and deletes if found
            f.truncate()
        print(f"Deleted todo #{no}")
  
    except Exception as e:
        print(f"Error: todo #{no} does not exist. Nothing deleted.")
  
#Marks an entered item as completed  
def done(no): #NO is item ID
    try:
  
        nec() #Opens main controller
        no = int(no)
        f = open('done.txt', 'a') #Opens done.txt and adds item/date/time
        st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[no]
        f.write(st) 
        f.write("\n") #Space for readability
        f.close()
        print(f"Marked todo #{no} as done.")
        
        #Checks and writes back to todo.txt if item is not done
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0) 
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i) 
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")
  
#The main function - controls the main todo.txt file  
def nec():
    try:
        f = open('todo.txt', 'r') 
        c = 1 #c is based on number of lines in the code
        for line in f:
            line = line.strip('\n') #Seperating spaces in each line
            d.update({c: line}) #Updates lines based on C-Counter
            c = c+1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))
        #Exception thrown in case of no items

#Traverses through array lists for terminal input
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
        if(args[1] == 'del'):
            args[1] = 'deL' #covering for user input mistakes
        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write( #exception handling incase user does not enter input
                "Error: Missing todo string. Nothing added!".encode('utf8'))
  
        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking todo as done.".encode('utf8'))
  
        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting todo.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
  
    except Exception as e:
  
        s = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
        sys.stdout.buffer.write(s.encode('utf8'))
