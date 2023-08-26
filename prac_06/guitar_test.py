from guitar import Guitar


def main():
    """Demo test code to show how to use car class."""
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson_guitar.get_age())
    print(gibson_guitar.is_vintage())

    another_guitar = Guitar("Another Guitar", 2013, 1512.9)
    print(another_guitar.get_age())
    print(another_guitar.is_vintage())


main()
