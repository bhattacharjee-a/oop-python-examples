# Repository Test

from banking import repository

def setup_function():
    repository.save_customer_db({
        "1003": {
            "Name": "DEL",
            "Phone Number": "7777777777",
            "Password": "pass",
            "D.O.B": "03/03/2000",
            "Balance": 300
        }
    })

def test_update_balance():
    repository.update_balance("1003", 500)
    customer = repository.get_customer("1003")
    assert customer["Balance"] == 500

def test_delete_customer():
    repository.delete_customer("1003")
    customer = repository.get_customer("1003")
    assert customer is None

