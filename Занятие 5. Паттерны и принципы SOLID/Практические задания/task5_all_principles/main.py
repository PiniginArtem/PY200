# TODO загрузить абстрактный метод
from typing import Union


class LibraryBookOut:
    # TODO нужно сделать абстрактным методом
    def check_out(self):
        pass


class LibraryBookIn:
    # TODO тоже абстрактный
    def check_in(self):
        pass


class Book:
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN


class PhysicalBook(# TODO что тут нужно добавить для разделения интерфейса?):
    def __init__(self, title: str, author: str, ISBN: str):
        # TODO что нужно написать, так как Book и PhysicalBook очень похожи?
        self.is_checked_out = False

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


class Ebook(# TODO а что тут?):
    def __init__(self, title: str, author: str, ISBN: str, link: str):
        # TODO как произвести расширение конструктора на базе какого-то класса?
        self.link = link

    def check_out(self):
        print(f"Электронная книга {self.title} доступна для скачивания по ссылке {self.link}")


class Audiobook(# TODO разделяем интерфейс):
    def __init__(self, title: str, author: str, ISBN: str, link: str):
        # TODO аналогично Ebook
        self.link = link

    def check_out(self):
        print(f"Аудиокнига {self.title} доступна для прослушивания по ссылке {self.link}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Union[LibraryBookIn, LibraryBookOut]): # Ранее была зависимость на абстракции LibraryBook, а что теперь?
        # TODO добавляем книги

    def check_out_book(self, ISBN: str):
        for book in self.books:
            if # ранее писали book.ISBN == ISBN, а что теперь нужно добавить к прошлой записи, чтобы обработать нужный интерфейс?:
                return book.check_out()
        print(f"Книга с ISBN {ISBN} не найдена.")

    def check_in_book(self, ISBN: str):
        for book in self.books:
            if # дописать проверку для cheek_in_book:
                return book.check_in()
        print(f"Книга с ISBN {ISBN} не найдена или не может быть возвращена.")


if __name__ == "__main__":
    library = Library()
    book1 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
    book2 = Ebook("The Catcher in the Rye", "J.D. Salinger", "987654321", "www.example.com/ebooks/thecatcherintherye")
    book3 = Audiobook("The Catcher in the Rye", "J.D. Salinger", "876543219",
                      "www.example.com/audiobooks/thecatcherintherye")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.check_out_book("123456789")
    library.check_out_book("876543219")
    library.check_in_book("876543219")
