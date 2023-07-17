PASSWORD = "Pythonista"
MINIMUM_LENGTH = 0

def main():
    password_attempt = get_valid_password()
    while password_attempt != PASSWORD:
        if password_attempt > PASSWORD:
            asterisks = "*" * len(password_attempt)
            print(asterisks)
            print("Incorrect Password")
            password_attempt = get_valid_password()
    print("Access Granted")

def get_valid_password():
    password_attempt = input("Enter the Password: ")
    while len(password_attempt) == MINIMUM_LENGTH:
        print("Invalid Input")
        password_attempt = input("Enter the Password: ")
    return password_attempt

main()
