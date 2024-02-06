class Birthdays():
    def __init__(self):
        self.birthdays = {}

    def adds_birthday(self, name, date):
        self.birthdays[name] = date
        return self.birthdays