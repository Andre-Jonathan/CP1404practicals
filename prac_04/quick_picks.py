import random
number_of_line = int(input("How many quick picks? "))
for i in range(number_of_line):
    for j in range(6):
        random_number = random.randint(1, 45)
        print(f"{random_number:3}", end=" ")
    print()
