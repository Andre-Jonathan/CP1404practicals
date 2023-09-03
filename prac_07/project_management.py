from project import Project
import datetime

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
COMPLETED_PERCENTAGE = 100


def main():
    """Get user to load, save, display, filter, add, and update on the projects"""
    projects = []
    extract_file(FILENAME, projects)
    print(MENU_CHOICE)
    user_pick = input(">>> ").title()
    while user_pick != "Q":
        if user_pick == "L":
            extract_file(FILENAME, projects)
        elif user_pick == "S":
            save_file(FILENAME, projects)
        elif user_pick == "D":
            incomplete_projects, completed_projects = sort_completion(projects)
            print("Incomplete projects: ")
            display_project(incomplete_projects)
            print("Complete projects: ")
            display_project(completed_projects)
        elif user_pick == "F":
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filter_date = [project for project in projects if project.start_date >= date]
            sort_filter_date = sorted(filter_date, key=sort_by_start_date)
            print("Filtered Projects")
            for project in sort_filter_date:
                print(project)
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
            for i, project in enumerate(projects, 0):
                print(i, project)
            project_choice = int(get_valid_input("Project choice: "))
            chosen_project = projects[project_choice]
            print(chosen_project)
            new_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_percentage != "":
                chosen_project.completion_percentage = new_percentage
            if new_priority != "":
                chosen_project.priority = new_priority

        else:
            print("Invalid menu choice")
        print(MENU_CHOICE)
        user_pick = input(">>> ").title()


def sort_by_start_date(project):
    """return index for each project's date"""
    return project.start_date


def display_project(projects):
    """prints all the project in projects list"""
    for project in projects:
        print(project)


def get_valid_date(prompt):
    """get valid date"""
    date_check = True
    date = input(prompt)
    formatted_date = ""
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


def extract_file(filename, projects):
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


def save_file(filename, projects):
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
        if project.completion_percentage != COMPLETED_PERCENTAGE:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    return incomplete_projects, completed_projects


main()
