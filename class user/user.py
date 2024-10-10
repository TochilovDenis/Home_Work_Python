class User:  # Описание класса User
    def __init__(self, name, surname, patronymic, age):  # конструктор класса
        self.name = name  # создание и инициализация переменной name
        self.surname = surname  # создание и инициализация переменной surname
        self.patronymic = patronymic  # создание и инициализация переменной patronymic
        self.age = age  # создание и инициализация переменной age

    def __str__(self):
        return f"Фамилия: {self.name} | Имя: {self.name} | Отчество: {self.patronymic} | Возраст: {self.age}"


class UsersList:
    def __init__(self):
        self.users: list[User] = list()

    def add_user(self, users: User) -> None:
        self.users.append(users)

    def print_all_users(self) -> None:
        for i, user in enumerate(self.users):
            print(f"[{i}]: {user}")


user1 = User("Dsdsd","Tsddzc", "NASDF", "30")
user2 = User("Asds","Ndesd", "ACX", "31")
user3 = User("Csds","Tddf", "AXX", "32")
user4 = User("Bsdsd","Jsd", "NF", "33")
user5 = User("Csd","Rsd", "NG", "34")

user_list = UsersList()
user_list.add_user(user1)
user_list.add_user(user2)
user_list.add_user(user3)
user_list.add_user(user4)
user_list.add_user(user5)


user_list.print_all_users()
