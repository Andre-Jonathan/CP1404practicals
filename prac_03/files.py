NAME_FILE = "name.txt"
name = input("Enter your name: ").title()
out_file = open(NAME_FILE, "w")
print(f"Your name is {name}", file=out_file)
out_file.close()

in_file = open(NAME_FILE, "r")
text = in_file.read().strip()
print(text)
in_file.close()


in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
out_file = open("numbers.txt", "a")
total = str(total)
out_file.write(total)
out_file.close()
