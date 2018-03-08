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
    while True:
        if len(password) < 8:
            return {'message': 'Password is less than 8 characters'}
        elif re.search('[0-9]',password) is None:
            return {'message': 'No numbers present'}
        elif re.search('[A-Z]',password) is None: 
            return {'message': 'No capital letters present'}
        else:
            return True