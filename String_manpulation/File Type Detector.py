#Input a filename like "resume.pdf" or "data.csv".
#Check its type:
s=input("input filename:")
if s.endswith(".pdf"):
    print("PDF File")
elif s.endswith(".csv"):
    print("CSV File")
else:
    print("Unknown file type")