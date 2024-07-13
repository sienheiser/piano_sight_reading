from Chords import Chord
from Piano import Piano
import random
import sqlite3
import time 

database = "test2.db"
con = sqlite3.connect(database)

random.seed(10)
root_notes = [i for i in range(28, 36)]
maj_pattern = [4,7]

chords = [Chord(random.choice(root_notes),maj_pattern) for _ in range(len(root_notes))]

inversion = [chord.variations[random.choice([0,1,2])] for chord in chords]
num_chords = len(inversion)

def update_note(connection:sqlite3.connect, note: int, lesson_ID: int, press_time: float)->None:
    cur = connection.cursor()
    if note < 10:
        table_name = f"K0{note}"
    else:
        table_name = f"K{note}"
    sql = f"INSERT INTO {table_name} VALUES ({lesson_ID},{press_time})"
    cur.execute(sql)
    connection.commit()
    return None

if __name__ == "__main__":
    lesson_ID = 1
    for i in range(1):
        start_time = time.time()
        time.sleep(2.3)
        end_time = time.time()
        chord = inversion[i]
        for note in chord:
            update_note(con,note,lesson_ID,end_time-start_time)

    print(chords)



