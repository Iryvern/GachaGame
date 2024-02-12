class Building:
    def __init__(self, name, size, color, position):
        self.name = name
        self.size = size  # Diameter of the building's circle representation
        self.color = color  # Default color of the building's circle
        self.position = position  # Position of the building as a tuple (x, y)
        self.hover_color = (0, 255, 0)  # Green color for hover effect

    def is_hovering(self, mouse_pos):
        """Check if the mouse is hovering over the building."""
        distance = ((mouse_pos[0] - self.position[0]) ** 2 + (mouse_pos[1] - self.position[1]) ** 2) ** 0.5
        return distance < self.size // 2

    def draw(self, screen, apply_hover_effect=True):
        """Draws the building as a circle on the given screen at its position, considering hover effect based on the given flag."""
        import pygame
        # Check for mouse hover to determine the color, only if apply_hover_effect is True
        mouse_pos = pygame.mouse.get_pos()
        if apply_hover_effect and self.is_hovering(mouse_pos):
            current_color = self.hover_color
        else:
            current_color = self.color

        # Draw the circle with the determined color
        pygame.draw.circle(screen, current_color, self.position, self.size // 2)

        # Render the name text
        font = pygame.font.SysFont(None, 24)
        text_surf = font.render(self.name, True, (255, 255, 255))  # White text color
        text_rect = text_surf.get_rect(center=self.position)
        screen.blit(text_surf, text_rect)
