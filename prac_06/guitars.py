from prac_06.guitar import Guitar


def main():
    INCREMENT = 1
    count = 1
    counter = 0

    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        adding_guitar = Guitar(name, year, cost)
        guitars.append(adding_guitar)
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"

        print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
        print()
        count += INCREMENT
        counter += INCREMENT
    else:
        print("No guitars available")


main()