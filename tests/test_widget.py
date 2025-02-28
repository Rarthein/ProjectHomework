import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def mask_account():
    return [
        {"account_data": "Visa Platinum 8990922113665229", "expected": "visa platinum 8990 92** **** 5229"},
        {"account_data": "Maestro 7000792289606361", "expected": "maestro 7000 79** **** 6361"},
        {"account_data": "Мир 6831982476737658", "expected": "мир 6831 98** **** 7658"},
        {"account_data": "MasterCard 8300734726758", "expected": "Номер карты должен состоять из 16 цифр"},
        {"account_data": "MasterCard 7158300734726758778888", "expected": "Номер карты должен состоять из 16 цифр"},
        {"account_data": "Счет 8990922113665212329", "expected": "счет **2329"},
        {"account_data": "Maestro 7000792289606361", "expected": "maestro 7000 79** **** 6361"},
        {"account_data": "5698592289606361", "expected": "Неверный ввод"},
        {"account_data": "Maestro qw00792289606361", "expected": "Номер карты должен содержать только цифры"},
        {"account_data": "Счет sd888882113665212329", "expected": "Номер счета должен содержать только цифры"}
    ]


@pytest.mark.parametrize("mask_account_data", [
    {"account_data": "Visa Platinum 8990922113665229", "expected": "visa platinum 8990 92** **** 5229"},
    {"account_data": "Maestro 7000792289606361", "expected": "maestro 7000 79** **** 6361"},
    {"account_data": "Мир 6831982476737658", "expected": "мир 6831 98** **** 7658"},
    {"account_data": "MasterCard 8300734726758", "expected": "Номер карты должен состоять из 16 цифр"},
    {"account_data": "MasterCard 7158300734726758778888", "expected": "Номер карты должен состоять из 16 цифр"},
    {"account_data": "Счет 8990922113665212329", "expected": "счет **2329"},
    {"account_data": "Maestro 7000792289606361", "expected": "maestro 7000 79** **** 6361"},
    {"account_data": "5698592289606361", "expected": "Неверный ввод"},
    {"account_data": "Maestro qw00792289606361", "expected": "Номер карты должен содержать только цифры"},
    {"account_data": "Счет sd888882113665212329", "expected": "Номер счета должен содержать только цифры"}
])
def test_mask_account_card(mask_account_data):
    assert mask_account_card(mask_account_data["account_data"]) == mask_account_data["expected"]


def test_mask_account_card_fixture(mask_account):
    for data in mask_account:
        assert mask_account_card(data["account_data"]) == data["expected"]


@pytest.fixture
def input_data():
    return [
        {"date_operation": "2024-03-11T02:26:18.671407", "expected": "11.03.2024"},
        {"date_operation": "2085-08-12T01:02:85.555888", "expected": "12.08.2085"},
        {"date_operation": "0001-01-01T00:00:00.000000", "expected": "01.01.0001"},
        {"date_operation": "9999-12-31T23:59:59.999999", "expected": "31.12.9999"},
        {"date_operation": "0001-01-01T00:00:000.0000000", "expected": "Неверный формат даты"},
        {"date_operation": "0002-02-02T00:00:00", "expected": "Неверный формат даты"},
        {"date_operation": "8888-12-3123:59:59.8888888", "expected": "Неверный формат даты"},
        {"date_operation": "", "expected": "Отсутствует дата"}
    ]


@pytest.mark.parametrize("get_date_data", [
    {"date_operation": "2024-03-11T02:26:18.671407", "expected": "11.03.2024"},
    {"date_operation": "2085-08-12T01:02:85.555888", "expected": "12.08.2085"},
    {"date_operation": "0001-01-01T00:00:00.000000", "expected": "01.01.0001"},
    {"date_operation": "9999-12-31T23:59:59.999999", "expected": "31.12.9999"},
    {"date_operation": "0001-01-01T00:00:000.0000000", "expected": "Неверный формат даты"},
    {"date_operation": "0002-02-02T00:00:00", "expected": "Неверный формат даты"},
    {"date_operation": "8888-12-3123:59:59.8888888", "expected": "Неверный формат даты"},
    {"date_operation": "", "expected": "Отсутствует дата"}
])
def test_get_date(get_date_data):
    assert get_date(get_date_data["date_operation"]) == get_date_data["expected"]


def test_get_data_fixture(input_data):
    for data in input_data:
        assert get_date(data["date_operation"]) == data["expected"]
