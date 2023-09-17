import random
MINIMUM_LINE = 0
RANDOM_AMOUNT = 6
MINIMUM_RANDOM = 1
MAXIMUM_RANDOM = 45
numbers = []
number_of_line = int(input("How many quick picks? "))
while number_of_line <= MINIMUM_LINE:
    print("Invalid Input")
    number_of_line = int(input("How many quick picks? "))

for i in range(number_of_line):
    for j in range(RANDOM_AMOUNT):
        random_number = random.randint(MINIMUM_RANDOM, MAXIMUM_RANDOM)
        while random_number in numbers:
            random_number = random.randint(MINIMUM_RANDOM, MAXIMUM_RANDOM)
        numbers.append(random_number)
    numbers.sort()
    print(" ".join(f"{number:3}" for number in numbers))
    numbers.clear()

