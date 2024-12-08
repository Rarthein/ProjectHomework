from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> str:
    """Функция маскирует номер карты или счета"""

    parts = account_data.split()

    if len(parts) < 2:
        return "Неверный ввод"

    card_name = " ".join(parts[:-1])

    if card_name.lower() == "счет":
        account_number = int(parts[-1])
        masked_account = get_mask_account(account_number)
        return f"{card_name.lower()} {masked_account}"
    else:
        card_number = int(parts[-1])
        masked_number = get_mask_card_number(card_number)
        return f"{card_name.lower()} {masked_number}"


print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Счет 8990922113665229'))


def get_date(input_date: str) -> str:
    """Функция преобразует дату в нужный формат"""

    string_date = input_date.split('T')
    date_part = string_date[0]
    final_date = date_part.split('-')
    day = final_date[2]
    month = final_date[1]
    year = final_date[0]
    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))
