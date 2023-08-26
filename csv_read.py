from csv import DictReader
from files import CSV_PATH_FILE

books_list = []

with open(CSV_PATH_FILE, newline='') as f:
    reader = DictReader(f)

    for row in reader:
        books_list.append(row)


def get_len_books() -> int:
    return len(books_list)
