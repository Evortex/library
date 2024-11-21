class Book:
    """Класс, представляющий книгу."""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Конвертирует объект книги в словарь."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        """Создает объект книги из словаря."""
        return Book(data["book_id"], data["title"], data["author"], data["year"], data["status"])
