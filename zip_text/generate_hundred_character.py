from random import choices  # Импорт функции choices из модуля random для генерации случайных значений
from string import ascii_letters, digits  # Импорт строк ASCII и цифр из модуля string
from zipfile import ZipFile # Импорт класса ZipFile из модуля zipfile для работы с ZIP-архивами
import os                   # Импорт модуля os для операций с файловой системой

# Константы для настройки генерации файла:
COUNT_LINES: int = 10000  # Количество строк в файле (10 000)
COUNT_SYMBOL: int = 100   # Количество символов в каждой строке (100)
BASE_DIR: str = 'src'     # Базовая директория для хранения файлов ('src')
FILENAME: str = "generated_ten_thousand.txt"      # Имя исходного текстового файла
ZIP_FILENAME: str = "generated_ten_thousand.zip"  # Имя архива


def generated_string(symbol_count:int) -> str:
    """
    Функция генерирует случайную строку заданной длины из букв и цифр.

    :param symbol_count: Количество символов в строке
    :return: Генерация случайной строки заданной длины
    """
    symbol_random: str = ascii_letters + digits  # Создание строки, содержащей все ASCII-символы и цифры
    return "".join(choices(population=symbol_random, k=symbol_count))

def generated_lines(count_symbol: int, count_lines: int) -> str:
    """
    Функция генерирует заданное количество строк, используя generated_string для каждого элемента.

    :param count_symbol: Количество символов в каждой строке
    :param count_lines: Количество линий для генерации
    :return: Генерация и объединение строк с новыми строками
    """
    return "".join(generated_string(count_symbol) + '\n' for _ in range(count_lines))


def write_ten_thousand(filename: str, string: str):
    """
    Функция записывает сгенерированный текст в указанный файл.

    :param filename: Имя файла для сохранения
    :param string: Сгенерированная строка
    """
    # Открытие файла в режиме записи и закрытие после завершения операции
    with open(filename, 'w') as f:
        f.write(string)  # Запись сгенерированного текста в файл


def archive_file(input_filename: str, output_filename:str):
    """
    Функция создает ZIP-архив из указанного входного файла.

    :param input_filename: Имя входного файла для архивации
    :param output_filename: Имя выходного ZIP-архива
    """
    # Создание ZIP-архива и открытие его в режиме записи
    with ZipFile(output_filename, 'w') as zipf:
        zipf.write(input_filename)  # Добавление файла в ZIP-архив


def main() -> None:
    # 1. Генерация текста
    result = generated_lines(COUNT_SYMBOL, COUNT_LINES)
    print(result)
    # 2. Сохранение файла
    filename: str = os.path.join(BASE_DIR, FILENAME)
    write_ten_thousand(filename, result)
    print(f"Файл сохранен: {filename}")
    # 3. Архивирование файла
    zip_filename: str = os.path.join(BASE_DIR, ZIP_FILENAME)
    archive_file(filename, zip_filename)
    print(f"Архив создан: {zip_filename}")

if __name__ == "__main__":
    main()