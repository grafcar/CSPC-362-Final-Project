import pygame
import time
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
                if pygame.mouse.get_pressed()[0]:
                    #time.sleep(0.1)
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    selection = board.selection(mouse_y,mouse_x)
                    if board.valid_selection(mouse_y,mouse_x): 
                        print("selection was valid, inside the while loop")               
                        while not pygame.mouse.get_pressed()[2]:
                            pygame.event.clear()
                            pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                            pygame.event.wait()
                            if pygame.mouse.get_pressed()[0]:                            
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                print("Press right mouse to exit")
                                board.move(mouse_y,mouse_x,selection)
                                break
                        print("Out of loop")
                #print("out of all ifs")
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()