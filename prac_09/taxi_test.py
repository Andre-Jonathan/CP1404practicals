from taxi import Taxi


def main():
    """Test taxi class to calculate my_taxi"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    print(my_taxi)
    my_taxi.drive(40)
    fare = my_taxi.get_fare()
    print(f"{my_taxi}, and the fair is ${fare} ")

    my_taxi.start_fare()

    my_taxi.drive(100)
    fare = my_taxi.get_fare()
    print(f"{my_taxi}, and the fair is ${fare} ")

main()
