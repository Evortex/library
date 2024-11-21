import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        """Создает объект книги для тестов"""
        self.book = Book(1, "Test Book", "Author", 2024)

    def test_book_creation(self):
        """Тест создания книги"""
        self.assertEqual(self.book.book_id, 1)
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Author")
        self.assertEqual(self.book.year, 2024)
        self.assertEqual(self.book.status, "в наличии")

    def test_to_dict(self):
        """Тест преобразования книги в словарь"""
        book_dict = self.book.to_dict()
        self.assertEqual(book_dict, {
            "book_id": 1,
            "title": "Test Book",
            "author": "Author",
            "year": 2024,
            "status": "в наличии"
        })

    def test_from_dict(self):
        """Тест создания книги из словаря"""
        book_dict = {
            "book_id": 1,
            "title": "Test Book",
            "author": "Author",
            "year": 2024,
            "status": "в наличии"
        }
        new_book = Book.from_dict(book_dict)
        self.assertEqual(new_book.book_id, 1)
        self.assertEqual(new_book.title, "Test Book")
        self.assertEqual(new_book.author, "Author")
        self.assertEqual(new_book.year, 2024)
        self.assertEqual(new_book.status, "в наличии")

if __name__ == "__main__":
    unittest.main()
