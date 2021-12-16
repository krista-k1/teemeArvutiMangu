import pygame, sys, random
import pygame_gui

pygame.init()

aken = pygame.display.set_mode([1024, 768])
manager = pygame_gui.UIManager([800, 600])

lol = pygame.image.load("woop.png")

halb = (0, 0, 0, 255)

koll = pygame.image.load("lamp.png")

koll_x = 800
koll_y = 450

koll_y_a_liigub = 0
koll_y_ü_liigub = 0
koll_x_p_liigub = 0
koll_x_v_liigub = 0

baas_kiirus = 100

kü = False
ka = False
kv = False
kp = False

mäng_töötab = True
kell = pygame.time.Clock()






while mäng_töötab:
    dt = kell.tick() / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False



    koll_all_x = int(koll_x) + 29
    koll_all_y = int(koll_y) + 55
    koll_värv_all = aken.get_at((koll_all_x, koll_all_y))



    koll_üleval_x = int(koll_x) + 29
    koll_üleval_y = int(koll_y) - 1
    koll_värv_üleval = aken.get_at((koll_üleval_x, koll_üleval_y))




    koll_vasak_x = int(koll_x)
    koll_vasak_y = int(koll_y) + 28
    koll_värv_vasak = aken.get_at((koll_vasak_x, koll_vasak_y))




    koll_parem_x = int(koll_x) + 58
    koll_parem_y = int(koll_y) + 28
    koll_värv_parem = aken.get_at((koll_parem_x, koll_parem_y))



    if koll_y_ü_liigub + koll_y_a_liigub + koll_x_v_liigub + koll_x_p_liigub == 0:

        nr1 = random.randint(0, 3)
        if nr1 == 0 and ka != True:
            koll_y_a_liigub = 1000
        if nr1 == 1 and kv != True:
            koll_x_v_liigub = 1000
        if nr1 == 2 and kp != True:
            koll_x_p_liigub = 1000
        if nr1 == 3 and kü != True:
            koll_y_ü_liigub = 1000






    if koll_värv_üleval == halb:
        kü = True
        koll_y_ü_liigub = 0
    if koll_värv_üleval != halb:
        kü = False

    if koll_värv_all == halb:
        ka = True
        koll_y_a_liigub = 0
    if koll_värv_all != halb:
        ka = False

    if koll_värv_vasak == halb:
        kv = True
        koll_x_v_liigub = 0
    if koll_värv_vasak != halb:
        kv = False


    if koll_värv_parem == halb:
        kp = True
        koll_x_p_liigub = 0
    if koll_värv_parem != halb:
        kp = False

    if koll_x > 1900 or koll_x < 0:
        koll_x = 400

    if koll_y > 1020 or koll_y < 0:
        koll_y = 300



    koll_y -= koll_y_ü_liigub * dt
    koll_y += koll_y_a_liigub * dt
    koll_x += koll_x_p_liigub * dt
    koll_x -= koll_x_v_liigub * dt


    aken.blit(lol, (0, 0))
    aken.blit(koll, [koll_x, koll_y])

    pygame.display.flip()



pygame.quit()