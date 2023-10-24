def valid_username(func):
    def wrapper(username):
        if not isinstance(username, str) or \
           not username.isalnum() or \
           len(username) > 20 or \
           len(username) < 4 or \
           username in {'admin', 'root', 'user'}:
            raise NameError("The name is invalid")
        return func(username)
    return wrapper
def valid_mail(func):
    def wrapper(mail):
        mail_details = ['@gmail.com',
                        'yahoo.com',
                        '@hotmail.com',
                        '@outlook.com',
                        '@aol.com',
                        '@icloud.com',
                        '@protonmail.com',
                        '@yahoo.co.uk',
                        '@rediffmail.com'
                        ]
        valid_flag = False
        check_mail = mail[1:]
        for i in mail_details:
            if check_mail.endswith(i):
                valid_flag = True
        if valid_flag == False :
            raise NameError ("Mail is invalid")
        
        return func(mail)
        
    return wrapper

def valid_phone(func):
    def wrapper(phone):
        if (not isinstance(phone, str)) or \
            (not phone.startswith('+374') and not phone.startswith('0')) or \
            (phone.startswith('+374') and len(phone) != 12 and not phone[4:].isdigit()) or \
            (phone.startswith('0') and len(phone) != 9 and phone.isdigit()):
            raise NameError("Phone-number is invalid")
        return func(phone)
    return wrapper


def valid_password(func):
    def wrapper(password):
        if (not isinstance(password, str)) or \
                len(password) < 8:
                    raise NameError ("Typed password is invalid")
        flag_upper = False
        flag_digit = False
        flag_lower = False
        for i in password:
            if i >= '0' and i <= '9':
                flag_digit = True
            if i >= 'a' and i <= 'z':
                flag_lower = True
            if i >= 'A' and i <= 'Z':
                flag_upper = True
        if flag_digit == flag_upper == flag_lower:
            return func(password)
        else:
            raise NameError ("Something goes wrong in password")
    return wrapper


def check_password(func):
    def wrapper(password, repeat_password):
        if password != repeat_password:
            raise NameError ("Passwords don't match")
        return func(password, repeat_password)
    return wrapper

@valid_username
def set_username(username: str) -> str:
    return username

@valid_mail
def set_mail(mail: str) -> str:
    return mail

@valid_phone
def set_phone(phone: str) -> str:
    return phone

@valid_password
def set_password(password: str) -> str:
    return password

@check_password
def check_password(password: str, repeat_password: str) -> bool:
    return password == repeat_password




while True:
    enter = input("Enter doing, add/break...")
    if enter == 'break': break
    if enter == 'add':

        username = input('Enter your username...')
        set_username(username)
        mail = input("Enter your mail ...")
        set_mail(mail)
        phone = input("Enter phone-number ...")
        set_phone(phone)
        password = input("Enter password ...")
        set_password(password)
        rep_password = input("Repeat password ...")
        check_password(password, rep_password)
        print("You have succesfully registered")

