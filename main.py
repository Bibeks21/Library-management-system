class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. please return it within 30 days OR reissue the book ")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,This book either already been issued to someone else or not available in library. please wait until the book returned")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book! Hope you enjoyed reading it!")

class Student:
    def requestBook(self):
        self.book= input("Enter the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__  == "__main__":
    centralLibrary = Library(["algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
 
    while(True):
        welcomeMsg = '''  =====Welcome to central Library=====  
        please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit The Library'''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library.")
            exit()
        else:
            print("Invalid Choice!")
        