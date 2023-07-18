"""
import determine score function from score.py
function main
    score = ""
    display menu
    get choice
    while choice != "Q"
        if choice == "G"
            score = get valid score()
            get choice
        else if choice == "P"
            if score == ""
                display no score
            else
                score_feedback = determine score(score)
                display score feedback
            get choice
        else if choice == "S"
            if score == ""
                display no score
            else
                stars = "*" * score
                display stars
            get choice
        else
            display invalid choice
            get choice
    display farewell

function get valid score()
    get score
    while score < 0 and score > 100
        display invalid score
        get score
    return score

function determine score()
    if score < 0 or score > 100:
        score message = "Invalid Input"
    else if score >= HIGH_SCORE:
        score message = "Excellent"
    else if score >= PASS_SCORE:
        score message = "Passable"
    else:
        score message = "Bad"
    return score message

"""

MENU = '(G)et a valid score (must be 0-100 inclusive)\n' \
       '(P)rint result (copy or import your function to determine the result from score.py)\n' \
       '(S)how stars (this should print as many stars as the score)\n' \
       '(Q)uit'
MAXIMUM_SCORE = 100
HIGH_SCORE = 90
PASS_SCORE = 50
MINIMUM_SCORE = 0

def main():
    score = ""
    print(MENU)
    choice = input("Input your choice = ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Score = {score}")
            print(MENU)
            choice = input("Input your choice = ").upper()
        elif choice == "P":
            if score == "":
                print("You have not added a score to give result ")
                print()
            else:
                score_feedback = determine_score(score)
                print(score_feedback)
            print(MENU)
            choice = input("Input your choice = ").upper()
        elif choice == "S":
            if score == "":
                print("You have not added a score convert into a stars")
                print()
            else:
                stars = "*" * score
                print(stars)
            print(MENU)
            choice = input("Input your choice = ").upper()
        else:
            print("Invalid Choice")
            print()
            print(MENU)
            choice = input("Input your choice = ").upper()
    print("Farewell")


def get_valid_score():
    """Function to get valid score"""
    score = int(input("Enter a score: "))
    while MINIMUM_SCORE > score > MAXIMUM_SCORE:
        print("Invalid score")
        score = input("Enter a score: ")
    return score

def determine_score(score):
    """Function to determine the score message based on the score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        score_message = "Invalid Input"
    elif score >= HIGH_SCORE:
        score_message = "Excellent"
    elif score >= PASS_SCORE:
        score_message = "Passable"
    else:
        score_message = "Bad"
    return score_message


main()
