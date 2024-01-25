import pygame
from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
import time

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
playing = False

# Define a variable to keep track of the key state
key_pressed = False

# Define a callback function for key press
def on_press(key):
    global key_pressed
    if key == keyboard.Key.space:
        key_pressed = not key_pressed

# Start the keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if key_pressed:
        Controller().click(Button.left)
        time.sleep(1)
        print("Clicked")

    pygame.display.flip()
    clock.tick(60)