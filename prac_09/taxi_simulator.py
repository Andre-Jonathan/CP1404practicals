from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_OPTION = (""
               "q)uit, "
               "c)hoose taxi, "
               "d)rive")
MINIMUM_INDEX = 0
MAXIMUM_INDEX = 3


def main():
    """User will choose a taxi and get fare based on the distance"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = ""
    final_bill = 0
    print("Let's drive!")
    print(MENU_OPTION)
    user_pick = input(">>> ").lower()
    while user_pick != "q":
        if user_pick == "c":
            print("Taxis available:")
            list_taxis(taxis)
            user_taxi = int(input("Choose taxi: "))
            if MAXIMUM_INDEX > user_taxi >= MINIMUM_INDEX:
                chosen_taxi = taxis[user_taxi]
            else:
                print("Invalid taxi choice")

        elif user_pick == "d":
            if chosen_taxi != "":
                drive_distance = int(input("Drive how far? "))
                chosen_taxi.start_fare()
                chosen_taxi.drive(drive_distance)
                total_bill = chosen_taxi.get_fare()
                final_bill += total_bill
                print(f"Your {chosen_taxi.name} trip cost you ${round(total_bill, 3)}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid menu choice")
        print(f"Bill to date: ${final_bill:.2f}")
        print(MENU_OPTION)
        user_pick = input(">>> ").lower()
    print(f"Total trip cost: ${final_bill:.2f}")
    list_taxis(taxis)


def list_taxis(taxis):
    """Lists all the taxi available in taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
