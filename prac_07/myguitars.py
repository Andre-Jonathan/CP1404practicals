from guitar import Guitar
import csv

NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    """Code to put the information from csv file to guitars list"""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        read = csv.reader(in_file)
        for row in read:
            new_guitar = Guitar(row[NAME_INDEX], int(row[YEAR_INDEX]), float(row[COST_INDEX]))
            guitars.append(new_guitar)
            print(new_guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
