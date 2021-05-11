import pygame
from const import TEXT_COLOR


class Button:
    def __init__(self, x, y, width, height, text=""):
        self.color = (39, 0, 78)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size_pos = (x, y, width, height)
        self.text = text
    
    def draw(self, win, font):
        # pygame.draw.rect(win, (0, 0, 0), (self.x-3, self.y-3, self.width+6, self.height+6), border_radius=40)
        pygame.draw.rect(win, self.color, self.size_pos, border_radius=40)
        if self.text != "":
            text = font.render(self.text, TEXT_COLOR)
            win.blit(text[0], (self.x + (self.width / 2) - (text[0].get_width() / 2), \
                               self.y + (self.height / 2) - (text[0].get_height() / 2)))

    def is_over(self, pos):
        cond = (pos[0] > self.x and pos[0] < self.x + self.width and \
                pos[1] > self.y and pos[1] < self.y + self.height)
        return cond