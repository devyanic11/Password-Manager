#Password Generator Project
from random import choice, randint, shuffle
import pyperclip

class Password:

  def password_generator(self):
    """Generates a password"""
    letters = ['sony','arcade','pune','goa','carleton', 'guleph', 'ottawa', 'america', 'Japan', 'Nihon', 'ichiban', 'kawai', 'tutsnuts', 'custard','melon','laxmi','aroma','aurora','atlantic','arctic','nato','nubik','nodem', 'angela']
    numbers = ['1234', '43557','2534','8544','7890','3498', '4592', '9832', '0532']
    symbols = ['#', '@','$',"!']

    password_letters = [choice(letters)]
    password_symbol = [choice(symbols)]
    password_numbers = [choice(numbers)]

    password_list = password_letters + password_symbol + password_numbers

    password = "".join(password_list)
    password = password.title()
    pyperclip.copy(password)
    return password
