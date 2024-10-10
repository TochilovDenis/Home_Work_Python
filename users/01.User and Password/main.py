from error import RefuseToCreateNewUser, NoMoreAttempts
from get_user import user_process

def main() -> None:
    try:
        while True:
            user_process("users.txt")
    except (NoMoreAttempts, RefuseToCreateNewUser) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    try:
       main()
    except KeyboardInterrupt:
        print('Exit')