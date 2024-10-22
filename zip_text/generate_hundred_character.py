from random import randint, choices
from string import ascii_letters, digits

LINES: int = 10000
COUNT: int = 100


def generator_ten_thousand(symbol_count:int):
        symbol_random: str = ascii_letters + digits
        return "".join(choices(population=symbol_random, k=symbol_count))


def main() -> None:
    for _ in range(LINES):
        generators = generator_ten_thousand(COUNT)
        print(generators)


if __name__ == "__main__":
    main()