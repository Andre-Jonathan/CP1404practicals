"""
CP1404/CP5632 Practical
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_month = int(input("How many months? "))

    for month in range(1, number_of_month + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes, number_of_month)


def print_report(incomes, number_of_month):
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
