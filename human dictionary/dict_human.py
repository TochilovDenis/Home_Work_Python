from calendar import monthrange
from datetime import date
from random import randint, choice

NAMES: list[str]       = ["Иван", "Петр", "Алексей", "Николай"]
SURNAMES: list[str]    = ["Иванов", "Петров", "Сидоров", "Кузнецов"]
PATRONYMICS: list[str] = ["Иванович", "Петрович", "Викторович", "Алексеевич"]


class InvalidDateError(Exception):
    ...


class Human:
    def __init__(self, surname: str, name: str, patronymic: str, birth_date: date):
        if not isinstance(birth_date, date):
            raise InvalidDateError("Неверная дата рождения")

        if birth_date > date.today():
            raise ValueError("Дата рождения не может быть в будущем")

        self.surname: str     = surname
        self.name: str        = name
        self.patronymic: str  = patronymic
        self.birth_date: date = birth_date


    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name} | "
                f"Отчество: {self.patronymic} | "
                f"Дата рождения: {self.birth_date}")


def add_person(dictionary: dict[str, Human], person: Human) -> bool:
    if not isinstance(dictionary, dict):
        raise TypeError("dictionary должен быть словарем")

    if not isinstance(person, Human):
        raise TypeError("person должен быть экземпляром класса Human")

    full_name: str = " ".join([person.surname, person.name, person.patronymic])

    if full_name in dictionary:
        print(f"Человек с ФИО: {full_name} уже существует в словаре.")
        return False
    else:
        dictionary[full_name] = person
        return True


def generate_birth_date() -> date:
    year = randint(1900, 2023)
    month = randint(1, 12)
    _, days_in_month = monthrange(year, month)
    day = randint(1, days_in_month)
    return date(year, month, day)


def print_people_list(people_dict: dict[str, Human]):
    print("\nСписок добавленных людей:")
    for i, (full_name, person) in enumerate(people_dict.items(), 1):
        print(f"{i}. {person}")


def main():
    people_dict: dict[str, Human] = dict()
    consecutive_errors: int = 0
    total_additions: int = 0
    total_errors: int = 0


    while True:
        birth_date: date  = generate_birth_date()
        new_person: Human = Human(
            choice(SURNAMES),
            choice(NAMES),
            choice(PATRONYMICS),
            birth_date)

        if add_person(people_dict, new_person):
            total_additions += 1
        else:
            total_errors += 1
            consecutive_errors += 1

        if consecutive_errors >= 4:
            print(f"Программа завершила работу после {consecutive_errors} ошибок подряд.")
            break

    print(f"\nРезультаты:")
    print_people_list(people_dict)
    print(f"\nДобавлено людей: {total_additions}")
    print(f"Всего ошибок добавления: {total_errors}")


if __name__ == "__main__":
    main()