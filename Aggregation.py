class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

book1 = Book("Python Programming")
book2 = Book("Data Structures")

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)

for book in my_library.books:
    print(book.title)