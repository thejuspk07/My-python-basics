s="python programming"
c=0;
for i in s:
    print("hello")
print("end")

for i in s:
    print(i)

#count using loop
for i in s: #i="p"
    if i=="p":
        c+=1
print(c)


#list capitalize
s=["python", "programming"]
for i in s:
    print(i.capitalize(),end = " ")
    print(i,len(i))

for i in range(1,101):
    print(i,end=" ")

for i in range(100,0,-1):
    print(i)



#range

range(start,end,step)


n = int(input("Enter the multiplication table you want"))
for i in range(1,11):
    print(f" {i} X {n}= {i*n}")


#natural number sum
sum=0
for i in range(1,152):
    sum+=i
print(sum)


m=0
for i in range(1,151):
    if i%2==0:
        m+=i
print(m)


for  i in range(1,152):
    if i%3==0 and i%7==0:
        print(i)

s="hello"
new=""
for i in s:
    new=i+new
print(new)



s="cat"
for i in s:
    print(s.index(i),i)


