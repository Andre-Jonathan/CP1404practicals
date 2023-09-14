class Band:
    def __init__(self, name: str):
        """Stores details of a musician."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Prints statement about the musicians and information provided"""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)}"

    def add(self, name):
        """Add musician in the list"""
        self.musicians.append(name)

    def play(self):
        """prints the musicians in a list"""
        return '\n'.join(musician.play() for musician in self.musicians)
