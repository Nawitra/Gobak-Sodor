import pygame, sys, player_class, guard_class

#inisialisasi pygame
pygame.init()
pygame.display.set_caption("Gobak Sodor: Reborn")

#inisialisasi game
size = [640, 400]
background_image = pygame.image.load("image/Background.png")
background_colour = [90, 84, 107]
player_line_colour = [131, 198, 106]
guard_line_colour = [255, 255, 255]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = clock.tick(60)
flag = 0

#inisialisasi karakter pemain
player_x = size[0] - 565
player_y = size[1] - 220
player_w = 32
player_h = 32
player_speed = 0.3
pemain = player_class.player(player_x, player_y, player_w, player_h, player_speed)

#invisible wall
guard_upper_limit = 35
guard_lower_limit = 355

#inisialisasi penjaga 1
guard1_x = 260 - 24
guard1_y = 165 - 24
guard1_w = 48
guard1_h = 48
guard1_speed = 0.2
guard1_image = pygame.image.load("image/Penjaga 1.png")
penjaga1 = guard_class.guard(guard1_x, guard1_y, guard1_w, guard1_h, guard1_speed)

#inisialisasi penjaga 2
guard2_x = 360 - 8
guard2_y = 165 - 8
guard2_w = 16
guard2_h = 16
guard2_speed = 0.6
guard2_image = pygame.image.load("image/Penjaga 2.png")
penjaga2 = guard_class.guard(guard2_x, guard2_y, guard2_w, guard2_h, guard2_speed)

#inisialisasi penjaga 3
guard3_x = 450 - 16
guard3_y = 165 - 16
guard3_w = 32
guard3_h = 32
guard3_speed = 0.3
guard3_image = pygame.image.load("image/Penjaga 3.png")
penjaga3 = guard_class.guard(guard3_x, guard3_y, guard3_w, guard3_h, guard3_speed)


#update screen
def window():
    screen.blit(background_image, (0, 0))
    screen.blit(guard1_image, (penjaga1.x, penjaga1.y))
    screen.blit(guard2_image, (penjaga2.x, penjaga2.y))
    screen.blit(guard3_image, (penjaga3.x, penjaga3.y))    
    screen.blit(pemain.image, (pemain.x, pemain.y))
    clock.tick(60)
    pygame.display.flip()


#menggerakkan karakter
def character():
    pemain.getEvent(size[0], size[1])
    pemain.boundCheck(size[0], size[1])
    pemain.changePos(dt, size[0], size[1])

#penjaga satu
def guard1():
    penjaga1.checkWall(guard_upper_limit, guard_lower_limit)
    penjaga1.movement(dt)

#penjaga dua
def guard2():
    penjaga2.checkWall(guard_upper_limit, guard_lower_limit)
    penjaga2.movement(dt)

#penjaga tiga
def guard3():
    penjaga3.checkWall(guard_upper_limit, guard_lower_limit)
    penjaga3.movement(dt)

def detectCollision1():
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga1.x + penjaga1.w) or pemain.x < penjaga1.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga1.y + penjaga1.h) or pemain.y < penjaga1.y):
        pemain.x = pemain.x
    else:
        temp = pemain.x - 70
        while(pemain.x > temp):
            pemain.x -= 3
            window()

def detectCollision2():
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga2.x + penjaga2.w) or pemain.x < penjaga2.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga2.y + penjaga2.h) or pemain.y < penjaga2.y):
        pemain.x = pemain.x
    else:
        temp = pemain.x - 20
        while(pemain.x > temp):
            pemain.x -= 1
            window()

def detectCollision3():
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga3.x + penjaga3.w) or pemain.x < penjaga3.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga3.y + penjaga3.h) or pemain.y < penjaga3.y):
        pemain.x = pemain.x
    else:
        temp = pemain.x - 50
        while(pemain.x > temp):
            pemain.x -= 2
            window()

start_time= pygame.time.get_ticks()    
while 1:
    time_passed = (pygame.time.get_ticks() - start_time) / 1000
    if(time_passed > 10):
        break
    else:
        window()
        character()
        guard1()
        guard2()
        guard3()
        detectCollision1()
        detectCollision2()
        detectCollision3()

