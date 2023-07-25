file = "name.txt"
name = input("Enter your name: ")
out_file = open(file, "w")
print(f"Your name is {name}", file=out_file)
out_file.close()

in_file = open(file, "r")
text = in_file.read()
print(text)
in_file.close()

