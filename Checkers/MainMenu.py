import pygame
import sys

pygame.init()

window_size = (1000, 800)
screen = pygame.display.set_mode(window_size)
background_image = pygame.image.load("background.jpg")

font = pygame.font.Font(None, 36)

# colors (used the same as your colors we can change later)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# main menu
def main_menu():
    # buttons
    start_button = pygame.Rect(window_size[0] // 2 - 50, window_size[1] // 2 - 25, 100, 50)
    quit_button = pygame.Rect(window_size[0] // 2 - 50, window_size[1] // 2 + 50, 100, 50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(event.pos):
                        return True
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
        
        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the menu
        pygame.draw.rect(screen, red, start_button)
        start_text = font.render("Start", True, white)
        start_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rect)
        pygame.draw.rect(screen, red, quit_button)
        quit_text = font.render("Quit", True, white)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_rect)
        pygame.display.update()


main_menu()

