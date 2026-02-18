# Account Test


from banking import repository
from banking.account import Account

def setup_function():
    repository.save_customer_db({
        "1002": {
            "Name": "USER",
            "Phone Number": "8888888888",
            "Password": "oldpass",
            "D.O.B": "02/02/2000",
            "Balance": 200
        }
    })

def test_password_update_success():
    db = repository.load_customer_db()
    acc = Account(db, "1002")

    new_pass = acc.password_update(
        old_pass="oldpass",
        phone="8888888888",
        new_pass="newpass"
    )

    assert new_pass == "newpass"

def test_password_update_wrong_old_password():
    db = repository.load_customer_db()
    acc = Account(db, "1002")

    try:
        acc.password_update("wrong", "8888888888", "newpass")
        assert False
    except ValueError as e:
        assert "Wrong Password" in str(e)
