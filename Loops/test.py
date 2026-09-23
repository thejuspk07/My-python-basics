#armstrong number
n="153"
arm=0
for i in n:
    arm+=int(i)**len(n)
print(arm)