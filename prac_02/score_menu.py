"""
import determine score function from score.py
score = ""
display menu
get choice
while choice != "Q"
    if choice == "G"
        get score
        while score < 0 and score > 100
            display invalid score
            get score
        get choice
    else if choice == "P"
        if score == ""
            display "You have not added a score"

        else
            score feedback = determine score(score)
            display score feedback
        get choice
    else if choice == "S"
        if score == ""
            display "You have not added a score"
        else
            display
        get choice
    else
        display invalid choice
        get choice

"""