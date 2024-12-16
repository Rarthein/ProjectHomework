inp_str = "Visa Platinum 7000792289606361"
parts = inp_str.split()
card_number = parts[-1]
print(parts)
print(card_number)
masked_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
print(masked_number)

""" if "Visa" in account_data:
        #Функция маски номеров карты или счета

        card_number = parts[-1]
        masked_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
        return f"{card_name} {masked_number}"
   elif "Maestro" in account_data:
        parts = account_data.split()
        card_number = parts[-1]
        masked_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
        return f"Maestro {masked_number}"
   elif "Счет" in account_data:
        parts = account_data.split()
        account_number = parts[-1]
        masked_account = "**" + account_number[-4:]
        return f"Счет {masked_account}"
   else:
        return "Ошибка ввода"
"""