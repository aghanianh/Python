cache = dict()

from functools import wraps

def valid_username(origin1):
    def wrapper1(name, *args, **kwargs):
        if not (5 <= len(name) <= 20 and name.isalnum() and name not in {'admin', 'root', 'varuj'}):
            raise ValueError(f"Invalid name '{name}' for user.")
        return origin1(name, *args, **kwargs)
    return wrapper1

def valid_mail(origin2):
    def wrapper2(name, mail, *args, **kwargs):
        valid_suffixes = {'@mail.ru', '@gmail.ru', '@yahoo.com', '@odnoklassniki.ru'}
        if not any(mail.endswith(suffix) for suffix in valid_suffixes):
            raise ValueError(f"Invalid mail '{mail}' for user.")
        return origin2(name, mail, *args, **kwargs)
    return wrapper2

def valid_number(origin3):
    def wrapper3(name, mail, number, *args, **kwargs):
        if (number.startswith('+374') and len(number) == 12 and number[1:].isdigit()) \
                or (number.startswith('0') and len(number) == 9 and number.isdigit()):
            return origin3(name, mail, number, *args, **kwargs)
        else:
            raise ValueError("Invalid number.")
        
    return wrapper3

@valid_username
@valid_mail
@valid_number
def set_user(name, mail, number):
    cache[name] = (mail, number)
    print(f"User '{name}' successfully added.")
set_user = valid_number(valid_mail(valid_username(set_user)))
def get_cache():
    print(cache)

# Example usage
try:
    set_user('varujan', 'varujam@gmail.ru', '077555090')
except ValueError as e:
    print(f"Validation error: {str(e)}")

get_cache()
print(set_user.__name__)

