import time
class Lesson:
    def __init__(self,display_notes,display_time,pressed_notes,pressed_time):
        self.display_notes = display_notes
        self.display_time = display_time
        self.pressed_notes = pressed_notes
        self.pressed_time = pressed_time




if __name__ == "__main__":
    display_time = time.time()
    display_notes = ['C','E','G']
    data = []
    for note in display_notes:
        start_time = time.time()
        pressed_note = input(f"Press note {note}: ")
        stop_time = time.time()
        data.append((note,start_time,pressed_note,stop_time-start_time))
    print(data)


