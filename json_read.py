import json
from files import JSON_PATH_FILE

users_list = []

with open(JSON_PATH_FILE, "r") as f:
    list_users = json.loads(f.read())

for user in list_users:
    users_list.append({"name": user.get("name"),
                       "gender": user.get("gender"),
                       "address": user.get("address"),
                       "age": user.get("age"),
                       "books": []
                       })


def get_len_users() -> int:
    return len(users_list)
