class Author:
    def __init__(self, name:str, nationality:str):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Author(name={self.name!r}, nationality={self.nationality!r})"

class Book:
    
    def __init__(self, title:str, genre:str, author: Author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.author} - {self.title}"
    
    def __repr__(self):
        return f"Book(title={self.title!r}, genre={self.genre!r}, author={self.author!r})"

class Library:
    def __init__(self, name:str):
        self.name = name
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        print(f"Aviable books in {self.name}")
        for book in self.books:
            print(book)

    def remove_book(self, title:str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        print(f"No book found with this title: {title}")

author1 = Author("X", "hungarian")
author2 = Author("Y", "bulgarian")

book1 = Book("How to get away with murder", "crime", author1)
book2 = Book("Test X", "crime", author2)

lib = Library("Szabo Ervin Városi Könyvtár")
print(lib.books)
lib.add_book(book1)
print(lib.books)
lib.add_book(book2)
lib.remove_book("Test X")
lib.list_books()
