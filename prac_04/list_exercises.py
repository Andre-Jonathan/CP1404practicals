def basic_list_operation():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {int(sum(numbers)) / len(numbers)}")


def security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = str(input("Enter your username: "))
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


basic_list_operation()
security_checker()
