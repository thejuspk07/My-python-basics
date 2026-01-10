#indexing..
s="python programming"
print(s[-1]) #backward
print(s[17]) #forward


#negitive index start at last
#positive index start at first


#positive--->0
#negative--->18
#g--->-1,17 #ing

print(len(s))

#slicing
print(s[0:6]) #positive
print(s[-18:-12]) #negative

print(s[7:10])
print(s[-3:])

print(s[16:18])

print(s[0:5:2]) # positive #pto #step value =2
print(s[-1:-4:-1])# gni

print(s[::-1])#right to left
print(s[::-2])

#method-->a particular datatype function
#-->lower
#-->upper
#-->capitalize
#-->split
#-->strip
#-->isupper()
#-->islower()
#-->isnumeric()
#-->startswit()
#-->endswith()
#-->count()

print(s.upper()) #uppercase
print(s.lower())#lowercase
print(s.capitalize())#first character (if alphabet) then first character become captial
print(s.title())
print(s.split()) #if space are available it split and makes list ['python', 'programming']
print(len(s.split()))
print((s.split()[1]))

#split
a="python,programming"
print(a.split())#['python,programming']
print(a.split(","))#['python', 'programming']
print(a.split("n"))#['pytho', ',programmi', 'g']


b="user@gmail.com"
print(b.split("@")[0])#dont need @gmail part

#strip
b="      user@gmail.co   m"
print(b.strip())


v="####user@gmail.com####"
print(v.strip("#")) #user@gmail.com

n=" ####user@gmail.com#### "
print(n.strip("#")) ####user@gmail.com####  because there is no # in starting space and ending space
print(n.strip("# "))#user@gmail.com
print(n.strip(" #u"))#ser@gmail.com


#isupper()
s="ABC"
print(s.isupper())

#islower()
print(s.islower())

#isnumeric()
print(s.isnumeric())

s="205a"
print(s.isupper())#False
print(s.islower())#True
print(s.isnumeric())#False

s="20.5"
print(s.isnumeric())#False

s="20  54"
print(s.isnumeric())#False

#startswith
print(s.startswith("python"))

#endswith
print(s.endswith("ing"))

#count
s="python programming"
print(s.count("p"))

#index
print(s.index("t"))

#replace
print(s.replace(" ","_"))

#list
list=['python','programming','language']
a="".join(list)
print(a)


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