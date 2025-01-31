class Book:
    def __init__(self,title,author,isbn,copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies
    def add_book(self,book):
        library.append(book)

    def remove_book(self,removebook):
        for book in library:
            if book.isbn==removebook:
                library.remove(book)
        else:
            print(f'No such book with {removebook} isbn is found to remove')

    def find_book(self,isbn1):
        for i in library:
            if i.isbn==isbn1:
                print(f"{i.title} is found")
        else:
            print(f"Book with {isbn1} isbn is not found")
        
    def display_books(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\ncopies: {self.copies}\n')        

library=[]
n=int(input("Enter number of books to enter"))
for i in range(n):
    title=input("Enter book title: ")
    author=input("Enter book author: ")
    isbn=input("Enter book isbn: ")
    copies=int(input("Enter number of copies: "))
    book=Book(title,author,isbn,copies)
    book.add_book(book)
isbn1=input("Enter isbn of a book to return from library: ")
book.find_book(isbn1)
removebook=input("Enter isbn of book to remove from library: ")
book.remove_book(removebook)
print("\nLibrary books after updating\n")
for i in library:
    i.display_books()