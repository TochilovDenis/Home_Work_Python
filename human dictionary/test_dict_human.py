import io
import sys

import pytest
from calendar import monthrange
from datetime import date
from dict_human import Human, add_person, generate_birth_date, print_people_list


# Проверка класса
def test_human_init():
    human = Human("Т", "Д", "Н", date(1990, 1,1))
    assert isinstance(human, Human)
    assert human.surname == "Т"
    assert human.name == "Д"
    assert human.patronymic == "Н"
    assert human.birth_date == date(1990, 1,1)


def test_human_str():
    human = Human("Т", "Д", "Н", date(1990, 1,1))
    expected_output = "Фамилия: Т | Имя: Д | Отчество: Н | Дата рождения: 1990-01-01"
    assert str(human) == expected_output


# Проверка добавления персонала
def test_add_person():
    # Базовый случай: успешное добавление
    dictionary = {}
    person = Human("Петров", "Иван", "Иванович", date(1990, 1, 1))
    assert add_person(dictionary, person) == True
    assert len(dictionary) == 1
    assert list(dictionary.keys())[0] == "Петров Иван Иванович"
    assert dictionary["Петров Иван Иванович"] == person

    # Случай, когда человек уже существует
    dictionary["Петров Иван Иванович"] = person
    assert add_person(dictionary, person) == False
    assert len(dictionary) == 1

    # Ошибка: не является словарем
    with pytest.raises(TypeError):
        add_person({}, object())

    # Ошибка: не является экземпляром класса Human
    with pytest.raises(TypeError):
        add_person(dictionary, object())

    # Проверка полного имени
    assert " ".join(["Петров", "Иван", "Иванович"]) == "Петров Иван Иванович"


# Проверка дата рождения
def test_generate_birth_date():
    # Базовый тест: проверка типа возвращаемого значения
    assert isinstance(generate_birth_date(), date), "Функция должна возвращать объект type 'date'"

    # Тест на случайную дату
    birth_date = generate_birth_date()
    assert isinstance(birth_date, date), f"Возвращаемое значение не является объектом type 'date': {type(birth_date)}"

    # Проверка диапазона года
    assert 1900 <= birth_date.year <= date.today().year, \
        f"Год должен быть в диапазоне от 1900 до {date.today().year}, но получен год: {birth_date.year}"

    # Проверка месяца и дня
    assert 1 <= birth_date.month <= 12, f"Месяц должен быть в диапазоне от 1 до 12, но получен месяц: {birth_date.month}"
    assert 1 <= birth_date.day <= monthrange(birth_date.year, birth_date.month)[1], \
        f"День должен быть в диапазоне от 1 до количества дней в месяце, но получен день: {birth_date.day}"

    # Дополнительный тест на случайную дату
    second_birth_date = generate_birth_date()
    assert isinstance(second_birth_date, date), f"Вторая генерируемая дата не является объектом type 'date'"

    # Проверяем, что две сгенерированные даты различаются
    assert birth_date != second_birth_date, "Сгенерированные даты должны отличаться друг от друга"


# Проверка список персона на экран
def test_print_people_list():
    # Создаем тестовый словарь с людьми
    people_dict = {
        "Петров Иван Иванович": Human("Петров", "Иван", "Иванович", date(1990, 1, 1)),
        "Сидорова Анна Анатольевна": Human("Сидорова", "Анна", "Анатольевна", date(1985, 12, 31)),
        "Точилов Денис Николаевич": Human("Точилов", "Денис", "Николаевич", date(1970, 6, 15))
    }

    # Запускаем функцию и сохраняем вывод в переменную
    capturedOutput = io.StringIO()  # Создаем объект StringIO для хранения вывода
    sys.stdout = capturedOutput  # Перенаправляем stdout в наш объект StringIO
    print_people_list(people_dict)
    sys.stdout = sys.__stdout__  # Возвращаем stdout обратно в оригинальное состояние

    # Проверяем вывод
    expected_output = """Список добавленных людей:
1. Фамилия: Петров | Имя: Иван | Отчество: Иванович | Дата рождения: 1990-01-01
2. Фамилия: Сидорова | Имя: Анна | Отчество: Анатольевна | Дата рождения: 1985-12-31
3. Фамилия: Точилов | Имя: Денис | Отчество: Николаевич | Дата рождения: 1970-06-15
"""
    assert capturedOutput.getvalue().strip() == expected_output.strip(), \
        f"Вывод не соответствует ожидаемому:\nОжидаемый: {expected_output}\nФактический: {capturedOutput.getvalue()}"
