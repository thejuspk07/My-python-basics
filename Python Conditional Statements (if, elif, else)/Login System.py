usr="admin"
pwd="1234"
username= input("Enter your username:")
password= input("Enter your password:")
if username==usr:
    if password==pwd:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")
