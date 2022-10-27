# Program to implement a book class and bookstore
class BookStore:

    def __init__(self, books):
        self.books = books

    def getbooks(self):
        return self.books


class Book:

    def __init__(self, name, isbn, author):
        self.name = name
        self.isbn = isbn
        self.author = author


bookList = [Book("Book1", "122323-ww-ww", "David"),
            Book("Book2", "323332-rr-ee-ee32", "Ben"),
            Book("Book3", "223-ew-ee-e", "Paul"),
            Book("Book4", "yy-21-12y", "Adam")]
bookstore = BookStore(bookList)
for item in bookstore.getbooks():
    print("==========")
    print(item.name)
    print(item.isbn)
    print(item.author)
    print("==========")




