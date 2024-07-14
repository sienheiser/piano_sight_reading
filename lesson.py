import random
from Chords import Chord
random.seed(10)
root_notes = [i for i in range(28, 36)]
maj_pattern = [4,7]

chords = [Chord(random.choice(root_notes),maj_pattern) for _ in range(len(root_notes))]

inversion = [chord.variations[random.choice([0,1,2])] for chord in chords]
