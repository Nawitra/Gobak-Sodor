import pygame, sys, player_class, guard_class

#inisialisasi pygame
pygame.init()
pygame.display.set_caption("Gobak Sodor: Reborn")

#inisialisasi game
size = [640, 400]
background_colour = [90, 84, 107]
player_line_colour = [131, 198, 106]
guard_line_colour = [255, 255, 255]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#inisialisasi karakter pemain
player_x = size[0] - 565
player_y = size[1] - 220
player_w = 32
player_h = 32
player_speed = 0.4 
pemain = player_class.player(player_x, player_y, player_w, player_h, player_speed)

#inisialisasi penjaga 1
guard1_x = 260 - 24
guard1_y = 165 - 24
guard1_w = 48
guard1_h = 48
guard1_upper_limit = 35
guard1_lower_limit = 355
guard1_speed = 0.2
penjaga1 = guard_class.guard(guard1_x, guard1_y, guard1_w, guard1_h, guard1_speed)


#update screen
def window():
    screen.fill(background_colour)
    pygame.draw.line(screen, player_line_colour, [150, 70], [150, 320], 1)
    pygame.draw.line(screen, guard_line_colour, [260, 30], [260, 360], 1)
    pygame.draw.line(screen, guard_line_colour, [360, 30], [360, 360], 1)
    pygame.draw.line(screen, guard_line_colour, [450, 30], [450, 360], 1)
    screen.blit(penjaga1.image, (penjaga1.x, penjaga1.y))
    screen.blit(pemain.image, (pemain.x, pemain.y))
    pygame.display.update()

#menggerakkan karakter
def character():
    pemain.getEvent(size[0], size[1])
    pemain.boundCheck(size[0], size[1])
    dt = clock.tick(60)
    pemain.changePos(dt, size[0], size[1])

#penjaga satu
def guard1():
    penjaga1.checkWall(guard1_upper_limit, guard1_lower_limit)
    dt = clock.tick(60)
    penjaga1.movement(dt)

#mulai game
while 1:
    window()
    character()
    guard1()

