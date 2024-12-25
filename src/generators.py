def filter_by_currency(transactions_list, currency):
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
                 "to": "Счет 75651667383060284188"}]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions):
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start, end):
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + ' ' + f"{number:016d}"[4:8] + ' ' + f"{number:016d}"[
                                                                         8:12] + ' ' + f"{number:016d}"[12:]


transactions = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации", "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 987654321, "state": "", "date": "2020-05-01T10:15:30.123456",
                 "operationAmount": {"amount": "1234.56", "currency": {"name": "EUR", "code": "EUR"}},
                 "description": "Оплата услуг",
                 "from": "Счет 123456789", "to": "Счет 987654321"}]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)
for _ in range(3):
    print(next(descriptions))

card_numbers = card_number_generator(1, 5)
for card in card_numbers:
    print(card)
