from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_OPTION = (""
               "q)uit, "
               "c)hoose taxi, "
               "d)rive")
MINIMUM_INDEX = 0
MAXIMUM_INDEX = 3


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = ""
    total_bill = 0
    print("Let's drive!")
    print(MENU_OPTION)
    user_pick = input(">>> ").lower()
    while user_pick != "q":
        if user_pick == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            user_taxi = int(input("Choose taxi: "))
            if MAXIMUM_INDEX >= user_taxi > MINIMUM_INDEX:
                chosen_taxi = taxis[user_taxi]
                print(chosen_taxi)
            else:
                print("Invalid taxi choice")
            print(f"Bill to date: ${total_bill}")

        elif user_pick == "d":
            print("drive")
        else:
            print("Invalid menu choice")
        print(MENU_OPTION)
        user_pick = input(">>> ").lower()


main()
