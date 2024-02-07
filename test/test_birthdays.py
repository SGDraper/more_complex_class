from datetime import datetime
from lib.birthdays import *

def test_adds_birthday():
    birthdays = Birthdays()
    result = birthdays.adds_birthday('Maria', '2000/08/17')
    assert result == {'Maria': {'birthdate': datetime(2000, 8, 17), 'sent': False}}

def test_update_date():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    result = birthdays.updates_date("Maria","2000/08/16")
    assert result == {'Maria': {'birthdate': datetime(2000, 8, 16), 'sent': False},
                      'Sam': {'birthdate': datetime(1994, 11, 28), 'sent': False}}


def test_update_name():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    result = birthdays.updates_name("Maria","Majo")
    assert result == {'Majo': {'birthdate': datetime(2000, 8, 17), 'sent': False},
                      'Sam': {'birthdate': datetime(1994, 11, 28), 'sent': False}}

def test_birthday_reminder():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    result = birthdays.reminder('November')
    assert result == {'Sam':{"birthdate": "1994/11/28", "age": 29}}


def test_mark_sent():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    assert birthdays.mark_sent('Maria') == 'Card has been sent to Maria'
# def test_get_ages():
#     birthdays = Birthdays()
#     birthdays.adds_birthday('Maria', '2000/08/17')
#     birthdays.adds_birthday('Sam', '1994/11/28')
#     result = birthdays.get_ages("November")
#     assert result == {'Sam': '1994/11/28', "age" : "29"}
    