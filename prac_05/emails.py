"""
Emails
Estimate: 20 minutes
Actual:    minutes
"""
FIRST_INDEX = 0
SECOND_INDEX = 1
emails = {}
email = input("Email: ")
while email != "":
    names = email.split("@")
    del names[1]
    if "." in names[FIRST_INDEX]:
        name = names[FIRST_INDEX].replace(".", " ")
    else:
        name = names[FIRST_INDEX]
    name_verification = input(f"Is your name {name.title()}? (Y/n)").title()
    if name_verification == "Y":
        emails[f"{name.title()}"] = email
        email = input("Email: ")
    elif name_verification == "N":
        name = input("Name: ").title()
        emails[f"{name}"] = email
        email = input("Email: ")

