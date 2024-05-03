"""
Write a Python class representing a library, allowing users to add books, remove books, and display the available books (txt faylga yozsin va o’qisin). - A
"""

class Library:
    def __init__(self, filename="library.txt"):
        self.books = []
        self.filename = filename
        self.load_books()
    def add_book(self, title, author):

        book = {"title": title, "author": author}
        self.books.append(book)
        self.save_books()

    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"] != title]
        self.save_books()

    def display_books(self):
        if not self.books:
            print("Kutubxonada kitoblar topilmadi ")
        else:
            print("Kutubxonadagi kitoblar:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book['title']} - {book['author']}")

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for book in self.books:
                file.write(f"{book['title']}|{book['author']}\n")

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    title, author = line.strip().split("|")
                    self.books.append({"title": title, "author": author})
        except FileNotFoundError:
            pass


library = Library()

library.add_book("Dunyo", "Abdulla Qodiriy")
library.add_book("Alpomish", "Shoir")
library.add_book("O'tgan kunlar", "Abdulla Qodiriy")

library.display_books()

library.remove_book("Alpomish")

library.display_books()
