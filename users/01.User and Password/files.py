import os

def add_user_files(filename: str, user: str, password: str) -> None:
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{user}: {password}\n")

def read_user_file(filename: str) -> dict[str, str]:
    result: dict[str, str] = {}
    if not os.path.exists(filename):
        return result

    with open(filename, 'r', encoding='utf-8') as file:
        return {line.split(":")[0].strip() : line.split(":")[1].strip() for line in file.readlines()}