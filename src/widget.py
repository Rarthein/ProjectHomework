from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> str:
    """Функция маскирует номер карты или счета"""

    parts = account_data.split()

    if len(parts) < 2:
        return "Неверный ввод"

    card_name = " ".join(parts[:-1])

    if card_name.lower() == "счет":
        if len(parts[-1]) < 16 or len(parts[-1]) > 20:
            return "Номер счета должен быть от 16 до 20 цифр"
        if not parts[-1].isdigit():
            return "Номер счета должен содержать только цифры"
        account_number = int(parts[-1])
        masked_account = get_mask_account(account_number)
        return f"{card_name.lower()} {masked_account}"
    else:
        if len(parts[-1]) != 16:
            return "Номер карты должен состоять из 16 цифр"
        if not parts[-1].isdigit():
            return "Номер карты должен содержать только цифры"
        card_number = int(parts[-1])
        masked_number = get_mask_card_number(card_number)
        return f"{card_name.lower()} {masked_number}"


# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Maestro 7000792289606361'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Мир 6831982476737658'))
# print(mask_account_card('Счет 8990922113665212329'))


def get_date(input_date: str) -> str:
    """Функция преобразует дату в нужный формат"""

    string_date = input_date.split('T')
    date_part = string_date[0]
    final_date = date_part.split('-')
    day = final_date[2]
    month = final_date[1]
    year = final_date[0]
    return f"{day}.{month}.{year}"

# print(get_date("2024-03-11T02:26:18.671407"))
