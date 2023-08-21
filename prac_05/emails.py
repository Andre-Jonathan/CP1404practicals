"""
Emails
Estimate: 20 minutes
Actual:   40 minutes
"""
FIRST_INDEX = 0
SECOND_INDEX = 1


def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_verification = input(f"Is your name {name}? (Y/n)").title()
        if name_verification == "Y":
            emails[f"{name}"] = email
            email = input("Email: ")
        elif name_verification == "N":
            name = input("Name: ").title()
            emails[f"{name}"] = email
            email = input("Email: ")

    print("".join(f"{email} ({emails[email]})\n" for email in emails))


def get_name(email):
    names = email.split("@")
    del names[SECOND_INDEX]
    name = names[FIRST_INDEX].replace(".", " ").title()
    return name


main()
