# import requests
#
# API_KEY = 'g789SGBI1udVa76Jn5BztdNjW2bIhXD1'  # Замените на ваш API ключ
# BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'
#
#
# def convert_to_rub(amount, currency):
#     if currency == 'RUB':
#         return float(amount)
#
#     params = {
#         'from': currency,
#         'to': 'RUB',
#         'amount': amount
#     }
#
#     headers = {
#         'apikey': API_KEY
#     }
#
#     try:
#         response = requests.get(BASE_URL, headers=headers, params=params)
#         response.raise_for_status()
#         data = response.json()
#
#         return float(data.get('result', 0))
#     except requests.RequestException as e:
#         print(f"Error fetching exchange rate: {e}")
#         return 0.0
#
#
# def get_transaction_amount_in_rub(transaction):
#     operation_amount = transaction.get('operationAmount', {})
#     amount = operation_amount.get('amount', 0)
#     currency = operation_amount.get('currency', {}).get('code', 'RUB')
#
#     return convert_to_rub(amount, currency)
