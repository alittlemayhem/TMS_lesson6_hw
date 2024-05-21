from getters import get_email, get_password
from validators import check_email, check_password


def app() -> None:
    while True:
        user_email = get_email()
        if check_email(user_email) is None:
            print("See you next time! Bye!")
            break

        user_password = get_password()

        if check_email(user_email) and check_password(user_password):
            print(f'Hello, {user_email}!')
            break
        else:
            print('Authentication error! Try again.')


if __name__ == '__main__':
    app()
