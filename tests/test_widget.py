import pytest

from src.widget import mask_account_card, get_date


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
