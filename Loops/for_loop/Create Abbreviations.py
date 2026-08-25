# For:
#
# companies = ["Indian Oil", "State Bank of India", "Tata Motors"]
#
# Print abbreviations like:
#
# IO, SBI, TM

companies = ["Indian Oil", "State Bank of India", "Tata Motors"]
for i in companies:
    s=""
    for j in i.split():
        if len(j)>2:
            s+=j[0].upper()
    print(s)

