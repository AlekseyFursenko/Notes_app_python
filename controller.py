import datetime

import database_ops
import ui
import view
import note_ops


# загрузить интерфейс

def show_ui():
    ui.start()


# def add_new_phonebook():
#     global phone_book
#     if phone_book == False:
#         view.warning_delete_phonebook()

#     phone_book = database_ops.new_phone_book()
#     return phone_book


def start(notes_book):
    show_ui()
    get_option(notes_book)


def get_option(notes_book):

    var = int(view.get_variant())

    match var:
        case 1:  # просмотр заметки
            id_view = str(view.get_id("Choose note's id number you want to view - "))
            note_ops.show_note(notes_book, id_view)
            return start(notes_book)

        case 2:  # добавить новую заметку
            notes_book.append(note_ops.new_note(notes_book))
            return start(notes_book)

        case 3:  # редактировать заметку
            id_edit = str(view.get_id("Choose id number your want to edit - "))
            note_ops.edit_note(notes_book, id_edit)
            return start(notes_book)

        case 4:  # удалить контакт
            id = int(view.get_id("Choose id number your want to delete from notes book - "))
            answer = view.get_confirmation('Are you sure?')
            if answer == 'y' or answer == 'Y':
                note_ops.delete_note(notes_book, id)
            return start(notes_book)

        case 5:  # распечатать книгу
            view.print_notes(notes_book)
            return start(notes_book)

        case 6:  # сохранить экспорт в csv
            database_ops.export_to_csv(notes_book)
            return start(notes_book)

        case 7:  # загрузить импорт из csv
            notes_book =[]
            database_ops.import_from_csv(notes_book)
            return start(notes_book)

        case 8:  # создать новую книгу заметок
            view.warning_delete_notes_book()
            answer = view.get_confirmation('Are you sure?')
            if answer == 'y' or answer == 'Y':
                notes_book = database_ops.new_notes_book()

            return start(notes_book)

        case 9:  # заметки на выбранную дату
            date = view.get_date()
            headers = view.get_fields_names()
            notes_on_date = []
            for item in notes_book:
                date_time_obj = datetime.datetime.strptime(item[headers[3]], '%Y-%m-%d %H:%M:%S.%f')
                #print(date_time_obj.date())
                if date_time_obj.date() == date:
                    notes_on_date.append(item)
            view.print_notes(notes_on_date)

            return start(notes_book)

        case 0:
            database_ops.export_to_csv(notes_book)
            print("All changes have been saved! Press any key to exit.")
            input()
            exit()

        case _:
            print('Input another variant!!')
            get_option(notes_book)


