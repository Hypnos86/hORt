import random

class Coin:
    SIDE = {'o':'Orzeł', 'r':'Reszka'}
    def __init__(self, side) -> None:
        if side not in self.SIDE:
            raise ValueError('Niepoprawny wybór')
        self.side = self.SIDE[side]
    
    def throw(self):
        self.side = random.choice(list(self.SIDE.values()))

    def __repr__(self) -> str:
        return f'{self.side}'

coin = Coin("o")
coin.throw()
print(coin)
