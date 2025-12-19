def deposit(balance, amount):
    balance += amount
    print(f"{amount} has been successfully deposited.")
    return balance


def withdraw(balance, amount):
    if amount > balance:
        print("Error: Insufficient funds!")
        return balance
    else:
        balance -= amount
        print(f"{amount} has been successfully withdrawn.")
        return balance


def check_balance(balance):
    print(f"Your current balance is: {balance}")
    return balance

balance = 1000.00

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        balance = deposit(balance, amount)
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        balance = withdraw(balance, amount)
    elif choice == "3":
        check_balance(balance)
    elif choice == "4":
        break
    else:
        print("Please choose a number between 1 and 4")
