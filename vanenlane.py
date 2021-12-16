import pygame, sys, random
import pygame_gui

pygame.init()

class Bot(pygame.sprite.Sprite):

    def __init__(self):

        self.aken = pygame.display.set_mode([1024, 768])
        self.halb = (0, 0, 0, 255)

        self.koll = pygame.image.load("lamp.png")

        self.koll_x = 800
        self.koll_y = 450

        self.koll_y_a_liigub = 0
        self.koll_y_ü_liigub = 0
        self.koll_x_p_liigub = 0
        self.koll_x_v_liigub = 0

        self.baas_kiirus = 100

        self.kü = False
        self.ka = False
        self.kv = False
        self.kp = False


        self.kell = pygame.time.Clock()
        self.dt = self.kell.tick() / 1000
    def bot_liikumine(self):

        self.koll_all_x = int(self.koll_x) + 29
        self.koll_all_y = int(self.koll_y) + 55
        self.koll_värv_all = self.aken.get_at((self.koll_all_x, self.koll_all_y))

        self.koll_üleval_x = int(self.koll_x) + 29
        self.koll_üleval_y = int(self.koll_y) - 1
        self.koll_värv_üleval = self.aken.get_at((self.koll_üleval_x, self.koll_üleval_y))

        self.koll_vasak_x = int(self.koll_x)
        self.koll_vasak_y = int(self.koll_y) + 28
        self.koll_värv_vasak = self.aken.get_at((self.koll_vasak_x, self.koll_vasak_y))

        self.koll_parem_x = int(self.koll_x) + 58
        self.koll_parem_y = int(self.koll_y) + 28
        self.koll_värv_parem = self.aken.get_at((self.koll_parem_x, self.koll_parem_y))

        if self.koll_y_ü_liigub + self.koll_y_a_liigub + self.koll_x_v_liigub + self.koll_x_p_liigub == 0:

            nr1 = random.randint(0, 3)
            if nr1 == 0 and self.ka != True:
                self.koll_y_a_liigub = 1000
            if nr1 == 1 and self.kv != True:
                self.koll_x_v_liigub = 1000
            if nr1 == 2 and self.kp != True:
                self.koll_x_p_liigub = 1000
            if nr1 == 3 and self.kü != True:
                self.koll_y_ü_liigub = 1000

        if self.koll_värv_üleval == self.halb:
            self.kü = True
            self.koll_y_ü_liigub = 0
        if self.koll_värv_üleval != self.halb:
            self.kü = False

        if self.koll_värv_all == self.halb:
            self.ka = True
            self.koll_y_a_liigub = 0
        if self.koll_värv_all != self.halb:
            self.ka = False

        if self.koll_värv_vasak == self.halb:
            self.kv = True
            self.koll_x_v_liigub = 0
        if self.koll_värv_vasak != self.halb:
            self.kv = False

        if self.koll_värv_parem == self.halb:
            self.kp = True
            self.koll_x_p_liigub = 0
        if self.koll_värv_parem != self.halb:
            self.kp = False

        if self.koll_x > 1900 or self.koll_x < 0:
            self.koll_x = 400

        if self.koll_y > 1020 or self.koll_y < 0:
            self.koll_y = 300


        self.koll_y -= self.koll_y_ü_liigub * self.dt
        self.koll_y += self.koll_y_a_liigub * self.dt
        self.koll_x += self.koll_x_p_liigub * self.dt
        self.koll_x -= self.koll_x_v_liigub * self.dt


        self.aken.blit(self.koll, [self.koll_x, self.koll_y])

        pygame.display.flip()