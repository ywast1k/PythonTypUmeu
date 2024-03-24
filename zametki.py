from csv import DictReader, DictWriter
from os.path import exists

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    note_title = input("Введите название заметки: ")
    note_content = input("Введите содержание заметки: ")
    return {'Название заметки': note_title, 'Содержание': note_content}

def create_file(file_name):
    if not exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=['Название заметки', 'Содержание'])
            f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    res.append(user_data)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Название заметки', 'Содержание'])
        f_writer.writeheader()
        f_writer.writerows(res)

def delete_data(file_name, line_number):
    res = read_file(file_name)
    if 1 <= line_number <= len(res):
        del res[line_number - 1]
        with open(file_name, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Название заметки', 'Содержание'])
            f_writer.writeheader()
            f_writer.writerows(res)
    else:
        raise LenNumberError(f"Недопустимый номер заметки. Доступны номера от 1 до {len(res)}.")

def edit_data(file_name, line_number):
    res = read_file(file_name)
    if 1 <= line_number <= len(res):
        user_data = get_info()
        res[line_number - 1] = user_data
        with open(file_name, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Название заметки', 'Содержание'])
            f_writer.writeheader()
            f_writer.writerows(res)
    else:
        raise LenNumberError(f"Недопустимый номер заметки. Доступны номера от 1 до {len(res)}.")

def main():
    file_name = 'Zametki.csv'

    while True:
        command = input("Работа с заметками -------\n w- создать заметку. \n r- прочитать заметки. \n c- копировать заметки. \n d- удалить заметку. \n e- редактировать заметку. \n q- выход. \n Введите команду:  ")
        if command == 'q':
            break
        elif command == 'w':
            create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файл не создан. Создайте его.")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            file_name_copy = 'Zametki_copy.csv'
            if not exists(file_name_copy):
                create_file(file_name_copy)
            try:
                line_number = int(input("Введите номер заметки для копирования: "))
                copy_data(file_name, file_name_copy, line_number)
            except LenNumberError as e:
                print(e.txt)
        elif command == 'd':
            try:
                line_number = int(input("Введите номер заметки для удаления: "))
                delete_data(file_name, line_number)
            except LenNumberError as e:
                print(e.txt)
        elif command == 'e':
            try:
                line_number = int(input("Введите номер заметки для редактирования: "))
                edit_data(file_name, line_number)
            except LenNumberError as e:
                print(e.txt)

main()