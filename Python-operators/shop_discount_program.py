price = float(input("enter the price:"))
discount = float(input("enter the discount percentage:"))
discounted_price = price*(discount/100)
final_price = price - discounted_price
print("final price:",final_price)