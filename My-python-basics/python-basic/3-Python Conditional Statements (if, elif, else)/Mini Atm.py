balance = int(input("Enter your balance:"))

print("1.Check balance\n2.Withdraw\n3.Deposit\n4.Exit")

choice = int(input("select your choice:"))
if choice==1:
    print(+balance,"is your balance")
elif choice==2:
    withdraw_balance = int(input("enter the amount to withdraw:"))
    if withdraw_balance<=balance:
        print(+withdraw_balance,"withdrawed  successfully")
        balance = balance-withdraw_balance
    else:
        print("insufficient balance")

elif choice==3:
    deposit = int(input("enter the amount to deposit:"))
    balance = balance+deposit
    print(+balance, "amount successfully deposited")

else:
    print("exited successfully")
