from datetime import datetime, date


class Human:
    def __init__(self, name: str, surname: str, patronymic: str, birth_date: date):
        self.name: str        = name
        self.surname: str     = surname
        self.patronymic: str  = patronymic
        self.birth_date: date = birth_date


    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name[0]} | "
                f"Отчество: {self.patronymic[0]} | "
                f"Дата рождения: {self.birth_date}")


def add_person(dictionary: dict, person: str or Human) -> None:
    full_name = f"{person.name} {person.surname} {person.patronymic}".strip()

    if full_name in dictionary:
        print(f"Человек с ФИО: {full_name} уже существует в словаре.")
    else:
        dictionary[full_name] = person
        print(f"Человек: {full_name} успешно добавлен в словарь.")


def main():
    people_dict: dict     = dict()

    while True:
        name: str         = input("Введите имя: ").strip()
        surname: str      = input("Введите фамилию: ").strip()
        patronymic:str    = input("Введите отчество: ").strip()
        date_birth: str   = input("Введите дату рождения (YYYY-MM-DD): ").strip()
        format_date: str  = '%Y-%m-%d'
        birth_date: date  = datetime.strptime(date_birth, format_date).date()
        new_person: Human = Human(name, surname, patronymic, birth_date)
        add_person(people_dict, new_person)

        cont: str         = input("Добавить еще одну персону? (д/н): ").lower().strip()
        if cont not in ['д', 'y']:
            break


if __name__ == "__main__":
    main()