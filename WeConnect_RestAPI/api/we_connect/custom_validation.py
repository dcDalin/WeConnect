import re

def is_empty(the_input):
    if the_input.strip() == '':
        return True
    return False

def is_email(the_input):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", the_input):
        return True
    return False

def is_gender(the_input):
    if (the_input == 'Male') or (the_input == 'Female') or (the_input == 'Other'):
        return False
    return True        

def is_password(password):
    pass