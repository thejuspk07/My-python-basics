#write a program to find factorial of number
n=int(input("enter the factorial u want:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# write a program to calculate the sum of digits of a given number
#eg input:7123 ---> Expected result:13
#iterable things --> strings,list,range
#integer float not iterable

s = int(input("enter the number:"))
res = 0
for i in str(s):
    res+=int(i)
print(res)

#armstrong number
a=153
r=0
for i in str(a):
    r+=int(i)**3
if r==a:
    print(f"{r} is a armstrong number")
else:
    print(f"{r} is not armstrong number")



