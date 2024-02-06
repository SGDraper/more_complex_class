from datetime import datetime

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

    def reminder(self, month):
        reminders = {}
        for name, date in self.birthdays.items():
            dob = datetime.strptime(date,"%Y/%m/%d")
            if dob.strftime('%B') == month:
                age = self.calculate_age(dob)
                reminders[name] = {"birthdate":date,"age":age}
        return reminders
    
    def calculate_age(self,birthdate):
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
