import pygame

class SelectMenu:
    def __init__(self, screen, options):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)
        self.options = options  # List of option names (strings)
        self.buttons = []
        self.active = True  # Indicates if the menu is currently shown
        self.padding = 10  # Padding around buttons
        self.setup_menu()
        self.overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 220))  # Semi-transparent overlay for dark filter

    def setup_menu(self):
        menu_width, menu_height = 300, (50 + self.padding * 2) * len(self.options) + self.padding * 2
        self.menu_rect = pygame.Rect(
            (self.screen.get_width() - menu_width) // 2,
            (self.screen.get_height() - menu_height) // 2,
            menu_width,
            menu_height
        )
        
        # Position the close button at the top right corner of the menu
        self.close_button_rect = pygame.Rect(
            self.menu_rect.right - 30,
            self.menu_rect.top - 10,
            20,
            20
        )
        
        # Initialize buttons
        self.setup_buttons()
    
    def setup_buttons(self):
        button_height = 50
        for index, option in enumerate(self.options):
            button_rect = pygame.Rect(
                self.menu_rect.x + self.padding,
                self.menu_rect.y + self.padding * 2 + index * (button_height + self.padding * 2),
                self.menu_rect.width - self.padding * 2,
                button_height
            )
            self.buttons.append((button_rect, option))

    def draw(self):
        if not self.active:
            return

        # Draw the semi-transparent overlay for dark filter
        self.screen.blit(self.overlay, (0, 0))

        # Draw the menu background
        pygame.draw.rect(self.screen, (200, 200, 200), self.menu_rect)

        # Draw buttons with hover effect
        mouse_pos = pygame.mouse.get_pos()
        for button_rect, option in self.buttons:
            button_color = (100, 100, 100) if button_rect.collidepoint(mouse_pos) else (160, 160, 160)
            pygame.draw.rect(self.screen, button_color, button_rect)
            text_surf = self.font.render(option, True, (0, 0, 0))  # Black text color
            text_rect = text_surf.get_rect(center=button_rect.center)
            self.screen.blit(text_surf, text_rect)
        
        # Draw the close button
        close_button_color = (255, 0, 0) if self.close_button_rect.collidepoint(mouse_pos) else (200, 0, 0)
        pygame.draw.rect(self.screen, close_button_color, self.close_button_rect)
        close_text_surf = self.font.render("X", True, (255, 255, 255))  # White text for "X"
        close_text_rect = close_text_surf.get_rect(center=self.close_button_rect.center)
        self.screen.blit(close_text_surf, close_text_rect)

    def handle_event(self, event):
        if not self.active:
            return False
        
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.close_button_rect.collidepoint(mouse_pos):
                self.active = False
                return True
            
            for button_rect, option in self.buttons:
                if button_rect.collidepoint(mouse_pos):
                    print(f"{option} was clicked")
                    # Trigger action here but do not deactivate the menu
                    return True  # Return True to indicate the event was handled
                    
        return False  # Return False if the event was not handled

    
    def toggle(self):
        self.active = not self.active