#Input a letter from the user and print all fruits that end with that letter using endswith().
l=input("enter the letter:")
words = ["apple", "pineapple", "kiwi", "strawberry", "fig"]
for i in words:
    if i.endswith(l):
        print(i)


        #5