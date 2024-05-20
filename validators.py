users = [
    {
        'email': 'some@mail.ru',
        'password': '123pass'
    },
    {
        'email': 'test@yahoo.com',
        'password': 'test123'
    }
]


def check_email(email):
    if email == 'exit':
        return None
    for i in users:
        if email == i['email']:
            return True
    return False


def check_password(password) -> bool:
    for i in users:
        if password == i['password']:
            return True
    return False
