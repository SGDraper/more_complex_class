## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"


## 2. Design the Class Interface

class Birthdays():
# User-facing properties:
#   name: string

    def __init__(self):
initiate empty dictionary


    def add_birthday(self, name, date, sent(boolean = false by default): 
name = name of the person
date = date of birth


    def update_date(self, name, new_date)
name is current name, used to find the item
new date is the new date used to relace the existing value

    def update_name(self, old_name, new_name)
old name is used to find the item
new name is used to replace the existing name value

    def birthday_reminder(self, month)
month is used to find the birthdays in that month
returns the list of birthdays upcoming oin that month


    def get_ages(self, maybe month):
returns dictionary with the ages of each person included (current age or upcoming age?)

    def mark_sent(self, name, done(boolean))
unsure 

