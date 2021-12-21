import sys

import pygame

pygame.init()

class Vana:

    def __init__(self, x, y):

        self.aken = pygame.display.set_mode([1024, 768])
        self.vana = pygame.image.load("vana.png")
        self.rect = self.vana.get_rect()
        self.kingid = pygame.image.load("kink.png")
        self.vana2 = pygame.image.load("vana2.png")
        self.lapskurb = pygame.image.load("lapskurb.png")
        self.lapsõnnelik = pygame.image.load("lapsõnnelik.png")
        self.halb = (0, 0, 0, 255)

        self.laps_x = 900
        self.laps_y = 650

        self.kingid_x = 50
        self.kingid_y = 50

        self.vana_x = x
        self.vana_y = y

        self.vana_x_p_liigub = 70
        self.vana_x_v_liigub = 70
        self.vana_y_ü_liigub = 70
        self.vana_y_a_liigub = 70

        self.tahab_liikuda_ü = False
        self.tahab_liikuda_a = False
        self.tahab_liikuda_p = False
        self.tahab_liikuda_v = False

        self.ü = False
        self.a = False
        self.v = False
        self.p = False

        self.võib_liikuda_ü = False
        self.võib_liikuda_a = False
        self.võib_liikuda_v = False
        self.võib_liikuda_p = False

        self.kink_käes = False
        self.lapselkink = False
        self.baas_kiirus = 50
        self.kell = pygame.time.Clock()
        self.dt = self.kell.tick() / 1000
        self.elab = True

        self.mäng_töötab = True

    def vana_liikumine(self):

        self.dt = self.kell.tick() / 100


        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.tahab_liikuda_ü = True

                if e.key == pygame.K_DOWN:
                    self.tahab_liikuda_a = True

                if e.key == pygame.K_LEFT:
                    self.tahab_liikuda_v = True
                if e.key == pygame.K_RIGHT:
                    self.tahab_liikuda_p = True
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.tahab_liikuda_ü = False
                if e.key == pygame.K_DOWN:
                    self.tahab_liikuda_a = False
                if e.key == pygame.K_LEFT:
                    self.tahab_liikuda_v = False
                if e.key == pygame.K_RIGHT:
                    self.tahab_liikuda_p = False

        self.vana_all_x = int(self.vana_x) + 29
        self.vana_all_y = int(self.vana_y) + 70
        self.vana_üleval_x = int(self.vana_x) + 29
        self.vana_üleval_y = int(self.vana_y) - 1
        self.vana_vasak_x = int(self.vana_x)
        self.vana_vasak_y = int(self.vana_y) + 28
        self.vana_parem_x = int(self.vana_x) + 70
        self.vana_parem_y = int(self.vana_y) + 28

        self.värv_üleval = self.aken.get_at((self.vana_üleval_x, self.vana_üleval_y))
        self.värv_all = self.aken.get_at((self.vana_all_x, self.vana_all_y))
        self.värv_vasak = self.aken.get_at((self.vana_vasak_x, self.vana_vasak_y))
        self.värv_parem = self.aken.get_at((self.vana_parem_x, self.vana_parem_y))
        print(self.tahab_liikuda_ü, self.tahab_liikuda_a, self.tahab_liikuda_v, self.tahab_liikuda_p)

        if self.värv_all == self.halb:

            self.a = True

        if self.värv_all != self.halb:

            self.a = False

        if self.tahab_liikuda_a == True and self.a == False:
            self.vana_y += self.vana_y_a_liigub * self.dt



        if self.värv_üleval == self.halb:

            self.ü = True

        if self.värv_üleval != self.halb:
            self.ü = False

        if self.tahab_liikuda_ü == True and self.ü == False:
            self.vana_y -= self.vana_y_ü_liigub * self.dt


        if self.värv_parem == self.halb:

            self.p = True

        if self.värv_parem != self.halb:
            self.p = False

        if self.tahab_liikuda_p == True and self.p == False:
            self.vana_x += self.vana_x_p_liigub * self.dt

        if self.värv_vasak == self.halb:

            self.v = True

        if self.värv_vasak != self.halb:
            self.v = False

        if self.tahab_liikuda_v == True and self.v == False:
            self.vana_x -= self.vana_x_v_liigub * self.dt

        if self.vana_x < 100 and self.vana_y < 100:
            self.kink_käes = True

        if self.vana_x > 880 and self.vana_y > 630 and self.kink_käes == True:
            self.lapselkink = True

