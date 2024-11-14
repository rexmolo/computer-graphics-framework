import pygame
from pygame.examples.sprite_texture import event


class Input(object) :

    def __init__(self):
        self.quit = False

    def update(self):
        if event.type == pygame.QUIT:
            self.quit = True