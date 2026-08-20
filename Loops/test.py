companies=["Indian oil","state bank of india","tata motors"]
for i in companies:
    s=""
    for j in i.split():
        if len(j)>2:
            s+=j[0].upper()
    print(s)