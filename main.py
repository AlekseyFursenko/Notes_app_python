import controller
import database_ops

notes_book = []
database_ops.import_from_csv(notes_book)
controller.start(notes_book)
