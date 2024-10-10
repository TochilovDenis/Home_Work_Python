def read_hashed(filename) -> dict[str, str]:
    hashes: dict[str, str] = {}

    with open(filename, 'r', encoding='utf=8') as f:
        for line in f:
            username, hash_value = line.strip().split(':')
            hashes[username] = hash_value

    return hashes


def add_hashed(filename, username, hash_value):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(f"{username}: {hash_value}\n")