from json_read import get_len_users
from csv_read import get_len_books

books = get_len_books()
all_users = get_len_users()


def get_book_each_user() -> int:
    return books // all_users


def get_book_residual() -> int:
    return books % all_users
