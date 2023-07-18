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
            score_feedback = determine score(score)
            get choice
        else if choice == "S"
            if score == ""
                display "You have not added a score"
            else
                stars = "*" * score
                display stars
            get choice
        else
            display invalid choice
            get choice

function get valid score()
    get score
    while score < 0 and score > 100
        display invalid score
        get score
    return score


"""