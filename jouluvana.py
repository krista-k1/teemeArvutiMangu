import pygame
pygame.init()
# from mang import *

class Jouluvana:
    def __init__(self, asukoht):
        self.alguskoht = [asukoht.x, asukoht.y]
        self.x = asukoht.x
        self.y = asukoht.y
        self.suund = 'paremale'
        self.vana = pygame.image.load("vana.png")
        pygame.display.update()

    def votaVana(self):

        #vana.get_rect()
        #self.aken.blit(vana, (0, 0))
        print('teeb jõuluvana pildi')

    votaVana()