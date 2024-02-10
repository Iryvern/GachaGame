import pygame
from game_functions import draw_button

def show_lobby(screen, font):
    running_lobby = True
    circle_color = (0, 120, 255)  # A blue color for the circle
    button_color = (200, 200, 200)  # A grey color for the button

    # Define the button position and size
    button_width, button_height = 100, 40
    button_x = screen.get_width() - button_width - 10  # 10 pixels from the right edge
    button_y = 10  # 10 pixels from the top edge

    while running_lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_lobby = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the button is clicked
                if button_x < event.pos[0] < button_x + button_width and button_y < event.pos[1] < button_y + button_height:
                    print("Button in lobby clicked!")  # Placeholder action

        screen.fill((255, 255, 255))  # Fill the screen with white

        # Draw the circle in the center of the screen
        pygame.draw.circle(screen, circle_color, (screen.get_width() // 2, screen.get_height() // 2), 50)
        draw_button(screen, button_color, button_x, button_y, button_width, button_height, 'All')

        pygame.display.flip()
