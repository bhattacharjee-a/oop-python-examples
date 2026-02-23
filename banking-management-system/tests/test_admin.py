# Admin Test.py
from banking import repository

def setup_function():
    # Start fresh DB for each test
    repository.save_customer_db({})

def test_create_customer_success():
    repository.create_customer(
        account_no="2001",
        name="AdminTest",
        phone="1234567890",
        password="adminpass",
        dob="01/01/2000",
        balance=500
    )

    customer = repository.get_customer("2001")
    assert customer is not None
    assert customer["Name"] == "AdminTest"
    assert customer["Balance"] == 500


def test_create_duplicate_customer():
    repository.save_customer_db({
        "2002": {
            "Name": "User",
            "Phone Number": "1111111111",
            "Password": "pass",
            "D.O.B": "01/01/2000",
            "Balance": 100
        }
    })

    try:
        repository.create_customer(
            account_no="2002",
            name="Duplicate",
            phone="9999999999",
            password="pass",
            dob="01/01/2000",
            balance=100
        )
        assert False
    except ValueError as e:
        assert "already exists" in str(e)


def test_delete_customer_success():
    repository.save_customer_db({
        "2003": {
            "Name": "DeleteMe",
            "Phone Number": "2222222222",
            "Password": "pass",
            "D.O.B": "01/01/2000",
            "Balance": 300
        }
    })

    repository.delete_customer("2003")
    customer = repository.get_customer("2003")
    assert customer is None


def test_update_customer_details():
    repository.save_customer_db({
        "2004": {
            "Name": "OldName",
            "Phone Number": "3333333333",
            "Password": "pass",
            "D.O.B": "01/01/2000",
            "Balance": 400
        }
    })

    repository.update_customer(
    "2004",
    {
        "Name": "NewName",
        "Phone Number": "4444444444"
    }
    )


    customer = repository.get_customer("2004")
    assert customer["Name"] == "NewName"
    assert customer["Phone Number"] == "4444444444"

