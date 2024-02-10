import pygame
from settings import *
from game_functions import draw_button

def show_popup_confirm(screen, font):
    # Create a semi-transparent overlay
    overlay = pygame.Surface((screen_width, screen_height))
    overlay.fill(black)
    overlay.set_alpha(180)  # Adjust transparency
    screen.blit(overlay, (0, 0))

    # Popup message
    message = "Are you sure you want to quit?"
    message_x = (screen_width - font.size(message)[0]) / 2
    message_y = (screen_height / 2) - 50

    # Define buttons
    yes_button_rect = pygame.Rect((screen_width / 2 - 105), (screen_height / 2), 100, 40)
    no_button_rect = pygame.Rect((screen_width / 2 + 5), (screen_height / 2), 100, 40)

    running_popup = True
    while running_popup:
        # Redraw overlay to prevent button ghosting
        screen.blit(overlay, (0, 0))
        # Redraw message
        text_img = font.render(message, True, white)
        screen.blit(text_img, (message_x, message_y))

        # Draw buttons with hover effect
        draw_button(screen, button_color, yes_button_rect.x, yes_button_rect.y, yes_button_rect.width, yes_button_rect.height, "Yes")
        draw_button(screen, button_color, no_button_rect.x, no_button_rect.y, no_button_rect.width, no_button_rect.height, "No")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_popup = False
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button_rect.collidepoint(pygame.mouse.get_pos()):
                    running_popup = False
                    return 'quit'
                elif no_button_rect.collidepoint(pygame.mouse.get_pos()):
                    running_popup = False
                    return 'continue'

        pygame.display.update()

