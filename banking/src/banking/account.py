# account_management.py

'''from src import repository
from src import constants
from src.logging_config import logger'''

from . import constants
from . import repository
from .logging_config import logger

class Account:

    def __init__(self, customer_database, account_no):
        self.db = customer_database
        self.account_no = account_no

    @classmethod
    def account_open(cls, name, phone, password, dob, balance):
        
        acc_list = repository.load_account_numbers()

        if acc_list == []:
            acc_num = str(constants.START_ACCOUNT_NUMBER + 1)
        else:
            for account in range(constants.START_ACCOUNT_NUMBER + 1, max(acc_list) + 2):
                if account not in acc_list:
                    acc_num = str(account)
                    break

        db = repository.load_customer_db()

        if len(str(phone))!=10:             # Verifying Valid Mobile Number.
            raise ValueError("Please Enter Valid Phone Number! ")

        elif phone <= 0:
            raise ValueError("Please Enter Valid Phone Number!")
        
        elif balance <= 0:
            raise ValueError("Balance amount must be positive")

                    
        # Creating and handelling Object.
        obj = cls(db, acc_num)
            
        try:

            repository.save_account_numbers(acc_list,acc_num)       # Updating Database.
            repository.create_customer(acc_num, name, str(phone), password, dob, balance)
            logger.info(f"Account Created Successfully!")
            return acc_num, db[acc_num]

        except ValueError as e:
            print(str(e))
                    

    def update_account(self, name, dob, phone):
        
        if len(phone)!=10:             # Verifying Valid Mobile Number.
            raise ValueError("Please Enter Valid Phone Number! ")
        
        if phone <= 0:
            raise ValueError("Please Enter Valid Phone Number!")
        
        # Updating Database.
        self.db[self.account_no]["Name"] = name
        self.db[self.account_no]["Phone Number"] = phone
        self.db[self.account_no]["D.O.B"] = dob

        return self.db

    def password_update(self, old_pass, phone, new_pass):
                    
        if self.db[self.account_no]["Password"] != old_pass:                    # Verifying Password.
            raise ValueError("Wrong Password! Try Again!")    
                            
        if self.db[self.account_no]["Phone Number"] != phone:              # Verifying Phone Number.
            raise ValueError("Your Phone Number Does not Match.Try Again!")      
                            
        if self.db[self.account_no]["Password"] == new_pass:            # Verifying New Password.
            raise ValueError("Your Password Same As Old Password. Try Again!")
                                    
        return new_pass

    def account_deletion(self,phone,password):

        if self.db[self.account_no]["Phone Number"] != phone:
            raise ValueError("Your Phone Number Does not Match.Try Again!")

        if self.db[self.account_no]["Password"] != password:
             raise ValueError("Wrong Password.Try Again!")
        
        return self.db

