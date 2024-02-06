from datetime import datetime
from lib.birthdays import *

def test_adds_birthday():
    birthdays = Birthdays()
    result = birthdays.adds_birthday('Maria', '2000/08/17')
    assert result == {'Maria': '2000/08/17'}