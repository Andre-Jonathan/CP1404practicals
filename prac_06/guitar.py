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
        CURRENT_YEAR = 2023
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks if guitar is vintage"""
        VINTAGE_AGE = 50
        return self.get_age() >= VINTAGE_AGE
