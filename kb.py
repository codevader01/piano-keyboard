import pygame
import keyboard  # This library allows capturing keyboard events even when the program is in the background
import random
# Initialize pygame
pygame.init()

# Load the sound file
sound = pygame.mixer.Sound('wav/beep.wav')
sound1 = pygame.mixer.Sound('wav/beepa.wav')
sound2 = pygame.mixer.Sound('wav/beepb1.wav')
sound3 = pygame.mixer.Sound('wav/beepc1.wav')
sound4 = pygame.mixer.Sound('wav/beepc1s.wav')
sound5 = pygame.mixer.Sound('wav/beepd1.wav')
sound6 = pygame.mixer.Sound('wav/beepd1s.wav')
sound7 = pygame.mixer.Sound('wav/beepe1.wav') 
sound8 = pygame.mixer.Sound('wav/beepf1.wav')
sound9 = pygame.mixer.Sound('wav/beepg1.wav')
sound10 = pygame.mixer.Sound('wav/beepg1s.wav')

sounds = [sound,sound1,sound2,sound3,sound4,sound5,sound6,sound7,sound8,sound9,sound10]

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Keyboard Sound Player")

# Function to play sound on key press csdsd,msk
def play_sound(event):
    random.choice(sounds).play().set_volume(0.5)
    
# Set up the keyboard hook
keyboard.on_press(play_sound)

# Run the loop until the user quits
try:
    print("Press ESC to stop")
    keyboard.wait('esc')  # The script will run until you press the ESC key
except KeyboardInterrupt:
    pass

# Quit pygame
pygame.quit()
 