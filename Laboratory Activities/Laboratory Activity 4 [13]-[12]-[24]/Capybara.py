class Capybara:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"Capybara(name={self.name}, gender={self.gender}, age={self.age})"
