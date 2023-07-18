def main():
    score = float(input("Enter score: "))
    score_feedback = determine_score(score)

    print(score_feedback)

def determine_score(score):
    if 0 > score > 100:
        score_message = "Invalid Input"
    elif score >= 90:
        score_message = "Excellent"
    elif score >= 50:
        score_message = "Passable"
    else:
        score_message = "Bad"
    return score_message
