import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [{"id": 1, "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
             "description": "Payment in USD"},
            {"id": 2, "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
             "description": "Payment in EUR"},
            {"id": 3, "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
             "description": "Another payment in USD"}]


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("GBP", 0)
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count, f"Expected {expected_count} transactions for currency {currency}"


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0, "Expected empty result for an empty transactions list"


def test_filter_by_currency_missing_currency_field():
    transactions = [{"id": 1, "operationAmount": {"amount": "100.00"}}]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0, "Expected no transactions when currency field is missing"


@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([
         {"description": "Payment 1"},
         {"description": "Payment 2"}
     ], ["Payment 1", "Payment 2"]),
    ([], []),
    ([{"id": 1}], [])
])
def test_transaction_descriptions(transactions, expected_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions, f"Expected descriptions: {expected_descriptions}"


@pytest.mark.parametrize("start, end, expected_cards", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
    (0, 0, ["0000 0000 0000 0000"])
])
def test_card_number_generator(start, end, expected_cards):
    result = list(card_number_generator(start, end))
    assert result == expected_cards, f"Expected card numbers: {expected_cards}"


def test_card_number_generator_empty_range():
    result = list(card_number_generator(5, 4))
    assert result == [], "Expected an empty list for an invalid range"
