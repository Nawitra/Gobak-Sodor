import pygame, sys, player_class

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

#inisialisasi penjaga



#update screen
def window():
    screen.fill(background_colour)
    pygame.draw.line(screen, player_line_colour, [150, 70], [150, 320], 1)
    pygame.draw.line(screen, guard_line_colour, [260, 30], [260, 360], 1)
    pygame.draw.line(screen, guard_line_colour, [360, 30], [360, 360], 1)
    pygame.draw.line(screen, guard_line_colour, [450, 30], [450, 360], 1)
    screen.blit(pemain.image, (pemain.x, pemain.y))
    pygame.display.update()

#menggerakkan karakter
def character():
    pemain.getEvent(size[0], size[1])
    pemain.boundCheck(size[0], size[1])
    dt = clock.tick(60)
    pemain.changePos(dt, size[0], size[1])

#penjaga satu

#mulai game
while 1:
    window()
    character()

