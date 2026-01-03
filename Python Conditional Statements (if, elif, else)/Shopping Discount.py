amount = int(input("enter the amount:"))
if amount>=500:
    member = input("Are you a member?:")
    if member=="yes":
        print(f"20% discount,amount is ")
    else:
        print("10% discount")
else:
    print("No discount")
