import pytest

from main import BooksCollector


class TestBooksCollector:
    #  Тест: добавление 4-х книг в словарь
    def test_add_new_book_add_four_books(self, generate_books_genre):
        assert len(generate_books_genre.get_books_genre()) == 4

    # Тест: проверяем количество символов в имени книги
    @pytest.mark.parametrize('new_name_book', [
        'Планета Сокровищ, одна из самых интересных книг',
        '',
        ' '
    ])
    def test_add_new_book_check_symbol_in_name_book(self, new_name_book):
        collector_books = BooksCollector()
        collector_books.add_new_book(new_name_book)
        assert len(collector_books.books_genre) == 0

    # Тест: проверяем, что нельзя добавлять одинаковые книги
    def test_add_new_book_check_duplicate_name_book(self):
        collector_books = BooksCollector()
        collector_books.add_new_book('Гарри Поттер')
        collector_books.add_new_book('Гарри Поттер')
        assert len(collector_books.books_genre) == 1

    # Тест: добавление жанра
    @pytest.mark.parametrize('name_book, name_genre', [
        ['Гарри Поттер', 'Фантастика'],
        ['Бронепароходы', 'Детективы']
    ])
    def test_set_book_genre_set_two_genre_for_books(self, name_book, name_genre):
        collector_books = BooksCollector()
        collector_books.add_new_book(name_book)
        collector_books.set_book_genre(name_book, name_genre)
        assert collector_books.books_genre[name_book] == name_genre

    # Тест: добавляем несуществующий жанр
    @pytest.mark.parametrize('name_book, name_genre', [
        ['Детство Максима Горького', 'Автобиография'],
        ['Как ловить рыбу', ' ']
    ])
    def test_set_book_genre_set_non_existent_genre_for_books(self, name_book, name_genre):
        collector_books = BooksCollector()
        collector_books.add_new_book(name_book)
        expected_books_genre = {
            name_book: ''
        }
        collector_books.set_book_genre(name_book, name_genre)
        assert collector_books.books_genre == expected_books_genre

    # Тест: получить жанр книги по имени
    def test_get_book_genre_get_genre_for_one_book(self, name_book='Гарри Поттер', name_genre='Фантастика'):
        collector_books = BooksCollector()
        collector_books.add_new_book(name_book)
        collector_books.set_book_genre(name_book, name_genre)
        assert collector_books.get_book_genre(name_book) == name_genre

    # Тест: получить список из 1 книги в жанре Детективы
    def test_get_books_with_specific_genre_get_book_genre_detectives(self, generate_books_genre):
        assert 'Детектив Шерлок' in generate_books_genre.get_books_with_specific_genre('Детективы') and len(
            generate_books_genre.get_books_with_specific_genre('Детективы')) == 1

    # Тест: получить словарь с книгами (не пусто (содержит 1-у книгу))
    def test_get_books_genre_contains_one_book(self, name_book='Гарри Поттер', name_genre='Фантастика'):
        collector_books = BooksCollector()
        collector_books.add_new_book(name_book)
        collector_books.set_book_genre(name_book, name_genre)
        assert str(collector_books.get_books_genre()) == "{'Гарри Поттер': 'Фантастика'}"

    # Тест: получить пустой словарь с книгами
    def test_get_books_genre_empty(self):
        collector_books = BooksCollector()
        assert len(collector_books.get_books_genre()) == 0

    # Тест: получить подходящие книги для ребёнка
    def test_get_books_for_children_proper_book(self, generate_books_genre):
        expected_books_for_children = ['Гарри Поттер', 'Лёлик и Болик', 'Маленькая ведьма']
        assert generate_books_genre.get_books_for_children() == expected_books_for_children

    # Тест: для ребёнка нет подходящих книг
    def test_get_books_for_children_empty(self, name_book='Чёрная борода', name_genre='Ужастик'):
        collector_books = BooksCollector()
        collector_books.add_new_book(name_book)
        collector_books.set_book_genre(name_book, name_genre)
        assert len(collector_books.get_books_for_children()) == 0

    # Тест: добавили 1-у книгу в избранные
    def test_add_book_in_favorites_add_one_new_book(self):
        collector_books = BooksCollector()
        collector_books.add_new_book('Лёлик и Болик')
        expected_book_in_favorites = ['Лёлик и Болик']
        collector_books.add_book_in_favorites('Лёлик и Болик')
        assert collector_books.favorites == expected_book_in_favorites

    # Тест: пытаемся добавить книгу, которая есть в избранных
    def test_add_book_in_favorites_add_duplicate_book(self):
        collector_books = BooksCollector()
        collector_books.add_new_book('Лёлик и Болик')
        collector_books.add_new_book('Планета сокровищ')
        expected_book_in_favorites = ['Лёлик и Болик']
        collector_books.add_book_in_favorites('Лёлик и Болик')
        collector_books.add_book_in_favorites('Лёлик и Болик')
        assert len(collector_books.favorites) == 1 and collector_books.favorites == expected_book_in_favorites

    # Тест: удалить 1-у книгу из избранных
    def test_delete_book_from_favorites_delete_one_book(self):
        collector_books = BooksCollector()
        collector_books.favorites = ['Лёлик и Болик', 'Приключение капитошки']
        collector_books.delete_book_from_favorites('Приключение капитошки')
        assert 'Приключение капитошки' not in collector_books.favorites and len(collector_books.favorites) == 1

    # Тест: получить список избранных книг
    def test_get_list_of_favorites_books_get_favorites(self):
        collector_books = BooksCollector()
        collector_books.favorites = ['Лёлик и Болик', 'Приключение капитошки']
        expected_book_in_favorites = ['Лёлик и Болик', 'Приключение капитошки']
        actual_book_in_favorites = collector_books.get_list_of_favorites_books()
        assert actual_book_in_favorites == expected_book_in_favorites

    # Тест: получить пустой список избранных книг
    def test_get_list_of_favorites_books_get_empty(self):
        collector_books = BooksCollector()
        assert len(collector_books.get_list_of_favorites_books()) == 0
