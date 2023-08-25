import json
from json_read import users_list
from csv_read import books_list
from calc_books_on_user import get_book_each_user, get_book_residual

count_book = 0  # Счётчик книг, для получения книги из books_list по позиции
count_user = 0  # Счётчик пользователей, для правильной раздачи кол-ва книг каждому
books_for_user = []

for user in users_list:
    if count_user < get_book_residual():
        books_each = get_book_each_user() + 1
    else:
        books_each = get_book_each_user()

    while books_each > 0:
        books_for_user.append(books_list[count_book])
        count_book += 1
        books_each -= 1

    users_list[count_user]["books"].extend(books_for_user)
    books_for_user.clear()
    count_user += 1


with open("example.json", "w") as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)
