from Chords import Chord
from lesson import inversion
from database_model import engine, Session
from database_scripts import get_next_lesson,update_note,update_lesson
import random
import time 

session = Session(engine)
num_chords = len(inversion)

def check_input(input_chord:list,displayed_chord:list) -> bool:
    correct = True
    for i in range(len(user_input)):
        if chord[i] != int(user_input[i]):
            correct = False
    return correct

if __name__ == "__main__":
    next_lesson = get_next_lesson(session)
    update_lesson(session,next_lesson,num_chords)

    #Block for adding individual note data to database
    i = 0
    while i < 1:
        chord = inversion[i]
        start_time = time.time()
        user_input = input(f"chord {chord}: " ).split(" ")
        end_time = time.time()

        correct = check_input(user_input,chord)
        if correct:
            i = i+1
            for note in chord:
                update_note(session,note,next_lesson,end_time-start_time)
        else:
            pass


    #print(inversion)
    



