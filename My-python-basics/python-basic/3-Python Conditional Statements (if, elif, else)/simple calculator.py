x = float(input("enter first number:"))
y = float(input("enter second number:"))
print("1.add \n2.subtract \n3.multiply \n4.division")
choice  = int(input("enter the operation (1-4):"))
if choice ==1:
    print("result = ",x+y)
elif choice ==2:
    print("result = ",x-y)
elif choice ==3:
    print("result = ",x*y)
elif choice ==4:
    if y!=0:
        print("result = ",x/y)
    else:
        print("Error,can't divide by zero")
else:
    print("invalid choice")


