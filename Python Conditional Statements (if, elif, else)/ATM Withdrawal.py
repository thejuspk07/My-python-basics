PIN="8726"
user_guess=input("Enter your PIN:")
if user_guess==PIN:
    amount=int(input("enter the withdrawal amount:"))
    if amount<=10000:
        print("withdrawal successful")
    else:
        print("limit reached")
else:
    print("Invalid pin")