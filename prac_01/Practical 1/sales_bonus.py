"""
Program to calculate and display a user's bonus based on the sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode:
get sales
while sales is not 0
    if sales >= 1000
        total = sales * 15/100
        display total
    else
        total = sales * 10/100
        display total
    get sales


"""
MINIMUM = 0
SALES_POINT = 1000
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.15

sales = float(input("Enter sales: $"))
while sales > MINIMUM:
    if sales >= SALES_POINT:
        total = sales * MAXIMUM_DISCOUNT
    else:
        total = sales * MINIMUM_DISCOUNT
    print(f"The value is ${int(total)}.")
    sales = float(input("Enter sales: $"))
