#Input a name with random spaces and cases, e.g. "   mEera  naIR  ".
#Clean and format it as "Hello, Meera Nair!".
s=input("Enter a name with random spaces and cases:")
word="" .join(s.strip()).title()
print(f"Hello,{word}")