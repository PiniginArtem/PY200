from typing import Iterable, Optional


BOOKS_DATABASE = [
    {
        "id": 123,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int) or not isinstance(name, str) or not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list[Book] = None):

        self.len = 0
        self.list_books: list[Book] = []

        if books:
            self.init_list_books(books)

    def init_list_books(self, books: list[Book]):

        self.list_books = books
        self.len = len(self.list_books)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int):
        return self.list_books[index]

    def __iter__(self):
        for index in range(self.len):
            yield self.list_books[index]

    def get_next_book_id(self):
        return self.list_books[self.len - 1].id + 1 if self.len else 1

    def get_index_by_book_id(self, id_: int):
        for i, val in enumerate(self):
            if val.id == id_:
                return i
        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(123))  # проверяем индекс книги с id = 123
