from random import randint, choices
from string import ascii_letters, digits

COUNT_LINES: int = 10000
COUNT_SYMBOL: int = 100
FILENAME = "src\generated_ten_thousand.txt"


def generated_string(symbol_count:int):
        symbol_random: str = ascii_letters + digits
        return "".join(choices(population=symbol_random, k=symbol_count))


def generated_lines(count_symbol: int, lines: int) -> str:
        return "".join(generated_string(count_symbol) + '\n' for _ in range(lines))


def write_ten_thousand(filename: str, string: str):
    with open(filename, 'w') as f:
        f.writelines(string)


def main() -> None:
    result = generated_lines(COUNT_SYMBOL, COUNT_LINES)
    print(result)
    write_ten_thousand(FILENAME, result)


if __name__ == "__main__":
    main()