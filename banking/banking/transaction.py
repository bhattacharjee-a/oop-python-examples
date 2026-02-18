# Transaction.py

from . import constants
from . import repository



class Transaction:

    def __init__(self, account_no):
        self.account_no = account_no

    def deposit(self, amount):
        current = self.get_balance()

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        new_balance = current + amount
        repository.update_balance(self.account_no, new_balance)
        return new_balance

    def withdraw(self, amount):
        current = self.get_balance()
    
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > current:
            raise ValueError("Insufficient balance")
        
        new_balance = current - amount
        repository.update_balance(self.account_no, new_balance)
        return new_balance

    def get_balance(self):
        customer = repository.get_customer(self.account_no)
        return customer["Balance"]


