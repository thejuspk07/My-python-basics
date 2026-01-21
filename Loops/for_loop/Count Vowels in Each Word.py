#For each word in:
#words = ["apple", "orange", "grape"]
#Count the vowels using a for loop and print:
#> apple → 2
#orange → 3
#grape → 2
words = ["apple", "orange", "grape"]
vowels="aeiou"
count=0
for i in words:
    for letter in i:
        if letter in vowels:
            count+=1
    print(i,count)
