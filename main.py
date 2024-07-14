from Chords import Chord
from lesson import inversion
from database_model import engine, Session
from database_scripts import get_next_lesson,update_note,update_lesson
import random
import time 

session = Session(engine)
num_chords = len(inversion)

if __name__ == "__main__":
    next_lesson = get_next_lesson(session)

    update_lesson(session,next_lesson,num_chords)

    #Block for adding individual note data to database
    for i in range(1):
        start_time = time.time()
        time.sleep(2.3)
        end_time = time.time()
        chord = inversion[i]
        for note in chord:
            update_note(session,note,next_lesson,end_time-start_time)

    print(inversion)
    



