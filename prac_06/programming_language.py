class ProgrammingLanguage:
    """Information about some programming language"""
    def __init__(self, name, typing, reflection, year):
        """Create a ProgrammingLanguage object with the provided values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """returns a print statement about the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """determine of a programming language is dynamic"""
        return self.typing == "Dynamic"


def list_dynamic():
    """List all the programming language that is dynamically typed"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    list_dynamic()
