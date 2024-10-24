from zipfile import ZipFile  # Импорт класса ZipFile из модуля zipfile для работы с ZIP-архивами
import os  # Импорт модуля os для операций с файловой системой
from pathlib import Path # Импорт модуля Path для работы с путями

# Константы для настройки:
PATH_DIR: str = 'src'  # Базовая директория для хранения файлов ('src')
ZIP_FILENAME: str = "generated_ten_thousand.zip"  # Имя архива
FILENAME: str = 'generated_ten_thousand.txt' # Имя файла
EXTRACT_PATH: str = 'unzip'  # Базовая директория для распаковки хранения файлов ('unzip')


def cur() -> str:
    """
    Функция возвращает путь к текущей директории, где находится скрипт.
    """
    current_folder: str = os.path.dirname(os.path.realpath(__file__))
    return current_folder


def unzip_files(base_dir: str, zip_filename, extract_path: str):
    """
    Распаковывает ZIP-файл в указанную директорию.

    :param base_dir: Базовая директория для хранения архива.
    :param zip_filename: Имя ZIP-файла.
    :param extract_path: Путь для распаковки.
    """
    archive_path: str = Path(cur()) / base_dir / zip_filename
    with ZipFile(archive_path) as myzip:
        myzip.extractall(extract_path)

    extracted_path: Path = Path(cur()) / extract_path
    print(f"Файлы из архива успешно распакованы в: {extracted_path}")


def read_file_txt(file_path: str):
    """
    Читает содержимое файла с обработкой возможных ошибок.

    :param file_path: Путь к файлу для чтения.
    :return str или None: Содержимое файла или None в случае ошибки.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content: str = file.read()
        return content
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def count_symbol(text: str) -> dict[str, int]:
    """
    Подсчитывает количество каждого символа в тексте.

    :param text: Текст для анализа.
    :return Словарь с символами и их количеством.
    """
    symbol_count: dict[str, int] = dict()
    for symbol in text:
        symbol_count[symbol] = symbol_count.get(symbol, 0) + 1
    return symbol_count


def sort_dict_by_value(dictionary: dict, n: int) -> list[tuple[str, int]]:
    """
    Сортирует элементы словаря по значению (в данном случае,
    по количеству символов) и возвращает первые N элементов.

    :param dictionary: Словарь для сортировки.
    :param n: Количество элементов для возврата.
    :return Список из N элементов словаря, отсортированных по значению.
    """
    sorted_items = list()
    for item in dictionary.items():
        sorted_items.append(item)

    def get_key(i):
        return i[1]

    sorted_items.sort(key=get_key, reverse=True)
    return sorted_items[:n]


def find_top_n_symbol(text: str, n: int) -> dict[str, int]:
    """
    Находит N самых часто встречающихся символов в тексте.

    :param text: Текст для анализа.
    :param n: Количество топ-символов для нахождения.
    :return Словарь с топ-N символами и их количеством.
    """
    symbol_count = count_symbol(text)
    sorted_symbol = sort_dict_by_value(symbol_count, n)
    return dict(sorted_symbol)


def main() -> None:
    # 1. Распаковывает ZIP-файл.
    unzip_files(PATH_DIR, ZIP_FILENAME, EXTRACT_PATH)

    # 2. Читает содержимое файла.
    path = f"{EXTRACT_PATH}/{PATH_DIR}/{FILENAME}"
    txt_content: str = read_file_txt(path)

    if txt_content:
        # 3. Выводит все строки файла.
        print(f"Все строки файла:")
        print(txt_content)

        # 4. Находит 5 самых часто встречающихся символов и выводит их вместе с количеством.
        number: int = 5
        print(f"{number} самых повторяющихся символов и их количество:")
        most_common_symbol = find_top_n_symbol(txt_content, number)
        for symbol, count in most_common_symbol.items():
            print(f"{symbol}: {count}")


if __name__ == '__main__':
    main()