import pytest

from main import BooksCollector


@pytest.fixture
def generate_books_genre():
    collector_books = BooksCollector()
    new_books_name = ['Гарри Поттер', 'Лёлик и Болик', 'Маленькая ведьма', 'Детектив Шерлок']
    genre_for_new_books = ['Фантастика', 'Мультфильмы', 'Фантастика', 'Детективы']
    for i in range(0, len(new_books_name)):
        collector_books.add_new_book(new_books_name[i])
        collector_books.set_book_genre(new_books_name[i], genre_for_new_books[i])
    return collector_books
