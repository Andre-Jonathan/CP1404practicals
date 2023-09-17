from unreliable_car import UnreliableCar


def main():
    first_car = UnreliableCar("Prius 1", 100, 52)
    first_car.drive(15)
    print(first_car)

    second_car = UnreliableCar("Honda", 221, 12)
    second_car.drive(41)
    print(second_car)

    third_car = UnreliableCar("Toyota", 43, 96)
    third_car.drive(63)
    print(third_car)


main()
