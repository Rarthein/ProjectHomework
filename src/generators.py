from typing import Iterator, Union


def filter_by_currency(transactions_list: list[dict], currency: str) -> Union[Iterator[dict], str]:
    """Функция фильтрует список транзакций по заданной валюте"""

    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


transactions = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
                 "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                 "to": "Счет 14211924144426031657"},
                {"id": 987654321, "state": "", "date": "2020-05-01T10:15:30.123456",
                 "operationAmount": {"amount": "1234.56", "currency": {"name": "EUR", "code": "EUR"}},
                 "description": "Оплата услуг",
                 "from": "Счет 123456789", "to": "Счет 987654321"}]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> str:
    """Функция возвращает список описаний транзакций"""

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номера карт, начиная со стартового номера и заканчивая конечным номером"""

    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + ' ' + f"{number:016d}"[4:8] + ' ' + f"{number:016d}"[
                                                                         8:12] + ' ' + f"{number:016d}"[12:]


usd_transactions = filter_by_currency(transactions, "USD")
for elem in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)
for elem in range(3):
    print(next(descriptions))

card_numbers = card_number_generator(1, 5)
for card in card_numbers:
    print(card)
