def get_mask_card_number(card_number: int) -> str:
    """Функция создающая маску из номера карты"""

    card_str = str(card_number)

    if len(card_str) != 16:
        return "Номер карты должен состоять из 16 цифр"

    masked_number = card_str[:4] + " " + card_str[4:6] + "** " + "**** " + card_str[-4:]

    return masked_number


def get_mask_account(account_number: int) -> str:
    """Функция создающая маску из номера счета"""

    account_str = str(account_number)

    if len(account_str) < 16 or len(account_str) > 20:
        return "Номер счета должен быть от 16 до 20 цифр"

    masked_account = "**" + account_str[-4:]

    return masked_account
