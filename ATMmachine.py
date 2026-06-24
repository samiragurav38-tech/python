accountinfo = {
    "Name": "samira",
    "Account_No": "1234567890",
    "Available_Balance": 20000,
    "PIN": 1234
}

print("------WELCOME TO ATM------")

entered_pin = int(input("Enter PIN: "))

if entered_pin != accountinfo["PIN"]:
    print("Invalid PIN")
    exit()
else:
    print("Login Successful\n")

while True:
    print("\n1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Change PIN")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance: Rs", accountinfo["Available_Balance"])

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: Rs "))

        if amount > accountinfo["Available_Balance"]:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            accountinfo["Available_Balance"] -= amount
            print(f"Rs {amount} withdrawn successfully")
            print("Updated Balance: Rs", accountinfo["Available_Balance"])

    elif choice == 3:
        amount = int(input("Enter amount to deposit: Rs "))

        if amount <= 0:
            print("Invalid amount")
        else:
            accountinfo["Available_Balance"] += amount
            print(f"Rs {amount} deposited successfully")
            print("Updated Balance: Rs", accountinfo["Available_Balance"])

    elif choice == 4:
        current_pin = int(input("Enter Current PIN: "))

        if current_pin == accountinfo["PIN"]:
            new_pin = int(input("Enter New PIN: "))
            accountinfo["PIN"] = new_pin
            print("PIN changed successfully")
        else:
            print("Incorrect current PIN")

    elif choice == 5:
        print("\n----- Account Details -----")
        print("Name:", accountinfo["Name"])
        print("Account Number:", accountinfo["Account_No"])
        print("Account Balance:", accountinfo["Available_Balance"])
        print("---------------------------")

    elif choice == 6:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid option. Please select 1-6.")