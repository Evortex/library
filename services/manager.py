from services.library import Library
from models.book import Book

class LibraryManager:
    def __init__(self, data_file):
        """Инициализация менеджера библиотеки с файлом данных."""
        self.library = Library(data_file)

    def show_all_books(self):
        """Отобразить все книги в библиотеке."""
        if not self.library.books:
            print("Библиотека пуста.")
            return
        for book in self.library.books:
            print(f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def add_book(self):
        """Добавить новую книгу в библиотеку."""
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        book_id = self.generate_id()
        book = Book(book_id, title, author, year)
        self.library.add_book(book)
        print(f"Книга '{title}' успешно добавлена!")

    def remove_book(self):
        """Удалить книгу по ID."""
        book_id = int(input("Введите ID книги для удаления: "))
        self.library.remove_book(book_id)
        print(f"Книга с ID {book_id} удалена.")

    def search_books(self):
        """Поиск книг по ключевому слову."""
        query = input("Введите запрос для поиска: ")
        results = self.library.search_books(query)
        if results:
            for book in results:
                print(f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
        else:
            print("Книги не найдены.")

    def change_status(self):
        """Изменить статус книги (в наличии/выдана)."""
        book_id = int(input("Введите ID книги для изменения статуса: "))
        status = input("Введите новый статус (в наличии/выдана): ").lower()
        if status not in ["в наличии", "выдана"]:
            print("Некорректный статус.")
            return
        for book in self.library.books:
            if book.book_id == book_id:
                book.status = status
                self.library.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def generate_id(self):
        """Генерация нового уникального ID для книги."""
        if not self.library.books:
            return 1
        return max(book.book_id for book in self.library.books) + 1
