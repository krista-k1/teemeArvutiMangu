import sys

import pygame

pygame.init()


# from mang import *

class Jouluvana(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('vana.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.samm = 100

    def kuva_pilt_ekraanile(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.flip()






