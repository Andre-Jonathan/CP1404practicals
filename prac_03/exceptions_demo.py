"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 A ValueError will occur when the input is not the data type that is wanted.
2. When will a ZeroDivisionError occur?
 A ZeroDivisionError will occur when the calculation is dividing a numerator with zero
which has an undefined answer.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
 It is possible by using both "try except" and a while loop which
keeps on asking for a numerator and denominator value.
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        False
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")