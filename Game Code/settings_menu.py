import pygame
from settings import *
from game_functions import draw_button
import json

def load_settings():
    try:
        with open('settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"music_volume": 50, "sounds_volume": 50, "notifications_on": True}
    
def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file)

def draw_slider(screen, x, y, width, height, value, color=(200, 200, 200), knob_color=(150, 150, 150)):
    # Slider track
    track_rect = pygame.Rect(x, y + height // 4, width, height // 2)
    pygame.draw.rect(screen, color, track_rect)

    # Slider knob
    knob_width = height  # Making the knob a square that fits in the slider height
    knob_x = x + (width - knob_width) * value  # Position based on value
    knob_rect = pygame.Rect(knob_x, y, knob_width, height)
    pygame.draw.rect(screen, knob_color, knob_rect)

    return track_rect, knob_rect

def draw_switch(screen, x, y, is_on, color_off=(200, 200, 200), color_on=(100, 200, 100)):
    width, height = 50, 20  # Dimensions for the switch
    switch_rect = pygame.Rect(x, y, width, height)
    # Background
    pygame.draw.rect(screen, color_off if not is_on else color_on, switch_rect)
    # Toggle
    toggle_radius = height // 2
    toggle_center = (x + toggle_radius if not is_on else x + width - toggle_radius, y + toggle_radius)
    pygame.draw.circle(screen, (255, 255, 255), toggle_center, toggle_radius - 2)  # Slightly smaller for a border effect
    return switch_rect


def update_slider_value(event, slider_rect, x, width):
    # Adjust calculation to consider the initial click position and the current mouse position
    relative_x = event.pos[0] - x
    new_value = max(0, min(relative_x / width, 1))  # Clamp between 0 and 1
    return new_value

def show_settings_menu(screen, font):
    running_settings = True
    settings = load_settings()
    music_volume = settings["music_volume"] / 100  # Convert to 0-1 range
    sounds_volume = settings["sounds_volume"] / 100
    notifications_on = settings["notifications_on"]
    dragging = None  # Keeps track of which slider is being dragged

    while running_settings:
        screen.fill(white)  # Or any background

        # Text labels 
        music_label_text = font.render("Music", True, black)
        sounds_label_text = font.render("Sounds", True, black)
        notification_label_text = font.render("Notifications", True, black)

        # Draw text labels to the left of sliders
        screen.blit(music_label_text, (50, 100 + music_label_text.get_height() // 2))
        screen.blit(sounds_label_text, (50, 150 + sounds_label_text.get_height() // 2))
        screen.blit(notification_label_text, (50, 200 + sounds_label_text.get_height() // 2))

        # Draw sliders for music and sounds
        music_track_rect, music_knob_rect = draw_slider(screen, 160, 112, 200, 30, music_volume)
        sounds_track_rect, sounds_knob_rect = draw_slider(screen, 160, 162, 200, 30, sounds_volume)

        # Slider value texts
        music_value_text = font.render(f"{int(music_volume * 100)}", True, black)
        sounds_value_text = font.render(f"{int(sounds_volume * 100)}", True, black)

        # Draw value texts to the right of sliders
        screen.blit(music_value_text, (365, 100 + music_value_text.get_height() // 2))
        screen.blit(sounds_value_text, (365, 150 + sounds_value_text.get_height() // 2))
        
        # Notifications switch
        notifications_switch_rect = draw_switch(screen, 245, 218, notifications_on)

        # Back button
        back_button_rect = draw_button(screen, button_color, screen_width - 110, screen_height - 60, 100, 40, "Back")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running_settings = False
                elif music_knob_rect.collidepoint(event.pos):  # Initial click on the knob
                    dragging = 'music'
                elif sounds_knob_rect.collidepoint(event.pos):  # Initial click on the knob
                    dragging = 'sounds'
                elif notifications_switch_rect.collidepoint(event.pos):
                    notifications_on = not notifications_on
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = None  # Stop dragging once the mouse button is released
            elif event.type == pygame.MOUSEMOTION:
                if dragging == 'music':
                    # Update music volume based on mouse x position, allowing drag anywhere
                    music_volume = update_slider_value(event, music_track_rect, 160, 200)
                elif dragging == 'sounds':
                    # Update sounds volume based on mouse x position, allowing drag anywhere
                    sounds_volume = update_slider_value(event, sounds_track_rect, 160, 200)

        # Outside the event loop, to ensure music_volume and sounds_volume stay within 0-1 range
        music_volume = max(0, min(music_volume, 1))
        sounds_volume = max(0, min(sounds_volume, 1))
        
        if not running_settings:
            settings_to_save = {
                "music_volume": int(music_volume * 100),
                "sounds_volume": int(sounds_volume * 100),
                "notifications_on": notifications_on
            }
            save_settings(settings_to_save)

        pygame.display.update()
