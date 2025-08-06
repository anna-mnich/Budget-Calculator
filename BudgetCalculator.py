# This function asks user input regarding income
def get_income():
    
    # Validating user input
    while True:
        try:
            # Code that might raise an exception
            income = float(input("Enter your monthly INCOME: " + "$"))
            # Code to execute if the condition is true
            if income > 0:
                return income
            # Code to execute if the condition is false
            else:
                print("Income cannot be negative or zero. Please enter a valid amount.")
        # Code to handle the exception
        except ValueError:
            print("Invalid input. Please enter a numerical value for INCOME.")
    
   
# This function asks user input regarding rent cost
def get_rent():
    
    # Validating user input
    while True:
        try:
            # Code that might raise an exception
            rent = float(input("Enter your monthly RENT cost: " + "$"))
            # Code to execute if the condition is true
            if rent >= 0:
                return rent
            # Code to execute if the condition is false
            else:
                print("Amount cannot be negative. Please enter a valid amount.")
        # Code to handle the exception
        except ValueError:
            print("Invalid input. Please enter a numerical value for RENT.")


# This function asks user input regarding food cost            
def get_food():
    
    # Validating user input
    while True:
        try:
            # Code that might raise an exception
            food = float(input("Enter your monthly FOOD cost: " + "$"))
            # Code to execute if the condition is true
            if food >= 0:
                return food
            # Code to execute if the condition is false
            else:
                print("Amount cannot be negative. Please enter a valid amount.")
        # Code to handle the exception
        except ValueError:
            print("Invalid input. Please enter a numerical value for FOOD.")        
                    

# This function asks user input regarding internet cost
def get_internet():
    
    while True:
        try:
            # Code that might raise an exception
            internet = float(input("Enter your monthly INTERNET cost: " + "$"))
            # Code to execute if the condition is true
            if internet >= 0:
                return internet
            # Code to execute if the condition is false
            else:
                print("Amount cannot be negative. Please enter a valid amount.")
        # Code to handle the exception
        except ValueError:
            print("Invalid input. Please enter a numerical value for INTERNET.")
    
    
# This function calculates remaining balance
def calculate_balance(income, rent, food, internet):
    remaining_balance = income - rent - food - internet
    return remaining_balance
    

# This function will display the results of remaining balance
# and print the results
def display_results(remaining_balance):
    print(f"REMAINING BALANCE is: ${remaining_balance:.2f}")
    

# The main function will call the other functions 
# when program is being executed
def main():
    income = get_income()
    rent = get_rent()
    food = get_food()
    internet = get_internet()
    remaining_balance = calculate_balance(income, rent, food, internet)
    display_results(remaining_balance)

# This conditional statement checks if the script is run directly 
# and not when imported as a module in another script
if __name__ == "__main__":
    main()
