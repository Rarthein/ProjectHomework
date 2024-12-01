def mask_account_card(account_data: str) -> str:
    if "Visa Platinum" in account_data:
        """Функция маски номеров карты или счета"""
        # Маскируем номер карты для Visa Platinum
        parts = account_data.split()
        card_number = parts[-1]
        masked_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
        return masked_number
    elif "Maestro" in account_data:
        # Маскируем номер карты для Maestro
        parts = account_data.split()
        card_number = parts[-1]
        masked_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
        return masked_number
    elif "Счет" in account_data:
        # Маскируем номер счета
        parts = account_data.split()
        account_number = parts[-1]
        masked_account = "**" + account_number[-4:]
        return masked_account
    else:
        return "Ошибка ввода"
