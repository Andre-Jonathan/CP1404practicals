"""
Emails
Estimate: 20 minutes
Actual:    minutes
"""

emails = {}
email = input("Email: ")
while email != "":
    names = email.split("@")
    print(names)
    if "." in names[0]:
        name = names[0].replace(".", " ")
    name_verification = input(f"Is your name {name.title()}? (Y/n)").title()
    if name_verification == "Y":
        emails[f"{name.title()}"] = names[1]
        print(emails)
        email = input("Email: ")
    elif name_verification == "N":
        name = input("Name: ")
        emails[f"{name.title()}"] = names[1]
        print(emails)
        email = input("Email: ")
