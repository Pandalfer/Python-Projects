import ast

passwords_file: str = "passwords.txt"
class USER:
    def __init__(self, name, password) -> None:
        self.name: str = name
        self.password: str = password
    
    @staticmethod
    def check_login_info(password: str, name: str) -> bool:
        with open(passwords_file, "r") as file:
            for line in file:
                if line.strip():
                    data: list = ast.literal_eval(line.strip())
                    credentials: list = data[0]
                    if credentials[0] == name and credentials[1] == password:
                        return True
        print("")
        print("No user found in database")
        return False

def create_user(name, password) -> None:
    user = USER(name, password)
    user_info = [[user.name, user.password]]
    with open(passwords_file, "r+") as file:
        if len(file.readlines()) >= 1:
            file.write("\n")
    with open(passwords_file, "a") as file:
        file.write(str(user_info))
    
    handle_password_actions(user.name, user.password)

def login() -> None:
    name: str = input("Please enter your name: ")
    password: str = input("Please enter your password: ")
    user: USER = USER(name, password)
    if user.check_login_info(password, name):
        print(f"\nWelcome, {name}")
        handle_password_actions(name, password)
    else:
        would_like_to_register: str = input("Would you like to register instead? (y / n): ")
        if would_like_to_register.lower() == "y":
            register()
        else:
            print("Exiting program...")
            quit()


def register() -> None:
    name: str = input("Please enter your name: ")
    password: str = input("Please enter your password: ")
    create_user(name, password)
    print(f"\nWelcome, {name}")

def get_data_from_line_number(line_number):
    with open(passwords_file, "r+") as file:
        for current_line, line in enumerate(file, start=1):
            if current_line == line_number:
                data = ast.literal_eval(line.strip())
                return data
def show_passwords(line_number):
    data = get_data_from_line_number(line_number)
    passwords = data[1:]
    if len(passwords) <= 0:
        print("You have no passwords saved")
    else:
        print("\nYour current passwords are:")
        for password in passwords:
            print(f"  => {password[0]}: '{password[1]}'")

def update_data_from_line_number(line_number: int, new_data: str) -> None:
    with open(passwords_file, "r") as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        lines[line_number - 1] = f"{new_data} \n"
    else:
        raise ValueError(f"Line {line_number} does not exist in the file.")

    with open(passwords_file, "w") as file:
        file.writelines(lines)


def add_password(line_number):
    data = get_data_from_line_number(line_number)
    password = input("Please enter the new password: ")
    context = input("What is the context of this new password: ")
    combined_data = [context, password]
    data.append(combined_data)
    update_data_from_line_number(line_number, data)


def remove_password(line_number: int):
    data = get_data_from_line_number(line_number)
    
    password = input("Please enter the password you wish to remove: ")
    for i, passwords in enumerate(data[1:], start=1):
        if passwords[1] == password:
            data.pop(i)
            break
    else:
        print("Password not found in the list.")
        return
    
    update_data_from_line_number(line_number, str(data))


def handle_password_actions(username: str, user_password: str) -> None:
    with open(passwords_file, "r") as file:
        data_line: None = None
        for line_number, line in enumerate(file, start=1):
            if line.strip():
                data = ast.literal_eval(line.strip())
                credentials = data[0]
                if credentials[0] == username and credentials[1] == user_password:
                    data_line: int = line_number
                    break
        show_passwords(data_line)
        action = input("Would you like to add or remove a password?: ")
        while True:

            if action.lower() == "add":
                add_password(data_line)
                action = input("Would you like to add or remove a password?: ")
            elif action.lower() == "remove":
                remove_password(data_line)
                action = input("Would you like to add or remove a password?: ")
                continue
            elif action.lower() == "quit":
                print("Exiting program...")
                quit()
            elif action.lower() == "show":
                show_passwords(data_line)
                action = input("Would you like to add or remove a password?: ")
                continue
            else:
                print("Invalid input")
                action = input("Would you like to add or remove a password?: ")
                





def main() -> None:
    print("Welcome to Password Manager")
    login_or_register: str = input("Would you like to login or register?: ")
    match login_or_register:
        case "login":
            login()
        case "register":
            register()
        
        case _:
            print("Invalid Input")
            main()




if __name__ == "__main__":
    main()

