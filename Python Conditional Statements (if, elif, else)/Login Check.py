#Input a username and password. If both match some predefined values, print "Login Successful", else "Login Failed".
usr="user1"
pwd="abc123"
user_guess=str(input("enter the username:"))
password=str(input("enter the password:"))
if user_guess==usr:
    if pwd==password:
        print("Login successful")
    else:
        print("incorrect password")
else:
    print("incorrect username")