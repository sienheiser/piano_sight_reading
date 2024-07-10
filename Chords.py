import numpy as np
notes = [i for i in range(13)]
class MajorTriad:
    def __init__(self,root_note:int):
        self.triad = np.array([root_note,root_note+4,root_note+7])
        self.fst_inversion = np.array([root_note+4,root_note+7,root_note+12])
        self.snd_inversion = np.array([root_note+7,root_note+12,root_note+16])

    def __repr__(self):
        return f"{self.triad}"

class MinorTriad:
    def __init(self,root_note:int):
        self.triad = np.array([root_note,root_note+3,root_note+7])
        self.fst_inversion = np.array([root_note+3,root_note+7,root_note+12])
        self.snd_inversion = np.array([root_note+7,root_note+12,root_note+15])


