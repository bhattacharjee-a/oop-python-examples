# main.py

from banking import bank

if __name__ == "__main__":        # Opens A file, Wr2ites a label Called "main".

    try:

        #bank = Bank()                 # Creates object Like Built A House
        bank.Bank().greet()
        bank.Bank().welcome_menu()    # Gateway Of The House

    except Exception as e:

        if e:
            print(f"Error: {e}")
        elif not e:
            print("Unexpected error occurred. Please contact support.")

    finally:
        bank.Bank().farewell()
