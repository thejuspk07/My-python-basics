#Input a name with random spaces and cases, e.g. "   mEera  naIR  ".
#Clean and format it as "Hello, Meera Nair!".
name =input("Input a name with random spaces:")
name=" ".join(name.strip().title().split())
print(f"Hello,{name}!")