import re

def is_empty(the_input):
    if the_input.strip() == '':
        return True
    return False

def is_email(the_input):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", the_input):
        return True
    return False