# Implement a library management system for a university library. The system should support the 
# following functionalities:

# Create an abstract class called LibraryItem using the ABC moduLLE.
# Define abstract methods in the LibraryItem class:
# get_title(): Returns the title of the item.
# get_author(): Returns the author of the item.
# is_available(): Returns True if the item is available for borrowing, False otherwise.
# check_out(): Marks the item as checked out.
# return_item(): Marks the item as returned.
from abc import ABC,abstractmethod
class libraryitem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
    @abstractmethod
    def get_title(self):
        pass
    @abstractmethod
    def get_author(self):
        pass
    @abstractmethod
    def is_available(self):
        pass
    @abstractmethod
    def chech_out(self):
        pass
    @abstractmethod
    def return_item(self):
        pass
# Create a concrete class called Book that inherits from LibraryItem.
# Implement the abstract methods in the Book class according to the requirements.
class Book(libraryitem):
    def __init__(self,title,author):
        super().__init__(title,author)
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def is_available(self):
        return not self.checked_out
    def chech_out(self):
        if self.is_available():
           self.checked_out=True
           print(f"Book '{self.title}'by {self.author}has been checked.")
        else:
            print(f"Book '{self.title}'by {self.author} is not available.")
    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"Book '{self.title}' by {self.author} was not checked out.")

# Create a class called Library to manage the library system.
# It should have a list to store the books in the library.
# Implement the following methods:
# add_book(book): Adds a new book to the library.
# remove_book(book): Removes a book from the library.
# search_books_by_title(title): Searches for books by title and returns a list of matching books.
# search_books_by_author(author): Searches for books by author and returns a list of matching books.
# display_book_availability(book): Displays the availability of a book.
# check_out_book(book): Checks out a book for borrowing.
# return_book(book): Returns a borrowed book.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Book '{book.get_title()}' by {book.get_author()} added to the library.")
        else:
            print("Invalid item. Only books can be added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.get_title()}' by {book.get_author()} removed from the library.")
        else:
            print("Book not found in the library.")

    def search_books_by_title(self, title):
        matching_books = [book for book in self.books if book.get_title().lower() == title.lower()]
        return matching_books

    def search_books_by_author(self, author):
        matching_books = [book for book in self.books if book.get_author().lower() == author.lower()]
        return matching_books

    def display_book_availability(self, book):
        if book.is_available():
            print(f"Book '{book.get_title()}' by {book.get_author()} is available.")
        else:
            print(f"Book '{book.get_title()}' by {book.get_author()} is not available.")

    def check_out_book(self, book):
        book.check_out()

    def return_book(self, book):
        book.return_item()


# Testing the library management system
# Adding a new book to the library.
# Removing a book from the library.
# Searching for books by title or author.
# Displaying the availability of a book.
# Checking out a book for borrowing.
# Returning a borrowed book.
if __name__ == "__main__":
    # Create some books
    book1 = Book("The Hobbit", "J.R.R. Tolkien")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Pride and Prejudice", "Jane Austen")

    # Create the library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Check book availability
    library.display_book_availability(book1)
    library.display_book_availability(book2)
    library.display_book_availability(book3)

    # Check out books
    library.check_out_book(book1)
    library.check_out_book(book2)

    # Try to check out an already checked-out book
    library.check_out_book(book1)

    # Return books
    library.return_book(book1)
    library.return_book(book3)

    # Remove a book from the library
    library.remove_book(book2)    
