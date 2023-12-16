from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")

# Registration loop for a valid name
while True:
    name = input("Enter name to register: ")

    # Check if the name length is between 1 and 10 characters
    if 1 <= len(name) <= 10:
        break  # Break out of the loop if the name is valid
    else:
        print("Invalid name! Please enter a name with a length between 1 and 10 characters.")

# Registration loop for a valid PIN
while True:
    pin = input("Enter PIN (4 digits): ")

    # Check if the PIN is a 4-digit number
    if pin.isdigit() and len(pin) == 4:
        break  # Break out of the loop if the PIN is valid
    else:
        print("Invalid PIN! Please enter a 4-digit number.")

# Continue with the rest of the registration process
balance = 0
print(name, 'has been registered with a starting balance of $' + str(balance))

print("          === Automated Teller Machine ===          ")
print("LOGIN")

while True:
    name_to_validate = input("Enter your name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
