#Input a name and year of joining.
#Generate a college ID → replace spaces in the name with _, convert to lowercase, and add the year.
name=input("enter the name:")
year=int(input("enter the year of joining:"))
college_id=name.replace(" ","_").lower()+str(year)
print(college_id+"@gmail.com")