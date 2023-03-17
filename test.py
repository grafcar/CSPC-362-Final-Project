import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Move the Circle")

# Set up the circle
CIRCLE_RADIUS = 20
circle_x = WINDOW_WIDTH // 2  # start at the center of the window
circle_y = WINDOW_HEIGHT // 2
circle_color = pygame.Color("red")

# Set up the clock
clock = pygame.time.Clock()

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()

    # Update the circle position
    circle_x += 5  # move the circle to the right
    if circle_x > WINDOW_WIDTH + CIRCLE_RADIUS:
        circle_x = -CIRCLE_RADIUS  # start again from the left

    # Draw the circle and update the screen
    window.fill(pygame.Color("white"))
    pygame.draw.circle(window, circle_color, (circle_x, circle_y), CIRCLE_RADIUS)
    pygame.display.update()

    # Tick the clock
    clock.tick(60)
