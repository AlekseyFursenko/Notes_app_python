import view


# новая заметка
def new_note(notes_book):
    new_id = get_new_id(notes_book)
    note = view.set_note_data(new_id)
    return note


# получение id
def get_new_id(notes_book):
    max_id = 0
    for item in notes_book:
        id = int(item['id'])
        if id > max_id:
            max_id = id

    max_id += 1
    return max_id


# удалить заметку
def delete_note(notes_book: list, id):
    for item in notes_book:
        if item['id'] == id:
            notes_book.remove(item)
            return notes_book

    return notes_book


# редактировать заметку
def edit_note(notes_book, id_edit):
    for item in notes_book:
        if item['id'] == id_edit:
            view.edit_note_data(item)
            return notes_book
    print(f'No such note with id {id_edit} exist. Try another one.')
    return notes_book


# показать заметку
def show_note(notes_book: list, id):
    for item in notes_book:
        if item['id'] == id:
            item = view.show_note(item)
