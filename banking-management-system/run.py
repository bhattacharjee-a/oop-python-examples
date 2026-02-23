from banking import bank

if __name__ == "__main__":
    try:
        bank.Bank().greet()
        bank.Bank().welcome_menu()
    
    except ValueError as e:
        print(f"Error: {e}")
        
    finally:
        bank.Bank().farewell()