import pygame
import random
from const import MARBLE_MOVE_CONST, FPS

class Marble:
    def __init__(self, marble_path):
        self.img = pygame.image.load(marble_path)
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.x_step = 0
        self.y_step = 0
        self.moving = False

    def get_pos(self):
        return (self.x, self.y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def rand_position(self, position, pit_size):
        self.target_x = random.randint(position[0] + 25, position[0] + pit_size[0] - 50)
        self.target_y = random.randint(position[1] + 25, position[1] + pit_size[1] - 50)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def move(self):
        if self.x == self.target_x and self.y == self.target_y:
            self.moving = False
            return

        if self.x > self.target_x - MARBLE_MOVE_CONST and self.x < self.target_x + MARBLE_MOVE_CONST:
            self.x = self.target_x
        if self.y > self.target_y - MARBLE_MOVE_CONST and self.y < self.target_y + MARBLE_MOVE_CONST:
            self.y = self.target_y

        if self.x != self.target_x:
            self.x += self.x_step
        if self.y != self.target_y:
            self.y += self.y_step

    def calc_step(self):
        self.moving = True

        self.x_step = ((self.target_x - self.x) / FPS) * 2
        self.y_step = ((self.target_y - self.y) / FPS) * 2
