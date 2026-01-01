#nested loop
age = int(input("Enter the age:"))
if age>=18:
    res=input("Did you passed driving test")
    if res=='yes'or 'YES':
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("Age not eligible")


#another one
n = int(input("Enter a number"))
if n>0:
    if n%2==0:
        print("positive even number")
    else:
        print("positive odd number")
elif n<0:
    if n%2==0:
        print("Negative even number")
    else:
        print("Negative odd number")
else:
    print("Zero")

#another
user="user1"
pwd="abc"
user_guess=input("Enter user name:")
password=input("Enter the password:")
if user_guess==user:
    if password==pwd:
        print("login successful")
    else:
        print("incorrect password")
else:
    print("incorrect username")

#another
marks = int(input("enter the marks"))
if marks>=40:
    if marks>=75:
        print("Distinction")
    else:
        print("pass")
else:
    print("fail")