import pygame
import random
from gui.pit import Pit
from const import TEXT_COLOR

class Board:
    def __init__(self):
        self.bg = pygame.image.load("gui/img/bg.png")
        self.pits = self._load_pits()
        self.font = pygame.freetype.Font("gui/Comic Sans MS 400.ttf", 40)
    
    def _load_pits(self):
        pits = []
        pits.append(Pit("gui/img/basket.png", True, True, (50, 50), None))

        x = 230
        y = 50
        for _ in range(6):
            pits.append(Pit("gui/img/pit.png", True, False, (x, y), pits[-1]))
            x += 180
        pits.append(Pit("gui/img/basket.png", False, True, (1310, 130), pits[-1]))

        y += 320
        x -= 180
        for i in range(6):
            pits.append(Pit("gui/img/pit.png", False, False, (x, y), pits[-1], pits[6-i]))
            pits[-1].opposite_pit()._opposite = pits[-1]
            x -= 180

        pits[0]._next = pits[-1]

        return pits 

    def draw_board(self, win):
        win.fill((0, 0, 0))
        win.blit(self.bg, (0, 0))

        marbles = []
        
        for pit in self.pits:
            pit.draw(win)
            marbles += pit.get_marbles()

        for m in marbles:
            m.draw(win)

    def move_marbles(self):
        for pit in self.pits:
            pit.move_marbles()
    
    def prep_anim(self):
        for pit in self.pits:
            pit.prep_anim()

    def get_pit(self, pos, top_player):
        for pit in self.pits:
            if (not pit.is_basket and pit.top_player == top_player 
                and pit.in_position(pos) and pit.get_marbles_count() > 0):
                return pit
        return None

    def animation_finished(self):
        for pit in self.pits:
            for marble in pit.get_marbles():
                if marble.moving == True:
                    return False
        return True

    def draw_text(self, win, top_player):
        text = "PLAYER TOP" if top_player else "PLAYER BOTTOM"
        basket_top = str(self.get_basket(True).get_marbles_count())
        basket_bot = str(self.get_basket(False).get_marbles_count())
        self.font.render_to(win, (630, 600), text, TEXT_COLOR)
        self.font.render_to(win, (110, 600), basket_top, TEXT_COLOR)
        self.font.render_to(win, (1390, 600), basket_bot, TEXT_COLOR)
    
    def get_basket(self, top_player):
        for pit in self.pits:
            if pit.is_basket and pit.top_player == top_player:
                return pit

    def check_game_over(self, top_player):
        pits = [pit for pit in self.pits if pit.top_player == top_player and not pit.is_basket]
        for p in pits:
            if p.get_marbles_count() > 0:
                return False
        return True

    def draw_game_over(self, win):
        basket_top = str(self.get_basket(True).get_marbles_count())
        basket_bot = str(self.get_basket(False).get_marbles_count())
        text = "GAME OVER, WINNER: PLAYER TOP" if basket_top > basket_bot else "GAME OVER, WINNER: PLAYER BOTTOM"
        self.font.render_to(win, (530, 600), text, TEXT_COLOR)
        self.font.render_to(win, (110, 600), basket_top, TEXT_COLOR)
        self.font.render_to(win, (1390, 600), basket_bot, TEXT_COLOR)
