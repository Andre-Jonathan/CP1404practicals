import datetime


class Project:
    def __init__(self, name, start_date, priority=0, cost_estimate=0, completion_percentage=0):
        """Stores details of a project."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Prints statement about the project based on the information provided"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"
