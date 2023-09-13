from silver_service_taxi import SilverServiceTaxi


def main():
    first_car = SilverServiceTaxi("Hummer", 200, 4)
    first_car.drive(15)
    print(f"{first_car}, current price: ${first_car.get_fare()}")

    second_car = SilverServiceTaxi("Toyota", 124, 32)
    second_car.drive(53)
    print(f"{second_car}, current price: ${second_car.get_fare()}")

    third_car = SilverServiceTaxi("Honda", 532, 52)
    third_car.drive(32)
    print(f"{third_car}, current price: ${third_car.get_fare()}")


main()
