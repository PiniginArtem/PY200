from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    # Абстрактные методы, которые должны быть реализованы в дочерних классах
    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def check_in(self):
        pass


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def check_out_book(self, ISBN: str):
        for book in self.books:
            if book.ISBN == ISBN:
                return book.check_out()
        print(f"Книга с ISBN {ISBN} не найдена.")

    def check_in_book(self, ISBN: str):
        for book in self.books:
            if book.ISBN == ISBN:
                return book.check_in()
        print(f"Книга с ISBN {ISBN} не найдена.")


class PhysicalBook(Book):
    def __init__(self, title: str, author: str, ISBN: str, is_checked_out=False):
        super().__init__(title, author, ISBN)
        self.is_checked_out = is_checked_out

    def check_out(self):
        if self.is_checked_out:
            print(f"Книга {self.title} уже взята на руки.")
        else:
            self.is_checked_out = True
            print(f"Книга {self.title} была взята на руки.")

    def check_in(self):
        if not self.is_checked_out:
            print(f"Книга {self.title} уже в библиотеке.")
        else:
            self.is_checked_out = False
            print(f"Книга {self.title} была возвращена.")


class Ebook(Book):
    def __init__(self, title: str, author: str, ISBN: str, link: str):
        super().__init__(title, author, ISBN)
        self.link = link

    def check_out(self):
        print(f"Электронная книга {self.title} доступна для скачивания по ссылке {self.link}")

    def check_in(self):
        print(f"Электронная книгу {self.title} не вернуть обратно, читай")


class Audiobook(Book):
    def __init__(self, title: str, author: str, ISBN: str, link: str):
        super().__init__(title, author, ISBN)
        self.link = link

    def check_out(self):
        print(f"Аудиокнига {self.title} доступна для прослушивания по ссылке {self.link}")

    def check_in(self):
        print(f"Аудиокнига {self.title} не вернуть обратно, слушай")


if __name__ == "__main__":
    library = Library()
    book1 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
    book2 = Ebook("The Catcher in the Rye", "J.D. Salinger", "987654321", "www.example.com/ebooks/thecatcherintherye")
    book3 = Audiobook("The Catcher in the Rye", "J.D. Salinger", "876543219", "www.example.com/audiobooks/thecatcherintherye")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.check_out_book("123456789")
    library.check_out_book("876543219")
    library.check_in_book("876543219")
