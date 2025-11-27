principal = float(input("Enter the principle:"))
rate  = float(input("enter the reate of interest:"))
time = float(input("enter the time in years:"))

si = principal*rate*time/100
print("Simple interest=",si)

amount=principal*(1+rate/100)**time
ci=amount-principal
print("compound interest=",ci)
