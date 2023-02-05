from typing import Optional
BOOKS_DATABASE = [
    {
        "id": 1,
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
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None): #Конструктор принимает необязательный аргумент со значением по умолчанию
        books: Optional[list] #Если пользователь его не передал, то библиотека инициализируется с пустым списком книг.
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int: #Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        if self.books != []:
            return self.books[-1].id + 1 #Если книги есть, то возвращает идентификатор последней книги увеличенный на 1
        else:
            return 1 #Если книг в библиотеке нет, то возваращет 1

    def get_index_by_book_id(self, idt: int) -> int: #Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса
        if (self.books == []) or (idt >= len(self.books)):
            raise ValueError("Книги с запрашиваемым id не существует")

        for i, book in enumerate(self.books): #Если книга существует, то возвращает индекс из списка
            if book.id == idt:
                return i


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
