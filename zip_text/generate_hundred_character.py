from random import choices
from string import ascii_letters, digits
from zipfile import ZipFile
import os


COUNT_LINES: int = 10000
COUNT_SYMBOL: int = 100
BASE_DIR: str = 'src'
FILENAME: str = "generated_ten_thousand.txt"
ZIP_FILENAME: str = "generated_ten_thousand.zip"


def generated_string(symbol_count:int) -> str:
        symbol_random: str = ascii_letters + digits
        return "".join(choices(population=symbol_random, k=symbol_count))


def generated_lines(count_symbol: int, lines: int) -> str:
        return "".join(generated_string(count_symbol) + '\n' for _ in range(lines))


def write_ten_thousand(filename: str, string: str):
    with open(filename, 'w') as f:
        f.write(string)


def archive_file(input_filename: str, output_filename:str):
    with ZipFile(output_filename, 'w') as zipf:
        zipf.write(input_filename)


def main() -> None:
    result = generated_lines(COUNT_SYMBOL, COUNT_LINES)
    print(result)

    filename: str = os.path.join(BASE_DIR, FILENAME)
    write_ten_thousand(filename, result)
    print(f"Файл сохранен: {filename}")

    zip_filename: str = os.path.join(BASE_DIR, ZIP_FILENAME)
    archive_file(filename, zip_filename)
    print(f"Архив создан: {zip_filename}")


if __name__ == "__main__":
    main()