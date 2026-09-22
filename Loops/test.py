# write a program to calculate the sum of digits in a given number
# eg input: 7123 ---? expected result :13
#             811--> expected result :10
n="7123"
res=0
for i in n:
    res+=int(i)
print(res)


a