import pygame
from settings import *

def draw_button(screen, color, x, y, width, height, text):
    # Create font object here
    font = pygame.font.SysFont(font_name, font_size)
    button_rect = pygame.Rect(x, y, width, height)
    mouse_pos = pygame.mouse.get_pos()

    # Darken the color if the mouse is hovering over the button
    original_color = color
    if button_rect.collidepoint(mouse_pos):
        # Darken each color component by 20% as an example
        darken_factor = 0.5
        color = tuple(max(0, int(c * darken_factor)) for c in original_color)
    
    pygame.draw.rect(screen, color, button_rect)
    text_img = font.render(text, True, black)
    screen.blit(text_img, (x + (width - text_img.get_width()) / 2, y + (height - text_img.get_height()) / 2))

    return button_rect


def handle_events(screen, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            for button in buttons:
                if button['rect'].collidepoint(pygame.mouse.get_pos()):
                    return button['action']
        
    return None
