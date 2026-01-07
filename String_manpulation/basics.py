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


print(s.upper()) #uppercase
print(s.lower())#lowercase
print(s.capitalize())#first character (if alphabet) then first character become captial
print(s.title())
print(s.split()) #if space are available it split and makes list ['python', 'programming']
print(len(s.split()))
print((s.split()[1]))

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

