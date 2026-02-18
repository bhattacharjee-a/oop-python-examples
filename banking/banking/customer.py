# Customer.py

import constants
import repository
from logging_config import logger
from account import Account
from transaction import Transaction

class Customer:

    def __init__(self, customer_database, account_no, name, phone, dob, balance):
        self.customer_info = customer_database
        self.account_no = account_no
        self.name = name
        self.phone = phone
        self.dob = dob

        self.trans = Transaction(account_no)
        self.account =  Account(customer_database,account_no)
        
    @staticmethod
    def main_menu():
    # CLI-driven flow controller (input + routing handled together intentionally)
       
        ans2="y"
        attempt   = 0
        login_failed = False


        while ans2=="y" and attempt <constants.MAX_ATTEMPTS:                     # Handling Wrong Attemps.
            
            attempt  += 1

            if login_failed == False:
               
                #reply = input("Are You An Existing Customer (Y/N):").lower()
                reply = input(
                        "1. Sign Up.\n"
                        "2. Login.\n"
                        "Choose an option:")



            if reply =="2" and login_failed == False:

                login_failed = Customer.verification()
                
                if login_failed == False:
                    return                 
                elif login_failed == True: 
                    continue
                else:
                    return
                
            elif reply =="1" or login_failed == True:                   # Handling New Customer For Creaing An Account.

                if login_failed == True:

                    ans1 = input("Do You Want to Create An Account (Y/N):").lower()
                        
                if reply =="1" or ans1 == "y":

                    name = input("Enter Your Name:").upper()
                    ph_number = input("Enter Your Phone Number (Without +91):")

                    try:
                        phone = int(ph_number)          
                    except ValueError:
                        logger.warning("Enter a valid number")
                        continue

                    password = input("Enter Password:")
                    dob = input("Enter Your D.O.B (DD/MM/YYYY):")
                    amount = input("Enter The opening Balance Ammout:").strip()

                    try:
                        balance = int(amount)          
                    except ValueError:
                        logger.warning("Enter a valid amount.")
                        continue
                    
                    try:
                        result = Account.account_open(name, phone, password, dob, balance)
                    except ValueError as e:
                        logger.warning(str(e))
                        continue

                    if result is None:
                        continue   # ask again
                    

                    acc_no, data = result

                    print(f"Account Number: {acc_no}")
                    print(data)

                    return
                
                elif ans1 =="n": 
                    return
                
                else:
                    logger.warning("Invalid input! Try Again.")

            else:
                logger.warning("Invalid input! Try Again.")
                        
            #attempt  += 1
            
        if attempt == constants.MAX_ATTEMPTS:
            logger.error("Too many failed attempts.")

        return
        
    @classmethod
    def verification(cls):
        
        customer_database=repository.load_customer_db()
        
        for attempt in range(constants.MAX_ATTEMPTS):
            account = input("Enter Account Number: ").strip()
            password = input("Enter Password: ").strip()

            if account not in customer_database:
                logger.warning("Invalid account number")
                continue

            if customer_database[account]["Password"] != password:
                logger.warning("Wrong password")
                continue

            # Loading Customer Details.
            Customer_info = customer_database[account]
            logger.debug("Database Loaded Successfully!")
            logger.info("Customer login Successful.")

            obj = cls(customer_database = customer_database, account_no=account, name=Customer_info["Name"], phone=Customer_info["Phone Number"], dob=Customer_info["D.O.B"], balance=Customer_info["Balance"])
            obj.account_handling()
            return 
            
        return True


    def account_handling(self):
            
        for attempt in range(constants.MAX_ATTEMPTS):                   
                
            operation=input("Choose operation:\n1. Balance & Transaction.\n2. Account Management\n3. Exit:\n\nEnter choice:")
                    
            if operation == "1":
                self.transaction()
                return
            elif operation == "2":
                self.account_management()
                return
            elif operation == "3":
                return
                    
            else:
                logger.warning("Invalid Input! Try again.")
                    
        return

    def transaction(self):
        
        for attempt in range(constants.MAX_ATTEMPTS):
            
            operation=input("Choose operation:\n1. Balance \n2. Deposit\n3. Withdraw\n4. Exit:\n\nEnter choice:")

            if operation == "1":

                print(f"Current Balance: {self.trans.get_balance()}")

            elif operation == "2":

                value = input("Enter deposit amount: ").strip()

                try:
                    amount = int(value)          
                except ValueError:
                    logger.warning("Amount must be a valid number")
                    continue
                
                try:
                    new_balance = self.trans.deposit(amount)
                    logger.info("Deposit successful!")
                    print(f"Deposit successful!\nDeposit: {amount}, New balance: {new_balance}")
                except ValueError as e:
                    logger.warning(str(e))
                    continue

            elif operation == "3":

                value = input("Enter deposit amount: ").strip()

                try:
                    amount = int(value)         
                except ValueError:
                    logger.warning("Amount must be a valid number")
                    continue
                
                try:
                    new_balance = self.trans.withdraw(int(amount))
                    logger.info("Withdrawal successful!")
                    print(f"Withdrawal successful!\nWithdrawal: {amount}, New balance: {new_balance}")
                except ValueError as e:
                    logger.warning(str(e))   

            elif operation == "4":
                return
                
            else:
                logger.warning("Invalid Input! Try again.")

        return

    def account_management(self):
        
        for attempt in range(constants.MAX_ATTEMPTS):
                
            operation=input("Choose operation:\n1. Check Account Details.\n2. Update Account Details & Password.\n3. Delete Account\n4. Exit:\n\nEnter choice:")

            if operation == "1":   
                print(f"Account Number : {self.account_no}\nName : {self.name}\nPhone Number : {self.phone}\nD.O.B: {self.dob}\nBalance : {self.trans.get_balance()}")
            elif operation == "2":       
                self.account_update()
                return
            elif operation == "3":
                self.account_delete()
                return
            elif operation == "4":
                return
            else:
                logger.warning("Invalid Input! Try Again.")
                    
        return
    
    def account_update(self):
        
        for attempt in range(constants.MAX_ATTEMPTS):
            
            choice = input("Choose operation:\n1. Update Details.\n2. Update password\n3. Exit:\n\nEnter choice:")
            if choice =="1":
                
                db = repository.load_customer_db()
                self.name = input("Enter Full Name:").upper()
                self.dob = input("Enter Your D.O.B (DD/MM/YYYY):")
                ph_number = input("Enter Old/New Phone Number (Without +91):")

                try:
                    self.phone = int(ph_number)          
                except ValueError:
                    logger.warning("Enter a valid number")
                    continue
                
                try:
                    updated_db = self.account.update_account(self.name,self.dob,self.phone)
                    print(f"Account Number: {self.account_no}\n{str(updated_db[self.account_no])[1:-1]}")
                except ValueError as e:
                    print(str(e))
                    continue

                repository.update_customer(
                            self.account_no,
                            {
                                "Name": self.name,
                                "Phone Number": self.phone,
                                "D.O.B": self.dob
                            }
                        )
                
            elif choice =="2":

                db = repository.load_customer_db()
                old_pass = input("Enter Current Password:")
                phone = input("Enter Your Phone Number:")
                new_pass = input("Enter new Password:")
                  
                try:
                    new_pass = self.account.password_update(old_pass, phone, new_pass)
                except ValueError as e:
                    print(str(e))
                    continue

                db[self.account_no]["Password"] = new_pass
                repository.save_customer_db(db)
                logger.info("Password Updated Successfully!")
                
            elif choice =="3":
                return
            else:
                logger.warning("Invalid Input! Try Again.")
        
        return
    
    def account_delete(self):

        for attempt in range(constants.MAX_ATTEMPTS):
            
            db = repository.load_customer_db()
            acc_list = repository.load_account_numbers()
            phone = input("Enter Phone Number:")      
            password = input("Enter Current Password:")

            try:
                Updated_db = self.account.account_deletion(phone,password)    
            except ValueError as e:
                logger.warning(str(e))
                continue

            # Removing Account Number From Existing Account Number List.
            acc_list.remove(int(self.account_no))
            repository.save_account_numbers(acc_list)

            # Removing Customer Details From Database.
            repository.delete_customer(self.account_no)
            
            logger.info("Account Deleted Successfully.")
            return                        
        
        return