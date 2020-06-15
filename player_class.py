import sys, pygame, main_menu

pygame.mixer.init()

class player():
    def __init__(self, x = 0, y = 0, w = 0, h = 0, speed = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.key_pressed = [False]*4
        self.image = pygame.image.load("image/Player 1.png")
    def boundCheck(self, size_x = 0, size_y = 0):
        if self.x < 35:
            self.x = 75
        if self.x > size_x - 10:
            self.x = size_x - 10
        if self.y < 25:
            self.y = 25
        if self.y > size_y - 10:
            self.y = size_x - 10
    def getEvent(self, size_x = 0, size_y = 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    self.key_pressed[0] = True  
                if event.key == pygame.K_RIGHT and self.x < size_x-70:
                    self.key_pressed[1] = True
                if event.key == pygame.K_UP and self.y > 0:
                    self.key_pressed[2] = True
                if event.key == pygame.K_DOWN and self.y < size_y-70:
                    self.key_pressed[3] = True
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    pygame.mixer.music.load("music/GameOver.mp3")
                    pygame.mixer.music.play(0)
                    main_menu.masukSini()
                else:
                    continue
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.key_pressed[0] = False
                if event.key == pygame.K_RIGHT:
                    self.key_pressed[1] = False
                if event.key == pygame.K_UP:
                    self.key_pressed[2] = False
                if event.key == pygame.K_DOWN:
                    self.key_pressed[3] = False
                else:
                    continue
    def changePos(self, dt = 1, size_x = 0, size_y = 0):
        if self.key_pressed[0] == True and self.x > 0:
            self.x -= self.speed * dt
        if self.key_pressed[1] == True and self.x < size_x - 70:
            self.x += self.speed * dt
        if self.key_pressed[2] == True and self.y > 0:
            self.y -= self.speed * dt
        if self.key_pressed[3] == True and self.y < size_y - 70:
            self.y += self.speed * dt
