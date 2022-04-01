from unicodedata import name
from coin import Coin
from player import Player

class Game:
    def __init__(self) -> None:
        print('Witaj w grze Orzeł czy Reszka')
        self.name = input('Podaj swoje imie:')

    user = Player(name, 0)
    computer = Player('Komputer', 0)



