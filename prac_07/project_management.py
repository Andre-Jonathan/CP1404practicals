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
            file_name = input("Enter a filename: ")
            extract_file(file_name)
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
            date_check = False
            date = input("Show projects that start after date (dd/mm/yy): ")
            while date_check:
                try:
                    valid_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
                    date_check = True
                except ValueError:
                    print("Invalid date")
                    date = input("Show projects that start after date (dd/mm/yy): ")

            print("Filter")
        elif user_pick == "A":
            print("Add")
        elif user_pick == "U":
            print("Update")
        else:
            print("Invalid menu choice")
        print(MENU_CHOICE)
        user_pick = input(">>> ").title()


def extract_file(filename):
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
