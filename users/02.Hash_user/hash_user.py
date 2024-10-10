from hashlib import md5
from hash_files import read_hashed, add_hashed

FILENAME = 'user.txt'

CHOICE = {"да", "нет", "y" ,"n" ,"yes" , "no"}

def hashed(obj):
    return md5(obj.encode()).hexdigest()

def main() -> None:
    while True:
        username = input("Введите имя пользователя: ")
        hashes = read_hashed(FILENAME)
        if username in hashes:
            print("Пользователь существует!")
        else:
            print("Хэш не найден! Сохранить?")
            save_hash_user = ""
            while save_hash_user not in CHOICE:
                save_hash_user = input("(да/нет): ").strip().lower()
                if save_hash_user not in CHOICE:
                    print("Пожалуйста, введите 'да' или 'нет'.")
                elif save_hash_user == 'да':
                    hash_value = hashed(username)
                    add_hashed(FILENAME, username, hash_value)
                    print("Хэш успешно сохранен.")

        cont = ""
        while cont not in CHOICE:
            cont = input("Продолжить? (да/нет): ").strip().lower()
            if cont not in CHOICE:
                print("Пожалуйста, введите 'да' или 'нет'.")
            elif cont == 'нет' or cont == 'n' or cont == 'no':
                exit(0)
                print("Выход")
            else:
                print("Продолжение работы")




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExit")
