import random

class Coin:
    SIDE = {'o':'Orzeł', 'r':'Reszka'}
    def __init__(self, side) -> None:
        if side not in self.SIDE:
            raise ValueError('Niepoprawny wybór')
        self.side = self.SIDE[side]
    
def throw(self):
    random.choice(self.side)

    def __repr__(self) -> str:
        return f'{self.side}'
