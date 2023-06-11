class Visitor:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = None

    def borrow_book(self, book_title):
        new_book = Book(book_title)
        if self.borrowed_books is None:
            self.borrowed_books = new_book
        else:
            current_book = self.borrowed_books
            while current_book.next_book is not None:
                current_book = current_book.next_book
            current_book.next_book = new_book

    def print_borrowed_books(self):
        if self.borrowed_books is None:
            print("Pengunjung", self.name, "tidak memiliki buku yang dipinjam.")
        else:
            print("Daftar buku yang dipinjam oleh pengunjung", self.name + ":")
            current_book = self.borrowed_books
            while current_book is not None:
                print(current_book.title)
                current_book = current_book.next_book


class Book:
    def __init__(self, title):
        self.title = title
        self.next_book = None


class Library:
    def __init__(self):
        self.visitors = []

    def add_visitor(self, name):
        new_visitor = Visitor(name)
        self.visitors.append(new_visitor)

    def find_visitor(self, name):
        for visitor in self.visitors:
            if visitor.name == name:
                return visitor
        return None


# Contoh penggunaan

library = Library()

# Menambahkan pengunjung
library.add_visitor("wawa")
library.add_visitor("ujang")
library.add_visitor("Mamat")

# Menyimpan catatan peminjaman buku
wawa = library.find_visitor("wawa")
wawa.borrow_book("mencintai dia")
wawa.borrow_book("kapan kamu suka sama aku?")

ujang = library.find_visitor("ujang")
ujang.borrow_book("jatuh cinta sendiri")

# Mencetak daftar buku yang dipinjam oleh pengunjung
wawa.print_borrowed_books()
ujang.print_borrowed_books()
