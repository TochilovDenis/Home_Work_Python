from files import read_user_file, add_user_files
from error import RefuseToCreateNewUser, NoMoreAttempts
from hashlib import md5

def hashed(h: str) -> str:
    return md5(h.encode()).hexdigest()

def user_process(users_filename) -> str:
    users = read_user_file(users_filename)
    user = input("Введите имя пользователя: ")
    if user in users:
        for _ in range(5):
            password = input("Введите пароль: ")
            if hashed(password) == users[user]:
                print("Доступ разрешен")
                # если пароль верный - вернуть имя
                return user
            else:
                print("Неверный пароль.")
        else: #  или исчерпать количество попыток
            raise NoMoreAttempts("Больше никаких попыток. До свидания.")

    save_response = input("Сохранить это имя пользователя? (да/нет): ")
    no = ['no', 'No', 'нет', 'Нет']
    for n in no:
        if save_response == n:
            raise RefuseToCreateNewUser("Нельзя продолжать не создав этого пользователя. До свидания.")

    # если нет такого имени - то создать - записать имя и новый пароль
    for _ in range(5):
        password = input("Введите новый пароль: ")
        again_password = input("Введите новый пароль еще раз: ")
        if password == again_password:
            users[user] = hashed(password)
            add_user_files(users_filename, user, hashed(password))
            print("Логин и пароль успешно сохранен")
            break
        print(f"Введённые пароли не совпадают, попробуйте ещё раз")
    else:
        raise NoMoreAttempts("Больше никаких попыток. До свидания.")