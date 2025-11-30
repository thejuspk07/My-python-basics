num = int(input("Enter a Year:"))
if num%4:
    if num%100==0 and num%400==0:
        print("leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
