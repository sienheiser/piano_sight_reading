class Piano:
    '''
        This class builds a piano with 88 keys whose lowest note  is
        A0 and highest note is C8
    '''
    def __init__(self):
        self.keys = [i for i in range(1,89)]
        letters = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
        self.letters = ['A0','As0','B0']

        for i in range(1,8):
            for letter in letters:
                self.letters.append(letter+str(i))
        self.letters.append('C8')

        self.mapping = {i:self.letters[i-1] for i in range(1,89)}

    def numbers_to_letters(self,chord:tuple)->tuple:
        li2 = [self.mapping[i] for i in chord]
        return tuple(li2)
