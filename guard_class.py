import pygame, sys

class guard():
    def __init__(self, x = 0, y = 0, w = 0, h = 0, speed = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
    def checkWall(self, upper_limit = 0, lower_limit = 0):
        if (self.y < upper_limit or (self.y + self.h) > lower_limit):
            self.speed = -(self.speed)            
    def movement(self, dt = 0):
        self.y += self.speed * dt
            
