import pygame
import pygame_gui
import jouluvana
from jouluvana import Jouluvana

pygame.init()
import sys


# pygame.display.set_caption('Jõulumäng')
class Mang:

    def __init__(self):
        self.aken = pygame.display.set_mode([800, 600])
        self.manager = pygame_gui.UIManager([800, 600])
        self.aken.fill([255, 255, 255])
        self.background = pygame.image.load('lol.png')
        self.kell = pygame.time.Clock()
        self.mangTootab = True
        self.etapp = 'algus'
        self.joulukas = Jouluvana(100, 100)
        pygame.mixer.music.load("mingitaustamuusika.mp3")
        taustamuusika = pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)


        self.minemangu = pygame_gui.elements.UIButton(pygame.Rect((50, 150), (200, 70)), "Alusta mängu", self.manager)
        self.nuppseaded = pygame_gui.elements.UIButton(pygame.Rect((50, 250), (150, 50)), "Seaded", self.manager)
        self.mänguautorid = pygame_gui.elements.UIButton(pygame.Rect((50, 325), (150, 50)), "Mängu autorid", self.manager)
        self.panekinni = pygame_gui.elements.UIButton(pygame.Rect((50, 400), (150, 50)), "Mäng kinni", self.manager)
        self.seadedtagasi = pygame_gui.elements.UIButton(pygame.Rect((500, 400), (150, 50)), "Tagasi", self.manager)
        self.muusikaliugur = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((100, 100), (250, 40)), 50, (0, 99),
                                                                    self.manager)
        self.heliefektid = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((100, 300), (250, 40)), 50, (0, 99),
                                                                  self.manager)
        self.heliefektid.hide()
        self.muusikaliugur.hide()
        self.seadedtagasi.hide()

        pygame.display.flip()

    def kontrolli(self):
        while self.mangTootab:

            if self.etapp == 'algus':
                print('mäng algab, tuleb alguseaken')
                self.alusta()
                self.teeAlguseAken()
            elif self.etapp == 'seaded':
                self.alusta()
                self.seaded()
            elif self.etapp == "autorid":
                self.alusta()
                self.autorid()

            elif self.etapp == 'mang_kaib':
                print('mäng algab, tuleb mänguaken')
                self.teeManguAken()
                self.joulukas.kuva_pilt_ekraanile(self.aken)
                self.mangi()
            elif self.etapp == 'mang_on_labi':
                print('nüüd sai mäng läbi, tuleb lõpuaken')
                self.teeLopuAken()
            else:
                print('muu värk')
            pygame.display.update()
            # self.kell.tick(0.1)
            print(self.kell)
        pygame.quit()
        sys.exit()

    def alusta(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.mangTootab = False
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.etapp = 'mang_kaib'
                print('vajutasid tühikut, etapp mang_kaib hakkas tööle')

            elif e.type == pygame.USEREVENT:
                if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if e.ui_element == self.minemangu:
                        print("alustasid mängu jhjhjhjhk")
                        self.etapp = 'mang_kaib'
                    if e.ui_element == self.nuppseaded:
                        print("seaded")
                        self.etapp = 'seaded'
                    if e.ui_element == self.mänguautorid:
                        print("Autorid")
                        self.etapp = "autorid"
                    if e.ui_element == self.panekinni:
                        pygame.quit()
                    if e.ui_element == self.seadedtagasi:
                        self.etapp = 'algus'
                if e.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if e.ui_element == self.muusikaliugur:
                        pygame.mixer.music.set_volume(e.value / 100)

            self.manager.process_events(e)

    def mangi(self):
        # jouluvana.votaVana()
        print('mängi ja mängi ja mängi')
        # self.joulukas.kuva_pilt_ekraanile(self.aken)
        # self.joulukas.juhi_nooltega()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.mangTootab = False
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.joulukas.rect.y = self.joulukas.rect.y - self.joulukas.samm
                elif e.key == pygame.K_DOWN:
                    self.joulukas.rect.y = self.joulukas.rect.y + self.joulukas.samm
                elif e.key == pygame.K_LEFT:
                    self.joulukas.rect.x = self.joulukas.rect.x - self.joulukas.samm
                elif e.key == pygame.K_RIGHT:
                    self.joulukas.rect.x = self.joulukas.rect.x + self.joulukas.samm

    def teeAlguseAken(self):
        #self.manager = pygame_gui.UIManager([800, 600])
        #self.minemangu = pygame_gui.elements.UIButton(pygame.Rect((50, 150), (200, 70)), "Alusta mängu", self.manager)
       #self.seaded = pygame_gui.elements.UIButton(pygame.Rect((50, 250), (150, 50)), "Seaded", self.manager)
        #self.mänguautorid = pygame_gui.elements.UIButton(pygame.Rect((50, 325), (150, 50)), "Mängu autorid", self.manager)
        #self.panekinni = pygame_gui.elements.UIButton(pygame.Rect((50, 400), (150, 50)), "Mäng kinni", self.manager)
        self.menüü_pilt = pygame.image.load("menüü.png")
        self.minemangu.show()
        self.nuppseaded.show()
        self.mänguautorid.show()
        self.panekinni.show()
        self.heliefektid.hide()
        self.muusikaliugur.hide()
        self.seadedtagasi.hide()
        self.aken.blit(self.menüü_pilt, (0, 0))
        self.manager.update(0.1)
        self.manager.draw_ui(self.aken)
        pygame.display.update()

    def seaded(self):

        self.seaded_taust = pygame.image.load("seaded.png")
        self.minemangu.hide()
        self.nuppseaded.hide()
        self.mänguautorid.hide()
        self.panekinni.hide()
        self.heliefektid.show()
        self.muusikaliugur.show()
        self.seadedtagasi.show()
        self.aken.blit(self.seaded_taust, (0, 0))
        self.manager.update(0.1)
        self.manager.draw_ui(self.aken)
        pygame.display.update()

    def autorid(self):

        self.autorid_taust = pygame.image.load("autorid.png")
        self.aken.blit(self.autorid_taust, (0, 0))
        self.minemangu.hide()
        self.nuppseaded.hide()
        self.mänguautorid.hide()
        self.panekinni.hide()
        self.seadedtagasi.show()
        self.manager.update(0.1)
        self.manager.draw_ui(self.aken)
        pygame.display.update()

    def teeManguAken(self):
        self.background = pygame.image.load('lol.png')
        self.aken.blit(self.background, (0, 0))
        print('teeb mänguakna taustapildiga')
        # pygame.display.update()

    def teeLopuAken(self):
        self.aken.fill([255, 0, 0])
        print('värvib lõpuakna punaseks')
        # pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
