import pygame
from popup import Popup
from game_functions import draw_button

def draw_popup_menu(screen, font):
    # Create a semi-transparent overlay
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))  # Dark overlay for contrast
    screen.blit(overlay, (0, 0))
    
    # Define button properties
    button_width, button_height = 200, 50
    button_color = (100, 100, 100)  # Dark grey
    button_hover_color = (150, 150, 150)  # Lighter grey for hover effect
    
    # Calculate button positions
    start_y = screen.get_height() // 2 - (3 * button_height + 2 * 10) // 2  # Vertically center buttons
    button_positions = ["Account", "Settings", "Quit"]
    
    buttons = []
    for i, btn_text in enumerate(button_positions):
        button_x = (screen.get_width() - button_width) // 2
        button_y = start_y + i * (button_height + 10)  # 10 pixels spacing between buttons
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        buttons.append((button_rect, btn_text))
    
    # Draw buttons
    for button_rect, btn_text in buttons:
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)
        # Button text
        text_surf = font.render(btn_text, True, (255, 255, 255))  # White text
        text_rect = text_surf.get_rect(center=button_rect.center)
        screen.blit(text_surf, text_rect)
    
    return buttons


def show_lobby(screen, font):
    running_lobby = True
    show_popup = False  # Initially, the popup is not shown.

    popup = Popup(screen, font, ["Account", "Settings", "Quit"], {
        "Account": lambda: print("Account details"),
        "Settings": lambda: print("Open settings"),
        "Quit": lambda: exit()
    })


    # Define the main menu button once outside the loop to avoid recreating it every frame.
    main_button_rect = pygame.Rect(screen.get_width() - 110, 10, 100, 40)  # Example position and size

    while running_lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_lobby = False
            
            # Handle clicking on the "Menu" button only if the popup is not currently shown.
            if not show_popup and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if main_button_rect.collidepoint(event.pos):
                    show_popup = True  # Show the popup

            # If the popup is shown, handle events within this block.
            if show_popup:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Assuming the draw_popup_menu returns buttons and handles drawing itself.
                    buttons = draw_popup_menu(screen, font)
                    clicked_button = None
                    for button_rect, btn_text in buttons:
                        if button_rect.collidepoint(event.pos):
                            clicked_button = btn_text
                            break  # Stop checking if we've found the clicked button.
                    
                    # Handle popup button actions here
                    if clicked_button:
                        print(f"{clicked_button} button clicked")
                        if clicked_button == "Quit":
                            running_lobby = False  # Example action for Quit
                        elif clicked_button == "Settings":
                            # Placeholder for opening settings - you might call show_settings_menu here
                            print("Open settings")
                        elif clicked_button == "Account":
                            # Placeholder for account actions
                            print("Account details")
                        # Hide the popup after any button is clicked for simplicity
                        show_popup = False

        screen.fill((255, 255, 255))  # Clear screen or draw the lobby background

        # Always draw the main "Menu" button, but only toggle the popup if it's not already shown.
        if not show_popup:
            draw_button(screen, (100, 100, 100), main_button_rect.x, main_button_rect.y, main_button_rect.width, main_button_rect.height, "Menu")


        # Draw the popup menu over everything else if it's active.
        if show_popup:
            popup.draw()

        pygame.display.flip()


