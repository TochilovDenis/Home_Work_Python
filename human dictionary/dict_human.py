from datetime import datetime


class Human:
    def __init__(self, name: str, surname: str, patronymic: str, birth_date: datetime):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date


    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name[0]} | "
                f"Отчество: {self.patronymic[0]} | "
                f"Дата рождения: {self.birth_date}")


def add_human_to_dictionary(self, name: str, surname: str, patronymic: str, birthday: datetime):
    add_result = dict()

