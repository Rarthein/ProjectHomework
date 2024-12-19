def filter_by_state(banking_operations: list, state="EXECUTED") -> list:
    """Функция для данных банковских операций возвращающая список словарей по заданному значению ключа state"""

    filtered_data = []
    for key in banking_operations:
        if key.get('state') == state:
            filtered_data.append(key)

    return filtered_data


def sort_by_date(bank_data: list, reverse=True) -> list:
    """Функция сортировки списка словарей по дате в прямом или обратном порядке"""

    def get_date(item):
        return item['date']

    return sorted(bank_data, key=get_date, reverse=reverse)
