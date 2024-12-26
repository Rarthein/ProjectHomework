def get_mask_card_number(card_number: int) -> str:
    """Функция создающая маску из номера карты"""
    if not isinstance(card_number, int):
        raise TypeError("Номер карты должен состоять только из цифр")

    card_str = str(card_number)

    if len(card_str) != 16:
        return "Номер карты должен состоять из 16 цифр."

    masked_number = card_str[:4] + " " + card_str[4:6] + "** " + "**** " + card_str[-4:]

    return masked_number


def get_mask_account(account_number: int) -> str:
    """Функция создающая маску из номера счета"""

    if not isinstance(account_number, int):
        raise TypeError("Номер счета должен состоять только из цифр")

    account_str = str(account_number)

    masked_account = "**" + account_str[-4:]

    return masked_account



# card_number = input("Введите номер карты: ")
# masked_number = get_mask_card_number(card_number)


# if __name__ == "__main__":
#     try:
#         card_number = int(input("Введите номер карты: "))
#         masked_number = get_mask_card_number(card_number)
#         print(masked_number)
#     except ValueError:
#         print("Ошибка! Номер карты должен содержать только цифры!")
#
#     try:
#         account_number = int(input("Введите номер счета: "))
#         masked_account = get_mask_account(account_number)
#         print(masked_account)
#     except ValueError:
#         print("Ошибка! Номер счета должен содержать только цифры!")