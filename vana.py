import sys

import pygame

pygame.init()


class Vana:

    def __init__(self, x, y):

        self.aken = pygame.display.set_mode([1024, 768])
        self.vana = pygame.image.load("vana.png")
        self.rect = self.vana.get_rect()

        self.halb = (0, 0, 0, 255)

        self.vana_x = x
        self.vana_y = y

        self.vana_x_p_liigub = 0
        self.vana_x_v_liigub = 0
        self.vana_y_ü_liigub = 0
        self.vana_y_a_liigub = 0

        self.ü = False
        self.a = False
        self.v = False
        self.p = False

        self.võib_liikuda_ü = False
        self.võib_liikuda_a = False
        self.võib_liikuda_v = False
        self.võib_liikuda_p = False

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
                    self.vana_y_ü_liigub += -self.baas_kiirus
                    self.võib_liikuda_ü = True
                    print(self.võib_liikuda_ü)
                if e.key == pygame.K_DOWN:
                    self.vana_y_a_liigub += self.baas_kiirus
                    self.võib_liikuda_a = True
                    print(self.võib_liikuda_a)
                if e.key == pygame.K_LEFT:
                    self.vana_x_v_liigub += -self.baas_kiirus
                    self.võib_liikuda_v = True
                    print(self.võib_liikuda_v)
                if e.key == pygame.K_RIGHT:
                    self.vana_x_p_liigub += self.baas_kiirus
                    self.võib_liikuda_p = True
                    print(self.võib_liikuda_p)
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.vana_y_ü_liigub -= -self.baas_kiirus
                    self.võib_liikuda_ü = False
                    print(self.võib_liikuda_ü)
                    print("keyup üles")
                if e.key == pygame.K_DOWN:
                    self.vana_y_a_liigub -= self.baas_kiirus
                    self.võib_liikuda_a = False
                    print(self.võib_liikuda_a)
                    print("keyup alla")
                if e.key == pygame.K_LEFT:
                    self.vana_x_v_liigub -= -self.baas_kiirus
                    self.võib_liikuda_v = False
                    print(self.võib_liikuda_v)
                    print("keyup vasak")
                if e.key == pygame.K_RIGHT:
                    self.vana_x_p_liigub -= self.baas_kiirus
                    self.võib_liikuda_p = False
                    print(self.võib_liikuda_p)
                    print("keyup parem")

        self.vana_all_x = int(self.vana_x) + 29
        self.vana_all_y = int(self.vana_y) + 55
        self.vana_üleval_x = int(self.vana_x) + 29
        self.vana_üleval_y = int(self.vana_y) - 1
        self.vana_vasak_x = int(self.vana_x)
        self.vana_vasak_y = int(self.vana_y) + 28
        self.vana_parem_x = int(self.vana_x) + 58
        self.vana_parem_y = int(self.vana_y) + 28

        self.värv_üleval = self.aken.get_at((self.vana_üleval_x, self.vana_üleval_y))
        self.värv_all = self.aken.get_at((self.vana_all_x, self.vana_all_y))
        self.värv_vasak = self.aken.get_at((self.vana_vasak_x, self.vana_vasak_y))
        self.värv_parem = self.aken.get_at((self.vana_parem_x, self.vana_parem_y))

        if self.värv_all == self.halb:
            self.vana_y_a_liigub = 0
            self.a = True

        if self.värv_all != self.halb:
            if self.võib_liikuda_a == True:
                self.vana_y += self.vana_y_a_liigub * self.dt

                self.a = False
            else:
                self.vana_y_a_liigub = 0

        if self.värv_üleval == self.halb:
            self.vana_y_ü_liigub = 0
            self.ü = True

        if self.värv_üleval != self.halb:
            if self.võib_liikuda_ü == True:
                self.vana_y += self.vana_y_ü_liigub * self.dt
                self.ü = False
            else:
                self.vana_y_ü_liigub = 0
        if self.värv_parem == self.halb:
            self.vana_x_p_liigub = 0
            self.p = True

        if self.värv_parem != self.halb:
            if self.võib_liikuda_p == True:
                self.vana_x += self.vana_x_p_liigub * self.dt
                self.p = False
            else:
                self.vana_x_p_liigub = 0

        if self.värv_vasak == self.halb:
            self.vana_x_v_liigub = 0
            self.v = True

        if self.värv_vasak != self.halb:
            if self.võib_liikuda_v == True:
                self.vana_x += self.vana_x_v_liigub * self.dt
                self.v = False
            else:
                self.vana_x_v_liigub = 0


