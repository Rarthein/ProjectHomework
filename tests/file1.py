from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_data: str) -> str:
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


print(mask_account_card(input("Введите наименование и номер карты или номер счета: ")))

"""'Visa Platinum 8990922113665229
    Счет 64686473678894779589'"""