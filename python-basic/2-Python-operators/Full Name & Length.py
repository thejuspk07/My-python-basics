#Input your first and last name. Print them together using sep=" " and also print how many characters the full name has (use + operator for string concatenation).
fname=input("enter the first name:")
lname=input("enter the second name:")
print(fname,lname,sep="")

flength = len(fname)
llength= len(lname)
print("fullname length=",flength+llength)