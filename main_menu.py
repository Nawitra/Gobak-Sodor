import pygame, sys, main

#inisialisasi pygame
pygame.init()
pygame.display.set_caption("Gobak Sodor: Reborn")
#home_image = pygame.image.load("image/home.png")

#inisialisasi game
size = [640, 400]
menuChoose = 0
background_color = [90, 84, 107]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = clock.tick(60)
fontGede = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf",80)
fontSedeng = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf", 35)
fontKecil = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf",24)
start = fontSedeng.render("Start", True, background_color, (255,255,255))
not_start = fontSedeng.render("Start", True, (255,255,255), background_color)
keluar = fontSedeng.render("Quit", True, background_color, (255,255,255))
not_keluar = fontSedeng.render("Quit", True, (255,255,255), background_color)
GobakSodor = fontGede.render("Gobak Sodor", True, (255,255,255), background_color)
Reborn = fontKecil.render("Reborn", True, (255,255,255), background_color)
bantuan = fontKecil.render("< Press Arrow Key to Move >", True, (255,255,255), background_color)
RebornRect = Reborn.get_rect()
GobakSodorRect = GobakSodor.get_rect()
startRect = start.get_rect()
not_startRect = not_start.get_rect()
keluarRect = keluar.get_rect()
not_keluarRect = not_keluar.get_rect()
bantuanRect = bantuan.get_rect()
bantuanRect.center = (320, 380)
GobakSodorRect.center = (320,45)
startRect.center = (220,200)
not_keluarRect.center = (420,200)
not_startRect.center = (220,200)
keluarRect.center = (420,200)
RebornRect.center = (320,100)

def homescreen(parameter):
    #screen.blit(home_image, (0,0))
    if(parameter == 1):
        screen.fill(background_color)
        screen.blit(GobakSodor, GobakSodorRect)
        screen.blit(Reborn, RebornRect)
        screen.blit(start, startRect)
        screen.blit(not_keluar,not_keluarRect)
        screen.blit(bantuan, bantuanRect)
        pygame.display.flip()
    else:
        screen.fill(background_color)
        screen.blit(GobakSodor, GobakSodorRect)
        screen.blit(Reborn, RebornRect)
        screen.blit(not_start, not_startRect)
        screen.blit(keluar,keluarRect)
        screen.blit(bantuan, bantuanRect)
        pygame.display.flip()
    #pygame.draw.rect(screen, (255,255,255), (150,450,100,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                menuChoose = 1
            if event.key == pygame.K_RIGHT:
                menuChoose = 0
            if event.key == pygame.K_RETURN:
                if menuChoose == 1:
                    #ke game ini fungsinya
                    while 1:
                        main.start_game(main.flag)
                else:
                    pygame.quit()
                    quit()
        homescreen(menuChoose)
