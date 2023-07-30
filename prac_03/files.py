NAME_FILE = "name.txt"
name = input("Enter your name: ").title()
out_file = open(NAME_FILE, "w")
print(f"Your name is {name}", file=out_file)
out_file.close()

in_file = open(NAME_FILE, "r")
text = in_file.read().strip()
print(text)
in_file.close()

NUMBER_FILE = "numbers.txt"
numbers = [17, 42, 400]
out_file = open(NUMBER_FILE, "w")
for number in numbers:
    print(number, file=out_file)
out_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

