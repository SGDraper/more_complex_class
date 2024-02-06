from datetime import datetime
from lib.birthdays import *

def test_adds_birthday():
    birthdays = Birthdays()
    result = birthdays.adds_birthday('Maria', '2000/08/17')
    assert result == {'Maria': '2000/08/17'}

def test_update_date():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    result = birthdays.updates_date("Maria","2000/08/16")
    assert result == {'Maria': '2000/08/16','Sam': '1994/11/28'}


def test_update_name():
    birthdays = Birthdays()
    birthdays.adds_birthday('Maria', '2000/08/17')
    birthdays.adds_birthday('Sam', '1994/11/28')
    result = birthdays.updates_name("Maria","Majo")
    assert result == {'Majo': '2000/08/17','Sam': '1994/11/28'}