l=[]
num=7
for i in range(2,num):
    for i in range(2,num//2):
        if num%i==0:
            l.append(num)
            break
print(l)

