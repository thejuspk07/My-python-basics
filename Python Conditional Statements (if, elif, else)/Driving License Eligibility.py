age = int(input("enter the age:"))
if age>=18:
    test=input("have you passed test:")
    if test=="yes":
        print("Eligible for licence")
    else:
        print("Test not passed")
else:
    print("too young")