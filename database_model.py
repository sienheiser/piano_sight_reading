from typing import Type
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, Float, text
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test2.db")
session = Session(engine)
Base = declarative_base()

class Lesson(Base):
    __tablename__ = "lesson"
    lesson_ID = Column(Integer,primary_key=True)
    number_displayed_chords = Column(Integer)

    def __rep__(self):
        return "<Lesson(lesson_ID= '%s',number_displayed_chords='%s')>" % (
            self.lesson_ID,
            self.number_displayed_chords
        )

def create_k_class(key: int) -> Type[Base]:
    if key < 10:
        table_name = f"K0{key}"
    else:
        table_name = f"K{key}"
    return type(table_name, (Base,), {
        '__tablename__': table_name,
        'lesson_ID': Column(Integer, primary_key=True),
        'time': Column(Float),
        '__repr__': lambda self: f"<{class_name}(lesson_ID= '{self.lesson_ID}', time='{self.time}')>"
    })


if __name__ == "__main__":
    #stmt = text("SELECT rowid, * FROM lesson WHERE rowid = (SELECT MAX(rowid) FROM lesson)")
    #for record in session.execute(stmt):
    #    print(record)
    stmt = text("SELECT * from K40")
    for record in session.execute(stmt):
        print(record)


