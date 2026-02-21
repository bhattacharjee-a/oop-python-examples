# Repository.py

import json
#from banking import constants
from . import constants


# ---------- Admin Database ----------

def load_admin_db():
    try:
        with open(constants.ADMIN_DB, "r+") as file:
            content = file.read().strip()
    except (FileNotFoundError, FileExistsError):
        with open(constants.ADMIN_DB, "w+") as file:
            content = file.read().strip()

    if content == "":
        administrative_database = {}
    else:
        administrative_database = json.loads(content)

    return administrative_database


def save_admin_db(administrative_database):
    with open(constants.ADMIN_DB, "w") as file:
        json.dump(administrative_database, file, indent=2)


# ---------- Customer Database ----------

def load_customer_db():
    try:
        with open(constants.CUSTOMER_DB, "r+") as file:
            content = file.read().strip()
    except (FileNotFoundError, FileExistsError):
        with open(constants.CUSTOMER_DB, "w+") as file:
            content = file.read().strip()

    if content == "":
        customer_database = {}
    else:
        customer_database = json.loads(content)

    return customer_database


def save_customer_db(customer_database):
    with open(constants.CUSTOMER_DB, "w") as file:
        json.dump(customer_database, file, indent=2, sort_keys=True)


# ---------- Account Numbers ----------

def load_account_numbers():
    acc_list = []

    try:
        with open(constants.ACCOUNT_NUMBERS, "r+") as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    acc_list.append(int(line))
        acc_list.sort()

    except FileNotFoundError:
        with open(constants.ACCOUNT_NUMBERS, "w") as file:
            pass

    return acc_list


def save_account_numbers(acc_list, acc_num):
    if acc_num in acc_list:
        raise ValueError("Account already exists")
    else:
        acc_list.append(int(acc_num))

    with open(constants.ACCOUNT_NUMBERS, "w") as file:
        for num in acc_list:
            file.write(f"{num}\n")


# ---------- Repository Helper Functions ----------

def create_customer(account_no, name, phone, password, dob, balance):
    db = load_customer_db()

    if str(account_no) in db:
        raise ValueError("Account already exists")

    db[str(account_no)] = {
        "Name": name,
        "Phone Number": phone,
        "Password": password,
        "D.O.B": dob,
        "Balance": balance
    }

    save_customer_db(db)


def customer_exists(account_no):
    db = load_customer_db()
    return str(account_no) in db


def get_customer(account_no):
    db = load_customer_db()
    return db.get(str(account_no))


def create_customer(account_no, name, phone, password, dob, balance):
    db = load_customer_db()

    if str(account_no) in db:
        raise ValueError("Account already exists")

    db[str(account_no)] = {
        "Name": name,
        "Phone Number": phone,
        "Password": password,
        "D.O.B": dob,
        "Balance": balance
    }

    save_customer_db(db)

ALLOWED_FIELDS = {"Name", "Phone Number", "Password", "D.O.B", "Balance"}

def update_customer(account_no, updated_fields: dict):
    db = load_customer_db()

    if str(account_no) not in db:
        raise KeyError("Account not found!")

    for key in updated_fields:
        if key not in ALLOWED_FIELDS:
            raise ValueError(f"Invalid field: {key}")

    db[str(account_no)].update(updated_fields)
    save_customer_db(db)


# ---------- Business Operations ----------

def update_balance(account_no, new_balance):
    update_customer(account_no, {"Balance": new_balance})


def delete_customer(account_no):
    db = load_customer_db()

    if str(account_no) not in db:
        raise KeyError("Account not found")

    db.pop(str(account_no))
    save_customer_db(db)
