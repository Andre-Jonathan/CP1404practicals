from project import Project
import datetime
from operator import itemgetter

MENU_CHOICE = """
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit
"""
FILENAME = "projects.txt"
NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
COMPLETION_INDEX = 4
COMPLETED_PPERCENTAGE = 100
projects = []


def main():
    extract_file(FILENAME)
    print(projects)
    print(MENU_CHOICE)
    user_pick = input(">>> ").title()
    while user_pick != "Q":
        if user_pick == "L":
            extract_file(FILENAME)
            print("Load")
        elif user_pick == "S":
            save_file(FILENAME)
            print("Save")
        elif user_pick == "D":
            incomplete_projects, completed_projects = sort_completion(projects)
            print("Incomplete projects: ")
            for project in incomplete_projects:
                print(project)
            print("Complete projects: ")
            for project in completed_projects:
                print(project)
        elif user_pick == "F":
            get_valid_date("Show projects that start after date (dd/mm/yy): ")

            print("Filter")
        elif user_pick == "A":
            print("Let's add a new project")
            new_name = get_valid_input("Name: ")
            new_date = get_valid_date("Start date (dd/mm/yy): ")
            new_priority = get_valid_input("Priority: ")
            new_cost = get_valid_input("Cost estimate: $")
            new_percent = get_valid_input("Percent complete: ")
            new_project = Project(new_name, new_date, new_priority, new_cost, new_percent)
            projects.append(new_project)
        elif user_pick == "U":
            print("Update")
        else:
            print("Invalid menu choice")
        print(MENU_CHOICE)
        user_pick = input(">>> ").title()


def get_valid_date(prompt):
    """get valid date"""
    date_check = True
    date = input(prompt)
    while date_check:
        try:
            valid_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            formatted_date = valid_date.strftime("%d/%m/%Y")
            date_check = False
        except ValueError:
            print("Invalid date")
            date = input(prompt)
    return formatted_date


def get_valid_input(prompt):
    """get valid inputs"""
    subject = input(prompt)
    while subject == "":
        print("It should be filled")
        subject = input(prompt)
    return subject


def extract_file(filename):
    """Extract information from the filename into the projects list"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for row in in_file:
            part = row.strip().split('\t')
            name = part[NAME_INDEX]
            date = part[DATE_INDEX]
            priority = part[PRIORITY_INDEX]
            cost_estimate = part[COST_INDEX]
            completion_estimate = part[COMPLETION_INDEX]
            project = Project(name, date, priority, cost_estimate, completion_estimate)
            projects.append(project)


def save_file(filename):
    """Save information from the projects list into the file"""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            project_report = [project.name, project.start_date, project.priority, project.cost_estimate,
                         project.completion_percentage]
            print("\t".join(str(element) for element in project_report), file=out_file)


def sort_completion(projects):
    """Sort the projects by completion percentage"""
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.completion_percentage != COMPLETED_PPERCENTAGE:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    return incomplete_projects, completed_projects


main()