import pygame
import sys
from kmp import KnuthMorrisPratt
from collections import OrderedDict

file = "./test.wav"

pygame.mixer.init()

# put this in a func for loopback later
def play_sound():
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()

play_sound()
pygame.init()

# add a window so we have something to "escape" out of
pygame.display.set_mode((100, 100))

# tracks all keypresses that are in unlock code
keypresses = []
# in this case our unlock code is '1337'
unlock_code = [
            pygame.K_1,
            pygame.K_3,
            pygame.K_3,
            pygame.K_7
        ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # loop sound
        if event.type == pygame.USEREVENT:
            play_sound()
        # check if key pressed is in unlock code
        if event.type == pygame.KEYDOWN:
            codez = list(OrderedDict.fromkeys(unlock_code))
            for c in codez:
                if event.key == c:
                    keypresses.append(c)

            # this algo finds sequences in lists, exits upon finding code
            for s in KnuthMorrisPratt(keypresses, unlock_code):
                sys.exit()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

