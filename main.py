import pygame
from Checkers.constants import *
from Checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Checkers')

def convert(x,y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    selected = False
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not selected:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        row, col = convert(mouse_x,mouse_y)
                        if board.select(row,col):
                            selected = True

            elif selected:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            row, col = convert(mouse_x,mouse_y)
                            board.move(row,col)
                            selected = False
            

        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()