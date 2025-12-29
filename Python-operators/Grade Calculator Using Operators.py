sub1 = float(input("enter the  mark of subject 1:"))
sub2 = float(input("enter the  mark of subject 2:"))
sub3 = float(input("enter the  mark of subject 3:"))
total = sub1+sub2+sub3
average = sub1+sub2+sub3/3
print("total marks of three subject:",total)
print("average marks of three subject:",average)
print("Grade A",average>=90)
print("Grade B",average>=80)
print("Grade C",average>=70)
print("FAIL",average<70)