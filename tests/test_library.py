import unittest
from services.library import Library
from models.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создает объект библиотеки для тестов"""
        self.library = Library(data_file="test_library.json")
        self.library.books = []  # Очищаем библиотеку перед каждым тестом

    def test_add_book(self):
        """Тест добавления книги"""
        book = Book(1, "Test Book", "Author", 2024)
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self):
        """Тест удаления книги"""
        book = Book(1, "Test Book", "Author", 2024)
        self.library.add_book(book)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        """Тест поиска книг"""
        book = Book(1, "Test Book", "Author", 2024)
        self.library.add_book(book)
        results = self.library.search_books("Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

    def test_save_and_load_books(self):
        """Тест сохранения и загрузки книг"""
        book = Book(1, "Test Book", "Author", 2024)
        self.library.add_book(book)
        self.library.save_books()
        new_library = Library(data_file="test_library.json")
        new_library.load_books()
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "Test Book")

if __name__ == "__main__":
    unittest.main()
