#Input three numbers from the user. Print them separated by |.
a = input("Enter first  number")
b = input("Enter second number")
c = input("Enter third  number")
print(a,b,c,sep = "|")

#another method
a,b,c=input("enter 3  with spaces numbers").split()
print(a,b,c,sep ="|")