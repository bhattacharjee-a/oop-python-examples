# Bank.py

import admin 
from logging_config import logger
import customer
import constants

class Bank:

    @staticmethod
    def greet():
        print("*********************************************************")
        print("**************** Welcome To Python Bank *****************")
        print("*********************************************************")


    def welcome_menu (self):

        attempt = 0
        while attempt<constants.MAX_ATTEMPTS:
            ans = input ("Choose An Option.\n1. Administrative Login. \n2. Customer Login. \n3. Exit:\n\nEnter choice:")
                
            if ans == "1":
                admin.Admin.verification()
                return            
            elif ans == "2":
                customer.Customer.main_menu()
                return
            elif ans == "3":
                break
            else: 
                logger.warning("Invalid Input! Try again.\n")

            attempt += 1
        return

    @staticmethod
    def farewell():
        
        print("*******************************************************")
        print("*********** Thank You For Using Python Bank ***********")
        print("*******************************************************")
