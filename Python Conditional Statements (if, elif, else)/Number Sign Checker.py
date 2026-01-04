num=int(input("Enter a number:"))
if num>0:
    even=num%2==0
    odd=num%2!=0
    if even:
        print("positive even")
    elif odd:
        print("positive odd")
else:
    print("not positive")