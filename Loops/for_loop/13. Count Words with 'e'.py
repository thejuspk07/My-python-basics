# 13. Count Words with 'e'
#
# From:
#
# words = ["apple", "banana", "mango", "cherry"]
#
# Count how many words contain "e".
words = ["apple", "banana", "mango", "cherry"]
c=0
for i in words:
    if 'e' in i:
        print(i)
        c+=1
print(c)