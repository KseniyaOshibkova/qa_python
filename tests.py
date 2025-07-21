import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    test_books = [
        ('Достать ножи', 'Комедии'),
        ('Котенок по имени Гав', 'Мультфильмы'),
        ('Крик', 'Ужасы'),
        ('Дело о пропавшем кольце', 'Детективы'),
        ('Куб', 'Фантастика'),
        ('Чумовая пятница', 'Комедии')]

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_default_value_in_genre(self):
        collector = BooksCollector()
        assert 'Фантастика' in collector.genre

    @pytest.mark.parametrize('name,genre', [['Оно', 'Ужасы'], ['Дорога', 'Драма']])
    def test_set_book_genre_set_valid_and_invalid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        if genre in collector.genre:
            assert collector.get_book_genre('Оно') == 'Ужасы'
        else:
            assert collector.get_book_genre('Дорога') == ''

    def test_get_book_genre_get_genre_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бегущий человек')
        collector.set_book_genre(name='Бегущий человек', genre='Фантастика')
        assert collector.get_book_genre(name='Бегущий человек') == 'Фантастика'

    @pytest.mark.parametrize('genre, expected_books', [
        ('Комедии', ['Достать ножи', 'Чумовая пятница']),
        ('Ужасы', ['Крик']),
        ('Фантастика', ['Куб'])])
    def test_get_books_with_specific_genre_parametrized(self, genre, expected_books):
        collector = BooksCollector()
        for name, book_genre in self.test_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_no_age_restricted_books_in_children_list(self):
        collector = BooksCollector()
        for name, genre in self.test_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        children_books = collector.get_books_for_children()

        for name, genre in self.test_books:
            if genre in collector.genre_age_rating:
                assert name not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Котенок по имени Гав')
        collector.add_book_in_favorites('Котенок по имени Гав')
        assert 'Котенок по имени Гав' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_one_book_not_from_list(self):
        collector = BooksCollector()

        for name, genre in self.test_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        collector.add_book_in_favorites(name='От заката до рассвета')
        assert 'От заката до рассвета' not in collector.favorites

    @pytest.mark.parametrize('name,genre', test_books)
    def test_delete_book_from_favorites_dlt_one_book(self, name, genre):
        collector = BooksCollector()

        for book_name, book_genre in self.test_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        collector.add_book_in_favorites(name='Котенок по имени Гав')
        collector.delete_book_from_favorites(name='Котенок по имени Гав')
        assert 'Котенок по имени Гав' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name,genre', test_books)
    def test_get_list_of_favorites_books_after_added_to_list(self, name, genre):
        collector = BooksCollector()

        for book_name, book_genre in self.test_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        for name in collector.books_genre:
            collector.add_book_in_favorites(name)
        for book in self.test_books:
            assert book[0] in collector.get_list_of_favorites_books()

    def test_get_book_genre_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Красотка')
        assert collector.get_book_genre('Красотка') == ""

    def test_add_new_book_over_len(self):
        collector = BooksCollector()
        long_name = 'Вечное сияние чистого разума и много много много другого'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()
