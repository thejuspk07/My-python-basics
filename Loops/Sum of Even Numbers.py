#Find the sum of even numbers between 1 and 50.
sum=0
for i in range(1,51):
    if i%2==0:
        sum=sum+i
print(sum)
