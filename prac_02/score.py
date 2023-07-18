from random import randint

MAXIMUM_SCORE = 100
HIGH_SCORE = 90
PASS_SCORE = 50
MINIMUM_SCORE = 0

def main():
    score = float(input("Enter score: "))
    score_feedback = determine_score(score)

    print(score_feedback)

    random_score = randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(random_score)
    score_feedback = determine_score(random_score)
    print(score_feedback)

def determine_score(score):
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