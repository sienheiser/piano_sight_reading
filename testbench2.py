import numpy as np
notes = [i for i in range(13)]
class MajorTriad:
    def __init__(self,root_note:int):
        self.triad = np.array([root_note,root_note+4,root_note+4+3])
        self.fst_inversion = np.array([root_note+4,root_note+7,root_note+12])
        self.snd_inversion = np.array([root_note+7,root_note+12,root_note+19])

    def __repr__(self):
        return f"{self.triad}"

c_maj = MajorTriad(1)
print(c_maj.snd_inversion)
