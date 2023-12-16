def show_balance(balance):
    print("Your current balance is: $" + str(balance))

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return amount+balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("You do not have the sufficient funds to withdraw this amount of money\nPlease try again!")
    else: 
        balance -= amount
    return balance

def logout(name):
    print("Goodbye",name +'!')