import pygame
import sys
from SelectMenu import SelectMenu
from Building import Building  # Assuming Building class exists

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Lobby")
font = pygame.font.SysFont(None, 30)

# Example buildings with callback to show SelectMenu
buildings = [
    Building("Summon", 100, (128, 128, 128), (400, 160)),
    Building("Residence", 100, (128, 128, 128), (520, 250))
]

running = True
select_menu_active = False
select_menu = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Only process SelectMenu events when active
        if select_menu_active:
            if select_menu.handle_event(event):
                select_menu_active = False  # Close the menu after a selection
        else:
            # Handle clicks only when SelectMenu is not active
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                for building in buildings:
                    if building.is_hovering(pygame.mouse.get_pos()):
                        # Define options based on the building clicked
                        options = ["Option 1", "Option 2", "Option 3"]
                        select_menu = SelectMenu(screen, options)
                        select_menu_active = True

    screen.fill((255, 255, 255))  # Clear screen or draw the lobby background

    # Always draw buildings and other lobby elements, regardless of SelectMenu's state
    circle_radius = min(screen_width, screen_height) * 2 // 3 // 2
    circle_center = (screen_width // 2, screen_height // 2)
    pygame.draw.circle(screen, (192, 192, 192), circle_center, circle_radius)

    for building in buildings:
        building.draw(screen, not select_menu_active)

    # Draw and handle the SelectMenu if active
    if select_menu_active:
        select_menu.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
