from random import randrange, choice


class User:  # Описание класса User
    def __init__(self, surname, name, patronymic, age):  # конструктор класса
        self.name = name  # создание и инициализация переменной name
        self.surname = surname  # создание и инициализация переменной surname
        self.patronymic = patronymic  # создание и инициализация переменной patronymic
        self.age = age  # создание и инициализация переменной age

    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name} | "
                f"Отчество: {self.patronymic} | "
                f"Возраст: {self.age}")

    def short(self, sep: str = '/'):
        return f"{self.surname}{sep}{self.name}{sep}{self.patronymic}{sep}{self.age}"


user_string = {
    0: "нет пользователей",
    1: "пользователь",
    2: "пользователя",
    3: "пользователя",
    4: "пользователя",
    5: "пользователей",
    6: "пользователей",
    7: "пользователей",
    8: "пользователей",
    9: "пользователей",
}


def get_users_string_by_amount(n: int) -> str:
    if n == 0:
        return user_string[0]
    return str(n) + " " + user_string[int(n % 10)]


class UsersList:
    def __init__(self):
        self.users: list[User] = list()

    def __len__(self):
        return len(self.users)

    def __str__(self):
        return f"В списке сейчас {get_users_string_by_amount(len(self.users))}."

    def add_user(self, u: User) -> None:
        self.users.append(u)

    def print_users(self) -> None:
        for u in self.users:
            print(u)


names: list[str] = ['Denis', 'Alex', 'Ivan', 'Sasha']
surnames: list[str] = ['Tochilov', 'Smirnov', 'Ivanov', 'Shanin']
patronymics: list[str] = ['Nikolaevich', 'Ivanovich', 'Veniaminovich', 'Alexandrovich']


def generate_name() -> User:
    return User(choice(surnames), choice(names), choice(patronymics), randrange(10, 100))


def parse_user(s: str, sep: str = ":") -> User:
    """
    Function to parse a string with a sep and return a User object
    :param s:
    :param sep:
    :return:
    """
    split_str = s.strip().split(sep)
    return User(split_str[0], split_str[1], split_str[2], split_str[3])


class FileWorker:
    @staticmethod
    def write_file(users: UsersList, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for user in users.users:
                f.write(user.short() + '\n')

    @staticmethod
    def read_file(users: UsersList, filename) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.readlines()
            for line in result:
                users.add_user(parse_user(line))


if __name__ == '__main__':
    userList = UsersList()
    for _ in range(33):
         userList.add_user(generate_name())
    userList.print_users()

    #print(len(userList))
    print(userList)
    file = FileWorker()
    file.write_file(userList, 'users.txt')
    file.read_file(userList, 'users.txt')
    userList.print_users()