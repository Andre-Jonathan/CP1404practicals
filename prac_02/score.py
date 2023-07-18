def main():
    score = float(input("Enter score: "))
    if 0 > score > 100:
        print("Invalid Input")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

