import pygame

class Popup:
    def __init__(self, screen, font, button_texts, action_callbacks):
        self.screen = screen
        self.font = font
        self.button_texts = button_texts
        self.action_callbacks = action_callbacks
        self.buttons = []
        self.active = False
        
        self.overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 200))  # Semi-transparent overlay
        
        self.setup_buttons()
    
    def setup_buttons(self):
        button_width, button_height = 200, 50
        start_y = self.screen.get_height() // 2 - (len(self.button_texts) * button_height + (len(self.button_texts) - 1) * 10) // 2
        
        for i, btn_text in enumerate(self.button_texts):
            button_x = (self.screen.get_width() - button_width) // 2
            button_y = start_y + i * (button_height + 10)
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            self.buttons.append((button_rect, btn_text))
    
    def draw(self):
        if not self.active:
            return
        
        self.screen.blit(self.overlay, (0, 0))
        
        for button_rect, btn_text in self.buttons:
            mouse_pos = pygame.mouse.get_pos()
            button_color = (100, 100, 100) if not button_rect.collidepoint(mouse_pos) else (150, 150, 150)
            
            pygame.draw.rect(self.screen, button_color, button_rect)
            text_surf = self.font.render(btn_text, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=button_rect.center)
            self.screen.blit(text_surf, text_rect)
    
    def handle_event(self, event):
        if not self.active or event.type != pygame.MOUSEBUTTONDOWN:
            return False
        
        for button_rect, btn_text in self.buttons:
            if button_rect.collidepoint(event.pos):
                callback = self.action_callbacks.get(btn_text)
                if callback:
                    callback()
                return True
        return False
    
    def toggle(self):
        self.active = not self.active
