from project import Project

MENU_CHOICE = """
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
"""
def main():
    print(MENU_CHOICE)
    user_pick = input(">>> ").title()
    while user_pick != "Q":
        if user_pick == "L":
            print("Load")
        elif user_pick == "S":
            print("Save")
        elif user_pick == "D":
            print("display")
        elif user_pick == "F":
            print("Filter")
        elif user_pick == "A":
            print("Add")
        elif user_pick == "U":
            print("Update")
        else:
            print("Invalid menu choice")
        print(MENU_CHOICE)
        user_pick = input(">>> ").title()

main()