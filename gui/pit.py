import pygame
from gui.marble import Marble
from const import TEXT_COLOR


class Pit:
    def __init__(self, pit_path, top_player, is_basket, pit_pos, pit_number, next_pit=None, opposite=None):
        self.img = pygame.image.load(pit_path)
        self.size = self.img.get_rect().size
        self.top_player = top_player
        self.is_basket = is_basket
        self.pos = pit_pos
        self.number = pit_number
        self._next = next_pit
        self._opposite = opposite
        self.marbles = self._load_marbles()
        # self.marbles = self._load_marbles_test()

    def draw(self, win, font):
        win.blit(self.img, self.pos)
        if not self.is_basket:
            text = str(self.get_marbles_count())
            if self.top_player:
                font.render_to(win, (self.pos[0] + 70, self.pos[1] + 180), text, TEXT_COLOR)
            else:
                font.render_to(win, (self.pos[0] + 70, self.pos[1] - 50), text, TEXT_COLOR)

    def _load_marbles(self):
        if self.is_basket:
            return []

        marbles = []
        for i in range(1, 5):
            marble = Marble(f"assets/marble{i}.png")
            marble.rand_position(self.pos, self.size)
            marbles.append(marble)
        return marbles

    # TEST
    def _load_marbles_test(self):
        if self.is_basket:
            return []

        marbles = []
        if self.number == 1 or self.number == 5:
            marble = Marble(f"assets/marble1.png")
            marble.rand_position(self.pos, self.size)
            marbles.append(marble)
        return marbles

    def move_marbles(self):
        for marble in self.marbles:
            marble.move()
    
    def prep_anim(self):
        for marble in self.marbles:
            marble.calc_step()

    def in_position(self, pos):
        return pos[0] > self.pos[0] and pos[0] < self.pos[0] + self.size[0] \
            and pos[1] > self.pos[1] and pos[1] < self.pos[1] + self.size[1]
    
    def next_pit(self):
        return self._next

    def opposite_pit(self):
        return self._opposite

    def get_marbles(self):
        return self.marbles

    def get_marbles_count(self):
        return len(self.marbles)

    def add_marble(self, marble):
        marble.rand_position(self.pos, self.size)
        marble.calc_step()
        self.marbles.append(marble)

    def remove_marbles(self):
        self.marbles = []