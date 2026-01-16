#Input a name and favorite color.
#Create a coupon like:
#<FIRST3LETTERS_NAME><LAST3LETTERS_COLOR> in uppercase.
#> Example: "Arya", "purple" → "ARYPLE"

s= input("enter the name:")
c= input("enter the favorite color:")
p=len(s)
print(s[0:3].upper() +c[-4:].upper())