from interaction import welcome_msg
from classifier import classify

class Game:
    def __init__(self):
        welcome_msg()
        classify()

instance = Game()
