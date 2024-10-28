balance_amount=1000
while True:
    print("\"1.\tcheck balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice ==1:
        print(f"The current balance ${balance_amount}")
    elif choice ==2:
        deposit_amount = float(input("Enter the amount"))
        balance_amount = balance_amount + deposit_amount
        print(f"The deposited amount${deposit_amount}"and f"the current balance ${balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("Enter the amount to withdraw"))
        if withdraw_amount>balance_amount:
            print("Insufficient balance")
        else:
            balance_amount = balance_amount-withdraw_amount
            print(f"The amount withdrawn from the account"f"${withdraw_amount} the balance amount"f"${balance_amount}")
    elif choice ==4:
        break
    else:
        print("Invalid Entry")