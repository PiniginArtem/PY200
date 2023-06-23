class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print(f"Книга {self.title} уже взята на руки.")
        else:
            self.is_checked_out = True
            print(f"Книга {self.title} была взята на руки.")

    def check_in(self):
        if not self.is_checked_out:
            print(f"Книга {self.title} уже возвращена.")
        else:
            self.is_checked_out = False
            print(f"Книга {self.title} была возвращена.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book.check_out()
        print(f"Книга с ISBN {ISBN} не найдена.")

    def check_in_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book.check_in()
        print(f"Книга с ISBN {ISBN} не найдена.")


if __name__ == "__main__":
    new_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
    library = Library()
    library.add_book(new_book)
    library.check_out_book("123456789")
    library.check_in_book("123456789")
