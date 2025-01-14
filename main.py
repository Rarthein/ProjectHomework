from src.utils import read_transactions
from src.external_api import get_transaction_amount_in_rub

file_path = 'data/operations.json'
transactions = read_transactions(file_path)

for transaction in transactions:
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    print(f"Transaction ID: {transaction['id']}, Amount in RUB: {amount_in_rub}")