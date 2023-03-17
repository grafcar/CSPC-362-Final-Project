import pygame
from Checkers.constants import *
from Checkers.board import Board
from Checkers.game import Game


pygame.display.set_caption('Checkers')

# clock = pygame.time.Clock()

def convert(x,y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def menu():
    background_color = (255,112,112)
    WIN.fill(background_color)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()
    dot_x = 20
    dot_y = 20
    background_color = (255,112,112)
    
    #game.game_state(2)
    #menu()
    while run:
        clock.tick(FPS)
        
        dot_x += 5
        dot_y += 5
        # if dot_x // dot_y == 5:
        #     dot_y += 5
        WIN.fill(background_color)
        pygame.draw.circle(WIN,White,(dot_x,dot_y),20)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # if not selected:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    row, col = convert(mouse_x,mouse_y)
                    # game.get_mouse_location(row,col)
                    # game.game_state(1)
                # if pygame.mouse.get_pressed()[2]:
                    # game.game_state(3)
                    # print("HELLO")
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