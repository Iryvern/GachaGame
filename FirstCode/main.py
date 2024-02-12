import pygame
import sys
from settings import *
from game_functions import draw_button, handle_events
from old_popup import show_popup_confirm
from settings_menu import show_settings_menu
from lobby import show_lobby

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Welcome Screen')
    font = pygame.font.SysFont(font_name, font_size)

    buttons = [
        {'rect': pygame.Rect((screen_width - button_width) / 2, 150, button_width, button_height), 'action': 'start', 'label': 'Start'},
        {'rect': pygame.Rect((screen_width - button_width) / 2, 220, button_width, button_height), 'action': 'options', 'label': 'Options'},
        {'rect': pygame.Rect((screen_width - button_width) / 2, 290, button_width, button_height), 'action': 'quit', 'label': 'Quit'}
    ]

    running = True
    while running:
        screen.fill(white)
        welcome_text = font.render('Welcome to the Pygame App', True, black)
        screen.blit(welcome_text, ((screen_width - welcome_text.get_width()) / 2, 50))

        for button in buttons:
            draw_button(screen, button_color, button['rect'].x, button['rect'].y, button['rect'].width, button['rect'].height, button['label'])
        
        # Inside your main game loop in main.py
        font = pygame.font.SysFont(font_name, font_size)  # Ensure this is defined at the start of your main function
        action = handle_events(screen, buttons)

        if action == 'start':
            show_lobby(screen, font)

        if action == 'quit':
            confirm_action = show_popup_confirm(screen, font)
            if confirm_action == 'quit':
                running = False
            elif confirm_action == 'continue':
                # Just continue the game, the popup will be closed by the function
                continue

        if action == 'options':
            current_screen_content = screen.copy()
            show_settings_menu(screen, font, current_screen_content)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
