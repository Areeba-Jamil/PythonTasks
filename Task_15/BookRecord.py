#Book Record for Library

#(name of book, author, ISBN number, add new book to record, update record, delete record)

#import required modules

#make a class named BOOK
class Book:

	def __init__(self,title,author,ISBN,ID):
		self.title = title
		self.author = author
		self.ISBN = ISBN
		self.ID = ID

	#print the book details
	def __str__(self):
		return f"\t {self.title}\t{self.author}\t{self.ISBN}\t{self.ID}\t\n"

	#function to update title only 
	def Updatetitle(self,utitle):
		self.title = utitle

	#function to update author name only
	def Updateauthor(self,uauthor):
		self.author = uauthor

	#function to update ISBN only
	def UpdateISBN(self,uisbn):
		self.ISBN = uisbn

	#function to update all info 
	def UpdateInfo(self,utitle,uauthor,uisbn):
		self.title = utitle
		self.author = uauthor
		self.ISBN = uisbn

class LibraryRecord:

	def __init__(self,blist):
		self.blist = blist

	#ADD
	#add new book to the list 
	def addnew(self,title,author,ISBN):

		if not self.blist:  # ID is defined as position of book in list
			ID = 0
		else:  # and if not, it sets itself to the end of the list
			ID = len(self.blist)

		newbook = Book(title,author,ISBN,ID)
		self.blist.append(newbook)

	#print the book list
	def showlist(self):
		for b in self.blist:
			print(b)

	#print a specific book by using ID
	def showlistbyID(self,ID):
		print(self.blist[ID])

	#DELETE
	#delete a book record
	def delbook(self,ID):
		self.blist.pop(ID)

	#To update all details of a particular book using ID
	def Updatebinfo(self,ID,utitle,uauthor,uISBN):
		self.blist[ID].UpdateInfo(utitle,uauthor,uISBN)

	# To update author of a particular book
	def UpdateBAuthor(self,ID,uauthor):
		self.blist[ID].Updateauthor(uauthor)
	
	# To update title of a particular book
	def UpdateBTitle(self,ID,utitle):
		self.blist[ID].Updatetitle(utitle)

	# To update ISBN of a particular book
	def UpdateBISBN(self,ID,uISBN):
		self.blist[ID].UpdateISBN(uISBN)


#Now the main function 
def mainFunc():
	bookList = []

	lib = LibraryRecord(bookList)

	# Loop until user wants to exit
	while (True):
		#ask user to enter choice
		c = int(input("Choose from the following optins:\n1. Add a book\n2. View Library\n3. View a Book\n4. Remove a Book\n5. Update a Book\n6. Exit\nEnter option:"))

		if (c == 1):
			title = input("Enter a title: ")
			author = input("Enter an author: ")
			ISBN = input("Enter an ISBN: ")
			lib.addnew(title, author, ISBN)
			print("Book added")
		elif (c == 2):
			lib.showlist()
		elif (c == 3):
			ID = int(input("Enter ID of book: "))
			lib.showlistbyID(ID)
		elif (c == 4):
			ID = int(input("Enter ID of book: "))
			lib.delbook(ID)
			print("Book removed")
		elif (c == 5):
			ID = int(input("Enter ID of book you want to update: "))

			#ask user to enter choice if they want to update any info
			uc = int(input("Do you want to:\n1. Update Title\n2.Update Author\n3. Update ISBN\n4. Update all details\nEnter option:"))

			if (uc == 1):
				updateTitle = input("Enter new title: ")
				lib.UpdateBTitle(ID, updateTitle)
				print("Title updated")
			elif (uc == 2):
				updateAuthor = input("Enter new author: ")
				lib.UpdateBAuthor(ID, updateAuthor)
				print("Author updated")
			elif (uc == 3):
				updateISBN = input("Enter new ISBN: ")
				lib.UpdateBISBN(ID, updateISBN)
				print("ISBN updated")
			elif (uc == 4):
				updateTitle = input("Enter new title: ")
				updateAuthor = input("Enter new author: ")
				updateISBN = input("Enter new ISBN: ")
				lib.Updatebinfo(ID, updateTitle, updateAuthor, updateISBN)
				print("All book details updated")
		
		elif (c == 6):
			break
		
		else:
			print("Invalid Option.")
	
if __name__ == '__main__':
	
	mainFunc()




