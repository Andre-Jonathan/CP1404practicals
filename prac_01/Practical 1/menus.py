"""
get name
display menu
get menu choice
while menu choice != "Q"
    if menu choice == "H"
        display "Hello" name
    else if menu choice == "G"
        display "Goodbye" name
    else
        display Invalid Choice
    display menu
    get menu choice
display "Finished".
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ").title()
print(MENU)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    print(MENU)
    menu_choice = input(">>> ").upper()
print("Finished.")
