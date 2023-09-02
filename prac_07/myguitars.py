from guitar import Guitar
import csv
FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    """Code to put the information from csv file to guitars list"""
    guitars = []
    with open(FILENAME, "r") as in_file:
        read = csv.reader(in_file)
        for row in read:
            new_guitar = Guitar(row[NAME_INDEX], int(row[YEAR_INDEX]), float(row[COST_INDEX]))
            guitars.append(new_guitar)
            print(new_guitar)
    guitars.sort()

    new_name = input("Enter a new guitar name:")
    while new_name != "":
        new_year = int(input("Enter its year: "))
        new_cost = float(input("Enter the cost: $"))
        new_guitar = Guitar(new_name, new_year, new_cost)
        guitars.append(new_guitar)
        new_name = input("Enter a new guitar name:")
    guitars.sort()
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            statement = [guitar.name, str(guitar.year), str(guitar.cost)]
            print(",".join(str(element) for element in statement), file=out_file)



main()
