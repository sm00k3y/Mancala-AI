import pygame
import random
from gui.pit import Pit
from const import TEXT_COLOR, FONT, FONT_SIZE


class Board:
    def __init__(self):
        self.bg = pygame.image.load("assets/bg.png")
        self.pits = self._load_pits()
        self.font = pygame.freetype.Font(FONT, FONT_SIZE)
    
    def _load_pits(self):
        pits = []
        pits.append(Pit("assets/basket.png", True, True, (50, 50), 6))

        x = 230; y = 50
        for i in range(6):
            pits.append(Pit("assets/pit.png", True, False, (x, y), 5-i, pits[-1]))
            x += 180
        pits.append(Pit("assets/basket.png", False, True, (1310, 130), 6, pits[-1]))

        y += 320; x -= 180
        for i in range(6):
            pits.append(Pit("assets/pit.png", False, False, (x, y), 5-i, pits[-1], pits[6-i]))
            pits[-1].opposite_pit()._opposite = pits[-1]
            x -= 180

        pits[0]._next = pits[-1]

        return pits 

    def draw_board(self, win):
        win.fill((0, 0, 0))
        win.blit(self.bg, (0, 0))

        marbles = []
        
        for pit in self.pits:
            pit.draw(win, self.font)
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

    def get_pit_by_number(self, pit_number, top_player):
        for pit in self.pits:
            if pit.top_player == top_player and pit.number == pit_number:
                return pit
        
    def animation_finished(self):
        for pit in self.pits:
            for marble in pit.get_marbles():
                if marble.moving == True:
                    return False
        return True

    def draw_text(self, win, top_player):
        text = "TOP PLAYER" if top_player else "BOTTOM PLAYER"
        basket_top = str(self.get_basket(True).get_marbles_count())
        basket_bot = str(self.get_basket(False).get_marbles_count())
        self.font.render_to(win, (610, 600), text, TEXT_COLOR)
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
    
    def update_baskets_gameover(self, top_player):
        pits = [pit for pit in self.pits if pit.top_player != top_player and not pit.is_basket\
                and pit.get_marbles_count() != 0]
        basket = self.get_basket(not top_player)
        for pit in pits:
            for marble in pit.get_marbles():
                basket.add_marble(marble)
            pit.remove_marbles()

    def draw_game_over(self, win):
        basket_top = str(self.get_basket(True).get_marbles_count())
        basket_bot = str(self.get_basket(False).get_marbles_count())
        text = "GAME OVER, WINNER: TOP PLAYER" if basket_top > basket_bot else "GAME OVER, WINNER: BOTTOM PLAYER"
        self.font.render_to(win, (350, 600), text, TEXT_COLOR)
        self.font.render_to(win, (110, 600), basket_top, TEXT_COLOR)
        self.font.render_to(win, (1390, 600), basket_bot, TEXT_COLOR)

    def generate_gamestate(self, top_player):
        a_player_basket = self.pits[0].get_marbles_count()
        a_player_points = []
        for i in range(1, 7):
            a_player_points.append(self.pits[i].get_marbles_count())
        b_player_basket = self.pits[7].get_marbles_count()
        b_player_points = []
        for i in range(8, 14):
            b_player_points.append(self.pits[i].get_marbles_count())

        a_player_points.reverse()
        b_player_points.reverse()
        
        return a_player_basket, a_player_points, b_player_basket, b_player_points, top_player

