import pygame
import pygame.freetype
from gui.board import Board

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.is_moving_anim = False
        self.board.prep_anim()
        self.top_player = True

    def update(self):
        self.board.move_marbles()
        self.board.draw_board(self.win, self.top_player)

        if self.board.animation_finished():
            self.is_moving_anim = False

    def move(self, pos):
        if self.is_moving_anim == True:
            print("NOPE")
            return

        print("YEP")
        self.is_moving_anim = True

        # Find pit clicked by mouse
        pit = self.board.get_pit(pos, self.top_player)

        if pit == None:
            self.is_moving_anim = False
            return
        
        # Move the marbles
        last_pit = self.move_marbles(pit)

        # Check take (zbicie)
        self.check_take(last_pit)
            
        # Change move if the last pit was not a player's basket
        if not (last_pit.is_basket and last_pit.top_player == self.top_player):
            self.top_player = not self.top_player

    # Moves marbles and returns last marble
    def move_marbles(self, pit):
        marbles = pit.get_marbles()
        pit.remove_marbles()
        for i in range(len(marbles)):
            pit = pit.next_pit()
            if pit.is_basket and pit.top_player != self.top_player:
                pit = pit.next_pit()
            pit.add_marble(marbles[i])
        return pit

    def check_take(self, pit):
        cond = (pit.top_player == self.top_player and pit.get_marbles_count() == 1 and
                not pit.is_basket and pit.opposite_pit().get_marbles_count() != 0)
        if cond:
            opposite_pit = pit.opposite_pit()
            opposite_marbles = opposite_pit.get_marbles()
            opposite_pit.remove_marbles()
            for m in opposite_marbles:
                self.board.get_basket(self.top_player).add_marble(m)
            self.board.get_basket(self.top_player).add_marble(pit.get_marbles()[0])
        