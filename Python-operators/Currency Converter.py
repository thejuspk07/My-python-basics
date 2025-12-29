#Input an amount in INR. Convert it to USD (assume 1 USD = 83 INR). Print both values.
amount = int(input("Enter the amount"))
USD= amount/83
print(f"{amount} INR = {USD} USD")