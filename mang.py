import sys

import pygame

pygame.init()


# pygame.display.set_caption('Jõulumäng')
class Mang:

    def __init__(self):
        self.aken = pygame.display.set_mode([800, 600])
        self.aken.fill([255, 255, 255])
        self.background = pygame.image.load('lol.png')
        self.kell = pygame.time.Clock()
        self.mangTootab = True
        self.etapp = 'algus'
        pygame.display.flip()

    def kontrolli(self):
        while self.mangTootab:

            if self.etapp == 'algus':
                print('mäng algab, tuleb alguseaken')
                self.alusta()
                self.teeAlguseAken()
            elif self.etapp == 'mang_kaib':
                print('mäng algab, tuleb mänguaken')
                self.teeManguAken()
                self.mangi()
                self.lopeta()
            elif self.etapp == 'mang_on_labi':
                print('nüüd sai mäng läbi, tuleb lõpuaken')
                self.teeLopuAken()
            else:
                print('muu värk')
            pygame.display.update()
            #self.kell.tick(0.1)
            print(self.kell)
        #pygame.quit()
        sys.exit()

    def alusta(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.mangTootab = False
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.etapp = 'mang_kaib'
                print('vajutasid tühikut, etapp mang_kaib hakkas tööle')

    def mangi(self):
        print('mängi ja mängi ja mängi')


    def lopeta (self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.mangTootab = False
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.etapp = 'mang_on_labi'
                print('vajutasid esc, etapp mang_on_labi hakkas tööle')

    def teeAlguseAken(self):
        self.aken.fill([255, 255, 0])
        print('värvib alguseakna kollaseks')
        pygame.display.update()

    def teeManguAken(self):
        self.background = pygame.image.load('lol.png')
        self.aken.blit(self.background, (0, 0))
        print('teeb mänguakna taustapildiga')
        # pygame.display.update()

    def teeLopuAken(self):
        self.aken.fill([255, 0, 0])
        print('värvib lõpuakna punaseks')
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()


