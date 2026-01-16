#Input a 16-digit credit card number.
#Replace all except the last 4 digits with "*" →
s=input("enter the 16 digit card number")
a="*"*12+s[-4:]
print(a)