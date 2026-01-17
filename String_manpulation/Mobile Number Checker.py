#Input a mobile number as a string and check if it starts with '9' or '8'.
#If true → "Valid Indian Mobile Number", else "Invalid Number".
s=input("Enter the mobile number:")
if s[0]=="9" or s[0]=="8":
    print("valid Indian Mobile number")
else:
    print("invalid number")