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
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
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
    print(projects)
    print(MENU_CHOICE)
    user_pick = input(">>> ").title()
    while user_pick != "Q":
        if user_pick == "L":
            print("Load")
        elif user_pick == "S":
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
            print("Filter")
        elif user_pick == "A":
            print("Add")
        elif user_pick == "U":
            print("Update")
        else:
            print("Invalid menu choice")
        print(MENU_CHOICE)
        user_pick = input(">>> ").title()


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
