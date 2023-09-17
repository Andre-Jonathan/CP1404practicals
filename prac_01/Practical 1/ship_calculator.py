"""
get item number

while item number <= 0
    display invalid input
    get item number
for i in range of item number
    get item price
    total += item price

if total price > 100
    subtrahend = total * 0.1
    final price = total price - subtrahend
else
    final price = total price
display item number, final total

"""

MINIMUM_ITEM = 0
MINIMUM_PRICE = 100
PERCENTAGE = 0.1
total_price = 0

item_number = int(input("Number of items: "))

while item_number <= MINIMUM_ITEM:
    print("Invalid Input")
    item_number = int(input("Number of items: "))
for i in range(item_number):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price >= MINIMUM_PRICE:
    subtracted_price = total_price * PERCENTAGE
    final_price = total_price - subtracted_price
else:
    final_price = total_price


print(f"Total price for {item_number} items is ${final_price:.2f}")
