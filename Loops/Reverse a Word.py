#Input a string and print its reverse using a for loop (no slicing).
s=input("enter a string:")
r=""
for i in s:
    r=i+r
print(r)