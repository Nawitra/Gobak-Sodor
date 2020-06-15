import pygame, sys, player_class, guard_class, main_menu

#inisialisasi pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Gobak Sodor: Reborn")

#inisialisasi game
size = [640, 400]
background_image = pygame.image.load("image/Background.png")
timer_colour = [255, 255, 255]
programIcon = pygame.image.load("image/Logo.png")
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dt = clock.tick(60)
flag = 0
font = pygame.font.SysFont('Consolas', 30)
#gameover_music = pygame.mixer.music.load("music/GameOver.mp3")

#inisialisasi karakter pemain
player_x = size[0] - 565
player_y = size[1] - 220
player_w = 32
player_h = 32
player_speed = 0.3
pemain = player_class.player(player_x, player_y, player_w, player_h, player_speed)
    
#invisible wall
guard_upper_limit = 40
guard_lower_limit = 355

#inisialisasi penjaga 1
guard1_x = 260 - 26
guard1_y = 165 - 26
guard1_w = 48
guard1_h = 48
guard1_speed = 0.2
guard1_image = [pygame.image.load("image/Penjaga 1/Penjaga 1-1.png"),
                pygame.image.load("image/Penjaga 1/Penjaga 1-1.png"),
                pygame.image.load("image/Penjaga 1/Penjaga 1-1.png"),
                pygame.image.load("image/Penjaga 1/Penjaga 1-3.png"),
                pygame.image.load("image/Penjaga 1/Penjaga 1-3.png"),
                pygame.image.load("image/Penjaga 1/Penjaga 1-3.png")]
guard1_counter = 0
penjaga1 = guard_class.guard(guard1_x, guard1_y, guard1_w, guard1_h, guard1_speed)

#inisialisasi penjaga 2
guard2_x = 360 - 10
guard2_y = 165 - 10
guard2_w = 16
guard2_h = 16
guard2_speed = 0.6
guard2_image = [pygame.image.load("image/Penjaga 2/Penjaga 2-1.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-1.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-1.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-2.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-2.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-2.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-3.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-3.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-3.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-4.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-4.png"),
                pygame.image.load("image/Penjaga 2/Penjaga 2-4.png")]
guard2_counter = 0
penjaga2 = guard_class.guard(guard2_x, guard2_y, guard2_w, guard2_h, guard2_speed)

#inisialisasi penjaga 3
guard3_x = 450 - 18
guard3_y = 165 - 18
guard3_w = 32
guard3_h = 32
guard3_speed = 0.3
guard3_image = [pygame.image.load("image/Penjaga 3/Penjaga 3-1.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-1.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-1.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-2.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-2.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-2.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-3.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-3.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-3.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-4.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-4.png"),
                pygame.image.load("image/Penjaga 3/Penjaga 3-4.png")]
guard3_counter = 0
penjaga3 = guard_class.guard(guard3_x, guard3_y, guard3_w, guard3_h, guard3_speed)

#-------------------------------------------------

#update screen
def window(text):
    global guard1_counter
    global guard2_counter
    global guard3_counter
    screen.blit(background_image, (0, 0))
    if(guard1_counter == 6):
        guard1_counter = 0
    if(guard2_counter == 12):
        guard2_counter = 0
    if(guard3_counter == 12):
        guard3_counter = 0
    screen.blit(guard1_image[guard1_counter], (penjaga1.x, penjaga1.y))    
    screen.blit(guard2_image[guard2_counter], (penjaga2.x, penjaga2.y))
    screen.blit(guard3_image[guard3_counter], (penjaga3.x, penjaga3.y))    
    screen.blit(pemain.image, (pemain.x, pemain.y))
    screen.blit(text, (20, 20))
    clock.tick(60)
    pygame.display.flip()
    guard1_counter += 1
    guard2_counter += 1
    guard3_counter += 1


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

def detectCollision1(text):
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga1.x + penjaga1.w) or pemain.x < penjaga1.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga1.y + penjaga1.h) or pemain.y < penjaga1.y):
        pemain.x = pemain.x
    else:
        if(flag == 0):
            temp = pemain.x - 100
            while(pemain.x > temp):
                pemain.x -= 3
                window(text)
        elif(flag == 1):
            temp = pemain.x + 100
            while(pemain.x < temp):
                pemain.x += 3
                window(text)

def detectCollision2(text):
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga2.x + penjaga2.w) or pemain.x < penjaga2.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga2.y + penjaga2.h) or pemain.y < penjaga2.y):
        pemain.x = pemain.x
    else:
        if(flag == 0):
            temp = pemain.x - 60
            while(pemain.x > temp):
                pemain.x -= 2
                window(text)
        elif(flag == 1):
            temp = pemain.x + 60
            while(pemain.x < temp):
                pemain.x += 2
                window(text)

def detectCollision3(text):
    #kolisi antara pemain dengan penjaga 1
    if(pemain.x > (penjaga3.x + penjaga3.w) or pemain.x < penjaga3.x):
        pemain.x = pemain.x
    elif(pemain.y > (penjaga3.y + penjaga3.h) or pemain.y < penjaga3.y):
        pemain.x = pemain.x
    else:
        if(flag == 0):
            temp = pemain.x - 80
            while(pemain.x > temp):
                pemain.x -= 2
                window(text)
        elif(flag == 1):
            temp = pemain.x + 80
            while(pemain.x < temp):
                pemain.x += 2
                window(text)

def checkTimeAndCollision():
    time_passed = (pygame.time.get_ticks() - start_time) / 1000
    timer = str(time_passed)
    text = font.render(timer, True, timer_colour)
    detectCollision1(text)
    detectCollision2(text)
    detectCollision3(text)
    window(text)
    if(time_passed > 10):
        pygame.mixer.stop()
        pygame.mixer.music.load("music/GameOver.mp3")
        pygame.mixer.music.play(0)
        main_menu.masukSini()
        
def timer_start():
    global start_time
    start_time = pygame.time.get_ticks()
    start_game()

def start_game():
    global flag
    pygame.mixer.music.load("music/Gameplay.mp3")
    pygame.mixer.music.play(0)
    while 1:
        if(pemain.x >= (500 + pemain.w)):
            flag = 1
        if(pemain.x <= (148 - pemain.w) and flag == 1):
            pygame.mixer.stop()
            main_menu.masukSiniWin()
            sys.exit()
        else:
            checkTimeAndCollision()
            character()
            guard1()
            guard2()
            guard3()



