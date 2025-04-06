# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические). Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции. Пропишите запись и считывание (get, set) инкапсулированных полей.
# ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ.
# Вар.1 	Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# б) список книг, выпущенных после заданного года.
# добавить: __setattr__, __str__, 2 маг арифметических метода, 2 маг оператора сравнения, __new__, __del__

class Book:
    book_count = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, book_id, title, authors, publisher, year, pages, price, binding_type):
        self.id = book_id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.price = price
        self.binding_type = binding_type
        Book.book_count += 1

    # Получения информации о книге
    def get_book_info(self):
        return f"{self.title} by {self.authors}, published by {self.publisher} in {self.year}, {self.pages} pages, ${self.price}, Binding: {self.binding_type}"

    # Метод для изменения цены
    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            print("Цена должна быть положительным числом!")

    def get_price(self):
        return self.price

    # Статический метод для получения общего количества книг
    @staticmethod
    def get_book_count():
        return Book.book_count

    # Метод класса для фильтрации книг по автору
    @classmethod
    def books_by_author(cls, books, author):
        return [book for book in books if author in book.authors]

    # Метод класса для фильтрации книг по году издания
    @classmethod
    def books_after_year(cls, books, year):
        return [book for book in books if book.year > year]

    # Метод __str__
    def __str__(self):
        return f"Book: {self.title}, Author(s): {self.authors}, Publisher: {self.publisher}, Year: {self.year}"

    # Магический метод __setattr__
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        super().__setattr__(name, value)

    # Магический метод для сложения цен книг
    def __add__(self, other):
        if isinstance(other, Book):
            return self.price + other.price
        return NotImplemented

    # Магический метод для сравнения книг по цене
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.price == other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.price < other.price
        return NotImplemented

    # Магический метод __del__ для удаления книги
    def __del__(self):
        print(f"Книга '{self.title}' была удалена.")
        Book.book_count -= 1


book1 = Book(1, "1984", "George Orwell", "Secker & Warburg", 1949, 328, 15, "Hardcover")
book2 = Book(2, "Pride and Prejudice", "Jane Austen", "T. Egerton", 1813, 279, 12, "Paperback")
book3 = Book(3, "To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", 1960, 281, 18, "Hardcover")
book4 = Book(4, "The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", 1925, 218, 10, "Paperback")

books = [book1, book2, book3, book4]

# Вывод
author_to_search = "Harper Lee"
books_by_author = Book.books_by_author(books, author_to_search)
print(f"Книги автора {author_to_search}:")
for book in books_by_author:
    print(book.get_book_info())

year_to_search = 1950
books_after_year = Book.books_after_year(books, year_to_search)
print(f"\nКниги, выпущенные после {year_to_search} года:")
for book in books_after_year:
    print(book.get_book_info())

print(f"\nСуммарное количество страниц книги 1 и книги 2: {book1 + book2} страниц.")

print(f"\nКнига 1 и книга 2 имеют одинаковое количество страниц: {book1 == book2}")
print(f"Книга 1 имеет меньше страниц, чем книга 2: {book1 < book2}")

book1.set_price(20)  
book2.set_price(-5)  # Некорректное изменение (выведется сообщение)
print(f"\nНовая цена книги '{book1.title}': {book1.get_price()}")





