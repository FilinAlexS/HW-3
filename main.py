import json
from json_read import users_list
from csv_read import books_list


class AllBooks:
    def __iter__(self):
        self.count_book = 0
        return self

    def __next__(self):
        if self.count_book < len(books_list):
            x = books_list[self.count_book]
            self.count_book += 1
            return x
        else:
            raise StopIteration


class AllUsers:
    def __iter__(self):
        self.count_users = 0
        return self

    def __next__(self):
        if self.count_users < len(users_list):
            x = users_list[self.count_users]
            self.count_users += 1
            return x
        else:
            raise StopIteration


count_books = 0
count_users = 1
users_list_with_books = []

books_class = AllBooks()
book_for_user = iter(books_class)

users_class = AllUsers()
user = iter(users_class)


while count_books <= len(books_list) - 1:
    for y in user:
        try:
            y["books"].append(next(book_for_user))
        except StopIteration:
            break
        else:
            count_books += 1
    count_users += 1


for y in user:
    users_list_with_books.extend([y])


with open("result.json", "w") as f:
    s = json.dumps(users_list_with_books, indent=4)
    f.write(s)
