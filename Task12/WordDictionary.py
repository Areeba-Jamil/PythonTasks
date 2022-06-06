#Create dictionary to explain the meaning of given words

#import required modules
from tkinter import *
from PyDictionary import PyDictionary

# Create instances and objests
dictionary = PyDictionary()
win =Tk()

#Define the size of the window
win.geometry("650x300")

win.title("Python Word Dictionary")

#Define Helper Function to use the other atributes of PyDictionary Class
def dict():
   meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

#Define Labels and Buttons
Label(win, text="Word Dictionary", font=("Times New Roman" ,24)).pack(pady=20)

# Frame 1
frame = Frame(win)
Label(frame, text="Enter a Word ", font=("Times New Roman", 14)).pack(side=LEFT)
word = Entry(frame, font=("Times New Roman", 12))
word.pack()
frame.pack(pady=10)

# Frame 2
frame1 = Frame(win)
Label(frame1, text="Meaning:", font=("Times New Roman", 14)).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Times New Roman",12,"italic"), width= 50)
meaning.pack()
frame1.pack(pady=10)

Button(win, text="Search Meaning", font=("Times New Roman",15), command=dict).pack()

# Execute Tkinter
win.mainloop()