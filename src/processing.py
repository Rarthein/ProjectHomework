def filter_by_state(banking_operations: list, state="EXECUTED") -> list:
    """Функция для данных банковских операций возвращающая список словарей по заданному значению ключа state"""

    filtered_data = []
    for key in banking_operations:
        if key.get('state') == state:
            filtered_data.append(key)

    return filtered_data


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED"))

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], ""))


def sort_by_date(bank_data: list, reverse=True) -> list:
    """Функция сортировки списка словарей по дате в прямом или обратном порядке"""

    def get_date(item):
        return item['date']

    return sorted(bank_data, key=get_date, reverse=reverse)
