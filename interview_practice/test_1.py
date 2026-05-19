class Book:
    def __init__(self, title):
        self.title = title
        self.checked_out = False


class User:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, user, title):

        for book in self.books:
            if book.title == title and not book.checked_out:
                book.checked_out = True
                user.books.append(book)
                return True

        return False

    def return_book(self, user, title):

        for book in user.books:
            if book.title == title:
                book.checked_out = False

        return True
    
    def available_books(self):
        available = []

        for book in self.books:
            if book.checked_out is False:
                available.append(book)

        return available

