#Input day, month, and year separately. Print in this format:
day = int(input("Enter the day:"))
month = int(input("Enter the month"))
year = int(input("Enter the year:"))
print(day,month,year,sep="/")#seperation method
print(f"{day:02d}/{month:02d}/{year}")#best method