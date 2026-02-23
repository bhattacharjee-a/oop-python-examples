# Transaction Test

from banking import repository
from banking.transaction import Transaction

def setup_function():
    # Reset test database before each test
    repository.save_customer_db({
        "1001": {
            "Name": "TEST",
            "Phone Number": "9999999999",
            "Password": "pass",
            "D.O.B": "01/01/2000",
            "Balance": 100
        }
    })

def test_deposit_success():
    t = Transaction("1001")
    new_balance = t.deposit(50)
    assert new_balance == 150

def test_withdraw_success():
    t = Transaction("1001")
    new_balance = t.withdraw(40)
    assert new_balance == 60

def test_withdraw_insufficient_balance():
    t = Transaction("1001")
    try:
        t.withdraw(500)
        assert False  # should never reach here
    except ValueError as e:
        assert "Insufficient balance" in str(e)
