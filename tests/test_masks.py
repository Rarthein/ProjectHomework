import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_data():
    """Фикстура для предоставления тестовых данных функции get_mask_card_number"""

    return [
        {"card_number": 1234567812345678, "expected": "1234 56** **** 5678"},
        {"card_number": 9999888877776666, "expected": "9999 88** **** 6666"},
        {"card_number": 12345678901234, "expected": "Номер карты должен состоять из 16 цифр"},
        {"card_number": 1234567890123456789, "expected": "Номер карты должен состоять из 16 цифр"},
        {"card_number": 0, "expected": "Номер карты должен состоять из 16 цифр"}
    ]


@pytest.mark.parametrize("card_masks", [
    {"card_number": 1234567812345678, "expected": "1234 56** **** 5678"},
    {"card_number": 9999888877776666, "expected": "9999 88** **** 6666"},
    {"card_number": 12345678901234, "expected": "Номер карты должен состоять из 16 цифр"},
    {"card_number": 1234567890123456789, "expected": "Номер карты должен состоять из 16 цифр"},
    {"card_number": 0, "expected": "Номер карты должен состоять из 16 цифр"}
])
def test_get_mask_card_number(card_masks):
    assert get_mask_card_number(card_masks["card_number"]) == card_masks["expected"]


def test_get_mask_card_number_fixture(card_data):
    for data in card_data:
        assert get_mask_card_number(data["card_number"]) == data["expected"]


@pytest.fixture
def account_data():
    """Фикстура для предоставления тестовых данных функции get_mask_account"""

    return [
        {"account_number": 1222223333344444, "expected": "**4444"},
        {"account_number": 12345678901234567890, "expected": "**7890"},
        {"account_number": 123456789, "expected": "Номер счета должен быть от 16 до 20 цифр"},
        {"account_number": 123456789123456789123456789, "expected": "Номер счета должен быть от 16 до 20 цифр"},
        {"account_number": 0, "expected": "Номер счета должен быть от 16 до 20 цифр"}
    ]


@pytest.mark.parametrize("account_masks", [
    {"account_number": 1222223333344444, "expected": "**4444"},
    {"account_number": 12345678901234567890, "expected": "**7890"},
    {"account_number": 123456789, "expected": "Номер счета должен быть от 16 до 20 цифр"},
    {"account_number": 123456789123456789123456789, "expected": "Номер счета должен быть от 16 до 20 цифр"},
    {"account_number": 0, "expected": "Номер счета должен быть от 16 до 20 цифр"}
])
def test_get_mask_account(account_masks):
    assert get_mask_account(account_masks["account_number"]) == account_masks["expected"]


def test_get_mask_account_fixture(account_data):
    for data in account_data:
        assert get_mask_account(data["account_number"]) == data["expected"]
