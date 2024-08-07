from database_model import Lesson,Session,text, create_k_class
from sqlalchemy import Table, select

def get_next_lesson(session:Session) -> int:
    stmt = text("SELECT rowid FROM lesson where rowid = (SELECT MAX(rowid) FROM lesson)")
    result = session.execute(stmt).scalar()
    if result is None:
      return 1
    else:
      return result + 1

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
