import pygame
import sys
from kmp import KnuthMorrisPratt
from collections import OrderedDict

file = "./test.wav"

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()

play_sound()
pygame.init()

pygame.display.set_mode((100, 100))

keypresses = []
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
        if event.type == pygame.USEREVENT:
            play_sound()
        if event.type == pygame.KEYDOWN:
            codez = list(OrderedDict.fromkeys(unlock_code))
            for c in codez:
                if event.key == c:
                    keypresses.append(c)

            for s in KnuthMorrisPratt(keypresses, unlock_code):
                sys.exit()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

