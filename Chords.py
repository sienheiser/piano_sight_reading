import random
import numpy as np

class Chord:
    '''
        This class builds chord using the root_note and pattern list.
        The pattern list contains the number of semitones from the root
        each additional key in a chord is. Example the major pattern is
        [4,7]. A minor pattern is [3,7].

        This class also builds all the possible inversions of the chord.
        '''
    def __init__(self,root_note:int,pattern:list):
        self.root_chord = []
        self.root_chord.append(root_note)

        for semitones in pattern:
            self.root_chord.append(root_note+semitones)

        self.variations = [np.array(self.root_chord)]

        inversion = np.array(self.root_chord)
        for i in range(len(pattern)):
            inversion[0] = inversion[0] + 12
            inversion = np.roll(inversion,-1)
            self.variations.append(inversion)

    def rng_variation(self) -> np.array:
        return random.choice(self.variations)




    



