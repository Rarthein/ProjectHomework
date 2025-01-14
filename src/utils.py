# import os
# import json
#
# # utils.py
# def load_transactions(file_path: str) -> list:
#     """
#     Читает данные о транзакциях из JSON-файла.
#
#     :param file_path: Путь до JSON-файла.
#     :return: Список транзакций (словарей). Пустой список, если файл не найден, пустой или не содержит список.
#     """
#     if not os.path.exists(file_path):
#         return "bad"
#
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             if isinstance(data, list):
#                 return data
#     except (json.JSONDecodeError, IOError):
#         pass
#
#     return []
#
# data_read = load_transactions('data/operations.json')
# print(data_read)

import json
import os


def read_transactions(file_path):
    try:
        if not os.path.exists(file_path):
            return 'bad2'

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []

            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []

data_read = read_transactions('data/operations.json')
print(data_read)

file_path = 'data/operations.json'
transactions = read_transactions(file_path)