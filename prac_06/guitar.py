"""
guitar
Estimate: 20 minutes
Actual:   106 minutes from 0:59 to 1:30
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Stores details of a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Prints statement about the guitar based on the information provided"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
