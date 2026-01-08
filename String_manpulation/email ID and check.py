#Input an email ID and check if it ends with "@gmail.com".
#If yes → print "Valid Gmail address", else "Invalid email type".
email = input("enter email ID:")
if email.split("@")[-1] == "gmail.com":
    print("Valid gmail address")
else:
    print("Invalid email address")