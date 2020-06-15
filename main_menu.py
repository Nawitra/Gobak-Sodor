import pygame, sys, main

#inisialisasi pygame
pygame.init()
pygame.display.set_caption("Gobak Sodor: Reborn")
#home_image = pygame.image.load("image/home.png")

#inisialisasi game
size = [640, 400]
GOChoose = 1
menuChoose = 1
background_color = [90, 84, 107]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = clock.tick(60)

#untuk munculin teks
fontGede = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf",80)
fontSedeng = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf", 35)
fontKecil = pygame.font.Font("res/8bitOperatorPlusSC-Regular.ttf",24)

#warna
black = [0, 0, 0]
white = [255, 255, 255]

#main menu
start = fontSedeng.render("Start", True, background_color, white)
not_start = fontSedeng.render("Start", True, white, background_color)
keluar = fontSedeng.render("Quit", True, background_color, white)
not_keluar = fontSedeng.render("Quit", True, white, background_color)
GobakSodor = fontGede.render("Gobak Sodor", True, white, background_color)
Reborn = fontKecil.render("Reborn", True, white, background_color)
bantuan = fontKecil.render("< Press Arrow Key to Move >", True, white, background_color)

#------buat posisi teks main menu
#bikin rectangle
RebornRect = Reborn.get_rect()
GobakSodorRect = GobakSodor.get_rect()
startRect = start.get_rect()
not_startRect = not_start.get_rect()
keluarRect = keluar.get_rect()
not_keluarRect = not_keluar.get_rect()
bantuanRect = bantuan.get_rect()

#posisiin rectangle untuk teks main menu
bantuanRect.center = (320, 380)
GobakSodorRect.center = (320,45)
startRect.center = (220,200)
not_keluarRect.center = (420,200)
not_startRect.center = (220,200)
keluarRect.center = (420,200)
RebornRect.center = (320,100)

#gameover menu
gameOver = fontGede.render("Game Over", True, white, black)
GO_no_retry = fontSedeng.render("Retry", True, white, black)
GO_retry = fontSedeng.render("Retry", True, black, white)
GO_keluar = fontSedeng.render("Quit", True, black, white)
GO_no_keluar = fontSedeng.render("Quit", True, white, black)

#------Posisi teks gameover
#bikin rectangle
GO_retryRect = GO_retry.get_rect()
GO_no_retryRect = GO_no_retry.get_rect()
GO_keluarRect = GO_keluar.get_rect()
GO_no_keluarRect = GO_no_keluar.get_rect()
gameOverRect = gameOver.get_rect()

#posisiin rectangle untuk teks main menu
GO_retryRect.center = (220,200)
GO_no_retryRect.center = (220,200)
GO_keluarRect.center = (420,200)
GO_no_keluarRect.center = (420,200)
gameOverRect.center = (320, 45)


#
def homescreen(parameter):
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

def akhirGame(parameter):
    if(parameter == 1):
        screen.fill(black)
        screen.blit(gameOver, gameOverRect)
        screen.blit(GO_retry, GO_retryRect)
        screen.blit(GO_no_keluar, GO_no_keluarRect)
        pygame.display.flip()
    else:
        screen.fill(black)
        screen.blit(gameOver, gameOverRect)
        screen.blit(GO_no_retry, GO_no_retryRect)
        screen.blit(GO_keluar, GO_keluarRect)
        pygame.display.flip()

def masukSini():
    parameter = 1
    while 1:
        for event in pygame.event.get():
            akhirGame(parameter)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    parameter = 1
                if event.key == pygame.K_RIGHT:
                    parameter = 0
                if event.key == pygame.K_RETURN:
                    if parameter == 1:
                        main.start_time = 0
                        masukAwal()
                    else:
                        pygame.quit()
                        quit()

def masukAwal():
    global menuChoose
    while True:
        for event in pygame.event.get():
            homescreen(menuChoose)
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
                        main.timer_start()
                    else:
                        pygame.quit()
                        quit()
    

if __name__ == "__main__":
    while True:
        masukAwal()
