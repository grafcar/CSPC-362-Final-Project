from Checkers.board import *
from Checkers.constants import *
from Checkers.main_game import *

class Game():
    def __init__(self):
        self.turn = 0
        self.x = 0
        self.y = 0
        self.main = Main_Game()

    def game_state(self,state):
        if state == 1:
            print("MAIN GAME IS GETTING CALLED")
            self.main_game()
        elif state == 2:
            print("waiting for state")
        elif state == 3:
            print("SELECTED BEFORE CHANGE",self.main.selected)
            self.main.selected = False
        else:
            print("stateless")
        
    def get_mouse_location(self,x,y):
        self.x = x
        self.y = y

    def menu(self):
        pass

    def main_game(self):
        self.main.select(self.x,self.y)
        self.main.move(self.x,self.y)
        self.main.draw()

    def quit(self):
        pass