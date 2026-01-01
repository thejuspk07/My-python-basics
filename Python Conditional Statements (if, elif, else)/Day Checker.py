num=int(input("Enter a number:"))
days={
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday"
}
if num in days:
    print(days[num])
else:
    print("invalid input")