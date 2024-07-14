from database_model import Lesson,Session,text, create_k_class

def get_next_lesson(session:Session) -> int:
    stmt = text("SELECT rowid FROM lesson where rowid = (SELECT MAX(rowid) FROM lesson)")
    for record in session.execute(stmt):
        current_lesson = record[0]
    return current_lesson + 1

def update_note(session:Session, note: int, lesson_ID: int, press_time: float)->None:
    K = create_k_class(note)
    insert = K(lesson_ID = lesson_ID, time = press_time)
    session.add(insert)
    session.commit()
    return None

def update_lesson(session: Session,lesson_number:int,number_displayed_chords:int) -> None:
    lesson = Lesson(lesson_ID = lesson_number,number_displayed_chords = number_displayed_chords)
    session.add(lesson)
    session.commit()
    return None
