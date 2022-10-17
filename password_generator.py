#Password Generator Project
from random import choice, randint, shuffle
import pyperclip

class Password:

  def password_generator(self):
    """Generates a password"""
    letters = ['shreya','devyani','gunu','vishakha','tutu','nitu','sony','arcade','pune','goa','carleton', 'guleph', 'ottawa', 'america', 'Japan', 'Nihon', 'ichiban', 'kawai', 'tutsnuts', 'custard','melon','laxmi','aroma','aurora','atlantic','arctic','nato','nubik','nodem', 'angela']
    numbers = ['6184','2811','1104','6778','0711','0511','2022','0411', '2611']
    symbols = ['#', '@']

    password_letters = [choice(letters)]
    password_symbol = [choice(symbols)]
    password_numbers = [choice(numbers)]

    password_list = password_letters + password_symbol + password_numbers

    password = "".join(password_list)
    password = password.title()
    pyperclip.copy(password)
    return password
