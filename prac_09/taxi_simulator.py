from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_OPTION = (""
               "q)uit, "
               "c)hoose taxi, "
               "d)rive")


def main():
    print("Let's drive!")
    print(MENU_OPTION)
    user_pick = input(">>> ").lower()
    while user_pick != "q":
        if user_pick == "c":
            print("chose")
        elif user_pick == "d":
            print("drive")
        else:
            print("Invalid menu choice")
        print(MENU_OPTION)
        user_pick = input(">>> ").title()


main()
