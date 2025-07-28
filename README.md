# qa_python
# test_default_value_in_genre проверяет __init__ класса, а именно наличие конкретного значение в переменной типа список.
# test_set_book_genre_set_valid_genre проверяет установку значения существующего жанра в списке genre для новосозданной книги.
# test_set_book_genre_set_invalid_genre проверяет установку значения не суествующего жанра в списке genre для новосозданной книги.
# test_get_book_genre_get_genre_new_book проверяет что при запросе книги по имени выводится соответствующий ей жанр.
# test_get_books_with_specific_genre_parametrized проверяет принадлежность списка книг запрашиваемому жанру. 
# test_no_age_restricted_books_in_children_list проверяет, что в список детских книг не попали запрещенные жанры.
# test_add_book_in_favorites_add_one_book_not_from_list проверяет, что в ибранное не добавляется фильм не состоящий в словаре books_genre. 
# test_delete_book_from_favorites_dlt_one_book проверяет удаление ранее добавленной книги из списка избранных.
# test_get_list_of_favorites_books_after_added_to_list проверяет, что содержание списка избранных книг соответствует добавленным.
# test_get_book_genre_without_genre проверяет, что у добавленной книги не установлен жанр
# test_add_new_book_over_len проверяет, что название фильма с длиной больше допустимой не добавляется в словарь books_genre.
