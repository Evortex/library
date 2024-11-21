import json
from models.book import Book

class Library:
    def __init__(self, data_file):
        """Инициализация библиотеки с файлом для хранения данных."""
        self.data_file = data_file
        self.books = []  # Список книг в библиотеке
        self.load_books()  # Загружаем книги при инициализации

    def add_book(self, book):
        """Добавить книгу в библиотеку."""
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id):
        """Удалить книгу из библиотеки по id."""
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def search_books(self, query):
        """Искать книги по названию, автору или году."""
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == str(book.year)]

    def save_books(self):
        """Сохранить книги в файл."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def load_books(self):
        """Загрузить книги из файла."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                book_dicts = json.load(file)
                self.books = [Book.from_dict(book_dict) for book_dict in book_dicts]
        except FileNotFoundError:
            self.books = []  # Если файл не найден, начинаем с пустой библиотеки
        except json.JSONDecodeError:
            self.books = []  # Если ошибка в формате данных, начинаем с пустой библиотеки

