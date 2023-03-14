import pygame
from Checkers.constants import *
from Checkers.board import Board
from Checkers.game import Game


pygame.display.set_caption('Checkers')

def convert(x,y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game()
    #game.game_state(2)
    selected = False
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # if not selected:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    row, col = convert(mouse_x,mouse_y)
                    game.get_mouse_location(row,col)
                    game.game_state(1)
                if pygame.mouse.get_pressed()[2]:
                    game.game_state(3)
                    print("HELLO")
                    # if main_game.select(row,col):
                    #     selected = True
                    # if board.select(row,col):
                    #     selected = True

            # elif selected:
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             if pygame.mouse.get_pressed()[0]:
            #                 row, col = convert(mouse_x,mouse_y)
            #                 # board.move(row,col)
            #                 main_game.move(row,col)
            #                 selected = False
            

        #board.draw(WIN)
        #game.game_state(2)
        
        pygame.display.update()
    pygame.quit()

main()