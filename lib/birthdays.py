from datetime import datetime

class Birthdays():
    def __init__(self):
        self.birthdays = {}

    def adds_birthday(self, name, date):
        dob = datetime.strptime(date, "%Y/%m/%d")
        self.birthdays[name] = {'birthdate': dob, 'sent': False}
        return self.birthdays
    
    def updates_date(self, name, date):
        if name in self.birthdays:
            dob = datetime.strptime(date, '%Y/%m/%d')
            self.birthdays[name]['birthdate'] = dob
            return self.birthdays
        else:
            return f'{name} not found in list'
    
    def updates_name(self, old_name, name):
        if old_name in self.birthdays:
            self.birthdays[name] = self.birthdays.pop(old_name)
            return self.birthdays
        else:
            return f'{old_name} not found in list'

    def reminder(self, month):
        reminders = {}
        for name, value in self.birthdays.items():
            dob = value['birthdate']
            if dob.strftime('%B') == month:
                age = self.calculate_age(dob)
                reminders[name] = {"birthdate": dob.strftime('%Y/%m/%d'), "age": age}
        return reminders
    
    def calculate_age(self,birthdate):
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def mark_sent(self,name):
        if name in self.birthdays:
            self.birthdays[name]['sent'] = True
            return f'Card has been sent to {name}'
        else:
            return f'{name} not found'