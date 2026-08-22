#armstrong number
n=int(input("enter the number:"))
l=len(str(n))
arm=0
for i in str(n):
    arm+=int(i)**l
if arm==n:
    print(f"{arm} is armstrong number")
else:
    print(f"{arm} is not armstrong number")