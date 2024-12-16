import pytest


def get_mask_card_number(card_number: int) -> str:
    """Функция создающая маску из номера карты"""

    if not isinstance(card_number, int):
        raise TypeError("Номер карты должен состоять только из цифр")
    card_str = str(card_number)

    if len(card_str) != 16:
        return "Номер карты должен состоять из 16 цифр."

    masked_number = card_str[:4] + " " + card_str[4:6] + "** " + "**** " + card_str[-4:]

    return masked_number


@pytest.fixture
def valid_card_numbers():
    """Фикстура для валидных номеров карт"""
    return [
        (1234567812345678, "1234 56** **** 5678"),
        (9999888877776666, "9999 88** **** 6666"),
        (1111222233334444, "1111 22** **** 4444"),
    ]


@pytest.fixture
def invalid_card_numbers():
    """Фикстура для невалидных номеров карт"""
    return [
        (12345678901234, "Номер карты должен состоять из 16 цифр."),
        (1234567890123456789, "Номер карты должен состоять из 16 цифр."),
        (0, "Номер карты должен состоять из 16 цифр."),
    ]


@pytest.mark.parametrize("card_number, expected", [
    (1234567812345678, "1234 56** **** 5678"),
    (9999888877776666, "9999 88** **** 6666"),
    (1111222233334444, "1111 22** **** 4444"),
    (12345678901234, "Номер карты должен состоять из 16 цифр."),
    (1234567890123456789, "Номер карты должен состоять из 16 цифр."),
    (0, "Номер карты должен состоять из 16 цифр."),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_valid(valid_card_numbers):
    for card_number, expected in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid(invalid_card_numbers):
    for card_number, expected in invalid_card_numbers:
        assert get_mask_card_number(card_number) == expected


if __name__ == "__main__":
    pytest.main()
