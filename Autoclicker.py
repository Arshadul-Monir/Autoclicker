import pygame
from pynput import keyboard
from pynput.mouse import Button, Controller
import time

# Initialize GUI
screen = pygame.display.set_mode((500, 500))

# Global toggler variable
playing = False

# Function to compare keypress with hotkey and toggles if matches
def toggle(key):
    global playing
    if key == keyboard.Key.space:
        playing = not playing

# Starts key listener
keyboard_listener = keyboard.Listener(on_press=toggle)
keyboard_listener.start()

# Main loop
while True:
    # Closing program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Continues clicking while global variable is set to true
    if playing:
        Controller().click(Button.left)
        time.sleep(1)
        print("Clicked")
    
    # Updates display
    pygame.display.flip()
