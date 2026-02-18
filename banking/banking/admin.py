# Admin.py

import constants
import repository
from logging_config import logger
from account import Account

class Admin:

    def __init__(self, administrative_info, customer_database):
        self.administrative_database = administrative_info
        self.customer_database = customer_database

    @classmethod
    def verification(cls):

        administrative_database = repository.load_admin_db()
        customer_database = repository.load_customer_db()

        if "Name" not in administrative_database:
            administrative_database["Name"] = []

        if "Password" not in administrative_database:
            administrative_database["Password"] = "admin"
        
        for attempt in range(constants.MAX_ATTEMPTS):                   # verifying Existing Customer & Handling wrong Inputs.
            name = input("Enter Name:").upper()
            password = input("Enter Administrative Password:")
                    
            if name not in administrative_database["Name"]:            # verifying Administrative Details.
                logger.warning("Name Doesn't Exist!")
                continue

            if administrative_database["Password"] != password:
                logger.warning("Invalid Password!")
                continue

            logger.debug("Database Loaded Successfully!")
            logger.info("Information Found!")
            
            obj = Admin(administrative_database, customer_database)
            obj.main_menu()
            
            

        if attempt == (constants.MAX_ATTEMPTS-1):
            logger.error("Too many failed attempts.")


        return

    def main_menu(self):

        for attempt in range(constants.MAX_ATTEMPTS):    
            operation=input("Choose operation:\n1. Member Management\n2. Customer Management\n3. Administrative Password Management.\n4. Print Database\n5.Exit:\n\nEnter choice:")
            
            if operation == "1":
                self.member_management()
                return
            elif operation == "2":
                self.customer_management()
                return
            elif operation == "3":
                self.password_management()
                return
            elif operation == "4":
                self.print_database()
                return
            elif operation == "5":
                return
            else:
                logger.warning("Invalid Input! Try Again.")
                
        return

    def member_management(self):

        for attempt in range(constants.MAX_ATTEMPTS):

            operation=input("Choose operation:\n1. Adding Member \n2. Removing Member.\n3. Exit:\n\nEnter choice:")
            
            if operation == "1":

                name = input("Enter New Name:").upper()

                if name in self.administrative_database["Name"]:
                    logger.info("Name Already Exist!")
                    continue

                self.administrative_database["Name"].append(name)
                repository.save_admin_db(self.administrative_database)
                logger.info("Member Added Successfully!")
                return

            elif operation == "2":

                name = input("Enter Name To Remove:").upper()
                if name in self.administrative_database["Name"]: 

                    self.administrative_database["Name"].remove(name)
                    repository.save_admin_db(self.administrative_database)
                    logger.info("Member Removed Successfully!")
                    return
                    
                else:
                    logger.warning("Name Doesn't Exist. Try Again.")

            else:

                logger.warning("Wrong Input! Try Again.")

            attempt += 1

        return

    def customer_management(self):

        for attempt in range(constants.MAX_ATTEMPTS):

            operation=str(input("Choose operation:\n1. Adding Customer. \n2. Removing Customer.\n3. Exit:\n\nEnter choice:"))
                
            if operation == "1":

                name = input("Enter Your Name:").upper()
                ph_number = input("Enter Your Phone Number (Without +91):")

                try:
                    phone = int(ph_number)          
                except ValueError:
                    logger.warning("Enter Valid Phone Number!")
                    continue

                password = input("Enter Password:")
                dob = input("Enter Your D.O.B (DD/MM/YYYY):")
                amount = input("Enter The opening Balance Ammout:").strip()

                try:
                    balance = int(amount)          
                except ValueError:
                    logger.warning("Balance amount must be a valid number")
                    continue

                acc_no, data = Account.account_open(name, phone, password, dob, balance)
                print(f"Account Created Successfully!\nAccount Number: {acc_no}\n{data}")

            elif operation == "2":
               
                account_no = input ("Enter Customer Account Number:")

                if not repository.customer_exists(account_no):
                    logger.warning("Invalid Account Number / Customer Doesn't Exist")
                    continue

                # Removing Account Number From Existing Account Number List.
                acc_list = repository.load_account_numbers()
                acc_list.remove(int(account_no))
                repository.save_account_numbers(acc_list)

                # Removing Customer Details From Database.               
                repository.delete_customer(account_no)

                logger.info("Account Deleted Successfully.")
                return

            elif operation == "3":
                return
                
            else:
                logger.warning("Wrong Input! Try Again.")

            
        return

    def password_management(self):
        
        for attempt in range(constants.MAX_ATTEMPTS):

            operation=input("Choose operation:\n1. Current Password \n2. Changing Password.\n3. Exit:\n\nEnter choice:")
                
            if operation == "1":
                print(f"Current Administrative Password: {self.administrative_database['Password']}")

            elif operation == "2":
                old_pass=str(input("Enter Current Administrative Password:")).strip()

                if self.administrative_database["Password"] != old_pass:
                    logger.warning("Entered Wrong Password! Try Again.")
                    continue
                   
                new_pass=str(input("Enter New Administrative Password:")).strip()
                self.administrative_database["Password"] = new_pass
                repository.save_admin_db(self.administrative_database)
                logger.info("Password Updated Successfully.")

            elif operation == "3":
                return

            attempt += 1
            
        return

    def print_database(self):
        
        for attempt in range(constants.MAX_ATTEMPTS):

            operation=input("Choose operation:\n1. Print Administrative Database \n2. Print Customer Database.\n3. Exit:\n\nEnter choice:")
            if operation == "1":

                for key,value in self.administrative_database.items():

                    if key == "Password":
                        print(f"{key}: *****")
                    else:
                        print(f"{key}:{value}")

            elif operation == "2":
                
                for account, details in self.customer_database.items():

                    print(f"{account}:",end="{")
                            
                    for key,value in details.items():
                        
                        if key =="Password":                    # Replacing Password With "*****".
                            print(f"'{key}':***, ",end="")

                        else:
                            if key == list(details.keys())[-1]: # Access last key
                                print(f"'{key}': '{value}'", end="")
                            else:
                                print(f"'{key}': '{value}', ", end="")  
                    print("}")
                
            elif operation == "3":
                return
                
            else:
                logger.warning("Invalid Input! Try Again.")                
                
        return
