# Welcome to banking system

# import the random module for generate the random 10 char number for account number
import random 
amount = 0
ac_no = []  
pin = []

def implement_numbers():
    for account_number in range(111111111, 999999999):
        if account_number not in ac_no:
            return account_number
    return None
def Signin():
    
    user_ac_no = implement_numbers()
    if user_ac_no is not None:
        print(f"Your account number is {user_ac_no}")
        user_pin = input("Enter your PIN: ")
        
        if (len(user_pin) == 4 or len(user_pin) == 6) and user_pin.isdigit():
            ac_no.append(user_ac_no)
            pin.append(user_pin)
            print("########## Your account is successfully created! ##########")
            return user_ac_no, user_pin
        else:
            print("INVALID: Only four and six-digit PINs are accepted.")
    else:
        print("No available account numbers. Please try again later.")
    
    return None, None
        
    

def login(user_ac_no_input,user_pin_input):
            if user_ac_no_input in ac_no and pin[ac_no.index(user_ac_no_input)] == user_pin_input:
                print("account are login successfully!")
                while True:
                    print("1.Deposit money")
                    print("2.Withdraw money")
                    print("3.Check Balance")
                    print("4.Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        deposit()
                    elif choice == 2:
                        Withdraw()
                    elif choice == 3:
                        show_balance()
                    elif choice == 4:
                        print("Thanks!")
                        break
                    else:
                        print("Invalid Choice!")
            else:
                print("INVALID: Incorrect account number or PIN. Please try again.")

def deposit():
    global amount
    deposit_amount = int(input("Enter money you want to add: "))
    if deposit_amount > 0:
        amount += deposit_amount
        print(f"{deposit_amount} is successfully deposited. Total Balance is {amount}")
    else:
        print("INVALID: Invalid amount!")
        
def Withdraw():
    global amount
    withdraw_amount = int(input("Enter amount you want to withdraw: "))
    if 0 < withdraw_amount <= amount:
        amount -= withdraw_amount
        print(f"{withdraw_amount} is successfully withdraw.Total Balance is {amount}")
    else:
        print("INVALID: invalid amount")
    
def show_balance():
    print(f"the available balance is {amount}")


while True:
    print("********** Welcome To ATM **********")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_ac_no, user_pin = Signin()
    elif choice == 2:
        user_ac_no_input = int(input("Enter your account no: "))
        user_pin_no_input = input("Enter your PIN: ")
        login(user_ac_no_input,user_pin_no_input)
    elif choice == 3:
        print("Thanks!")
        break
    else:
        print("Invalid Choice")
        
        
        
        
        