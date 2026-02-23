# conftest

import os
import tempfile
from banking import constants


def pytest_configure():
    # Create temporary folder for test database files
    temp_dir = tempfile.mkdtemp()

    constants.CUSTOMER_DB = os.path.join(temp_dir, "customer_database.json")
    constants.ADMIN_DB = os.path.join(temp_dir, "administrative_database.json")
    constants.ACCOUNT_NUMBERS = os.path.join(temp_dir, "account_numbers.json")
