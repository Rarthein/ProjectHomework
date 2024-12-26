# import pytest
#
#
# def get_mask_card_number(card_number: int) -> str:
#     """Функция создающая маску из номера карты"""
#
#     if not isinstance(card_number, int):
#         raise TypeError("Номер карты должен состоять только из цифр")
#     card_str = str(card_number)
#
#     if len(card_str) != 16:
#         return "Номер карты должен состоять из 16 цифр."
#
#     masked_number = card_str[:4] + " " + card_str[4:6] + "** " + "**** " + card_str[-4:]
#
#     return masked_number
#
#
# @pytest.fixture
# def valid_card_numbers():
#     """Фикстура для валидных номеров карт"""
#     return [
#         (1234567812345678, "1234 56** **** 5678"),
#         (9999888877776666, "9999 88** **** 6666"),
#         (1111222233334444, "1111 22** **** 4444"),
#     ]
#
#
# @pytest.fixture
# def invalid_card_numbers():
#     """Фикстура для невалидных номеров карт"""
#     return [
#         (12345678901234, "Номер карты должен состоять из 16 цифр."),
#         (1234567890123456789, "Номер карты должен состоять из 16 цифр."),
#         (0, "Номер карты должен состоять из 16 цифр."),
#     ]
#
#
# @pytest.mark.parametrize("card_number, expected", [
#     (1234567812345678, "1234 56** **** 5678"),
#     (9999888877776666, "9999 88** **** 6666"),
#     (1111222233334444, "1111 22** **** 4444"),
#     (12345678901234, "Номер карты должен состоять из 16 цифр."),
#     (1234567890123456789, "Номер карты должен состоять из 16 цифр."),
#     (0, "Номер карты должен состоять из 16 цифр."),
# ])
# def test_get_mask_card_number(card_number, expected):
#     assert get_mask_card_number(card_number) == expected
#
#
# def test_get_mask_card_number_valid(valid_card_numbers):
#     for card_number, expected in valid_card_numbers:
#         assert get_mask_card_number(card_number) == expected
#
#
# def test_get_mask_card_number_invalid(invalid_card_numbers):
#     for card_number, expected in invalid_card_numbers:
#         assert get_mask_card_number(card_number) == expected
#
#
# if __name__ == "__main__":
#     pytest.main()


import pytest

# Функция для тестирования
def filter_by_state(banking_operations, state="EXECUTED"):
    filtered_data = []
    for key in banking_operations:
        if key.get('state') == state:
            filtered_data.append(key)
    return filtered_data

# Фикстура с тестовыми данными
@pytest.fixture
def sample_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

# Параметризация тестов для различных значений статуса state
@pytest.mark.parametrize("state, expected_result", [
    ("EXECUTED", [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ("CANCELED", [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]),
    ("PENDING", [])  # Проверка, когда нет словарей с указанным статусом
])
def test_filter_by_state(sample_data, state, expected_result):
    assert filter_by_state(sample_data, state) == expected_result

# Тестирование фильтрации списка словарей по заданному статусу state
def test_filter_executed(sample_data):
    result = filter_by_state(sample_data, "EXECUTED")
    assert result == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

# Проверка работы функции при отсутствии словарей с указанным статусом state в списке
def test_filter_no_matches(sample_data):
    result = filter_by_state(sample_data, "NON_EXISTENT_STATE")
    assert result == []
