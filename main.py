import pygame
from Checkers.constants import Width, Height
from Checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board.getPieceCoordinates(mouse_x,mouse_y)


        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()