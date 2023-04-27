from datetime import datetime

FIELDS_NAMES = ['Note_name', 'Note_text', 'Date_create', 'Date_last_edit']


def get_fields_names():
    global FIELDS_NAMES
    heads = ['id']
    for item in FIELDS_NAMES:
        heads.append(item)
    # print(heads)
    return heads


def set_note_data(id):
    global FIELDS_NAMES
    note = {'id': id}
    data = input(f"Input {FIELDS_NAMES[0]}:")
    note[FIELDS_NAMES[0]] = data
    data = input(f"Input {FIELDS_NAMES[1]}:")
    note[FIELDS_NAMES[1]] = data
    note[FIELDS_NAMES[2]] = datetime.today()
    note[FIELDS_NAMES[3]] = datetime.today()
    return note


def edit_note_data(note):
    global FIELDS_NAMES
    for i in range(2):
        print(f"{FIELDS_NAMES[i]} is: {note[FIELDS_NAMES[i]]}")
        answer = get_confirmation("Are you gonna change it?")
        if answer == 'Y' or answer == 'y':
            data = input(f"Input new {FIELDS_NAMES[i]}:")
            note[FIELDS_NAMES[i]] = data

    note[FIELDS_NAMES[3]] = str(datetime.today())
    return note


def warning_delete_notes_book():
    print("У вас есть записи в текущей книге и они будут удалены!!!")
    input()


def print_notes(notes_book):
    global FIELDS_NAMES
    print(f"ID  {FIELDS_NAMES[0]}          {FIELDS_NAMES[2]}         {FIELDS_NAMES[3]}")
    for item in notes_book:
        print(
            f"{item['id']}   {item[FIELDS_NAMES[0]]:16.12} {item[FIELDS_NAMES[2]]:17.16}    {item[FIELDS_NAMES[3]]:.16}")
        print(f"Note: {item[FIELDS_NAMES[1]]}")
        print()
    input('Press any key to continue')


def show_note(note):
    global FIELDS_NAMES
    print(
        f"ID: {note['id']}  {FIELDS_NAMES[0]}: {note[FIELDS_NAMES[0]]}  {FIELDS_NAMES[2]}: {note[FIELDS_NAMES[2]]}  {FIELDS_NAMES[3]}: {note[FIELDS_NAMES[3]]}")
    print(f"Note:     {note[FIELDS_NAMES[1]]}")
    input()


def get_variant():
    var = ''
    while var == '':

        try:
            var = input("Choose your variant - ")
        except ValueError:
            print("Input a variant.")

    return var


def get_id(text):
    print(text)
    value = get_value()
    return value


def get_id_edit():
    print("Choose id number your want to delete from notes book - ", )
    id_del = get_value()
    return id_del


def get_confirmation(text):
    a = input(text, )
    match a:
        case "y" | "Y" | "n" | "N":
            return a
        case _:
            return get_confirmation('Input y or n')


def get_value():
    while True:

        try:
            value = int(input())
            return value
        except ValueError:
            print("Input a value.")


