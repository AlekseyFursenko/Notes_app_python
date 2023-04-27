import csv
import os
from pathlib import Path

import view


# новая книга заметок список
def new_notes_book():
    notes_book = []
    clear_csv()
    return notes_book


# загрузка предыдущей базы данных
def import_from_csv(notes_book: list):

    path = Path.cwd() / 'notes.csv'

    if not os.path.exists(path):
        clear_csv()

    csv_file = Path.cwd() / 'notes.csv'

    with open(csv_file, encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ";"
        file_reader = csv.DictReader(r_file, delimiter=";")

        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0

        # названия полей
        field_names = view.get_fields_names()
        header_csv = []
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'File consist following fields: {", ".join(row)}')
                for item in row:
                    header_csv.append(item)
                if field_names != header_csv:
                    print('The file is not supported by application, please try again.')
                    return

            # Ввод полей csv файла в notes book
            note = dict.fromkeys(field_names)
            for item in field_names:
                note[item] = row[item]

            notes_book.append(note)

            count += 1
    print(f'Total imported {count} notes. {notes_book}')


# сохранение книги заметок csv
def export_to_csv(notes_book: list):
    csv_file = Path.cwd() / 'notes.csv'

    with open(csv_file, 'w', newline='') as csv_file:
        # field_names = ['id', 'Name', 'Surname', 'Phone_number', 'Description']
        field_names = view.get_fields_names()
        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=";")

        writer.writeheader()
        for item in notes_book:
            writer.writerow(item)


# создание чистого csv файла заметок
def clear_csv():
    csv_file = Path.cwd() / 'notes.csv'

    with open(csv_file, 'w', newline='') as file:
        # field_names = ['id', 'Name', 'Surname', 'Phone_number', 'Description']
        field_names = view.get_fields_names()
        writer = csv.DictWriter(file, fieldnames=field_names, delimiter=";")
        writer.writeheader()
