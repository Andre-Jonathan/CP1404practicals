NAME_FILE = "name.txt"
name = input("Enter your name: ")
out_file = open(NAME_FILE, "w")
print(f"Your name is {name}", file=out_file)
out_file.close()

in_file = open(NAME_FILE, "r")
text = in_file.read()
print(text)
in_file.close()

NUMBER_FILE = "numbers.txt"
numbers = [17, 42, 400]
in_file = open(NUMBER_FILE, "w")
for number in numbers:
    print(number, file=in_file)
in_file.close()
