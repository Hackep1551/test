import json


class User:
    def __init__(self, name, password, hendler):
        self.password = password
        self.hendler = hendler
        self.name = name
        self.is_write = False

    def read(self):
        data = self.hendler.read()
        for note in data:
            print(f"{note['user']}: {note['text']}")

    def write(self):
        if self.is_write:
            text = input("Текст: ")
            self.hendler.write({
                'user': self.name,
                'text': text
            })
            print("Нельзя")
        else:
            print("Не доступно")


class FileHandler:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def write(self, note):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        data.append(note)
        with open(self.path, "r", encoding="utf-8") as file:
            json.dump(file, note, ensure_ascii=False)


def main():
    hendler = FileHandler("file.json")
    sasha = User("Саша", "1234", hendler)
    vova = User("Вова", "4321", hendler)
    users = [sasha, vova]
    print("Ваше имя")
    user_input = input()
    current_user = ""
    for user in users:
        if user_input == user.name:
            current_user = user
            break
    if not current_user:
        print("Нет такого пользователя")
        exit()
    print("Ваш пароль")
    user_input = input()
    if user_input != current_user.password:
        print("Неверный пароль")
        exit()
    current_user.read()

if __name__ == "__main__":
    main()
