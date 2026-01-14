#Input a word and count how many vowels are present using a loop.
word = input("Enter a word:")
c=0
for i in word:
    if i=="a"or i=="e" or i=="i" or i=="o"or i=="u":
        c+=1
print(c)