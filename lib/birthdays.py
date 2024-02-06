class Birthdays():
    def __init__(self):
        self.birthdays = {}

    def adds_birthday(self, name, date):
        self.birthdays[name] = date
        return self.birthdays
    
    def updates_date(self, name, date):
        self.birthdays.update({name:date})
        return self.birthdays
    
    def updates_name(self, old_name, name):
        self.birthdays[name] = self.birthdays.pop(old_name)
        return self.birthdays