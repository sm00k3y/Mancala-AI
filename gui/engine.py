import pygame
import pygame.freetype
from gui.board import Board

class Engine:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.is_moving_anim = False
        self.board.prep_anim()
        self.top_player = True

    def update(self):
        self.board.move_marbles()
        self.board.draw_board(self.win)
        self.board.draw_text(self.win, self.top_player)
        pygame.display.update()

        if self.board.animation_finished():
            self.is_moving_anim = False

    def move(self, pos=(-1, -1), pit_number=-1):
        if self.is_moving_anim == True:
            return False
        self.is_moving_anim = True

        # Find pit clicked by mouse
        if pit_number == -1:
            pit = self.board.get_pit(pos, self.top_player)
        else:
            pit = self.board.get_pit_by_number(pit_number, self.top_player)

        if pit == None:
            return False
        
        # Move the marbles
        last_pit = self.move_marbles(pit)

        # Check take (zbicie)
        self.check_take(last_pit)
            
        # Change move if the last pit was not a player's basket
        if not (last_pit.is_basket and last_pit.top_player == self.top_player):
            self.top_player = not self.top_player

    # Moves marbles and returns last pit
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
            self.board.get_basket(self.top_player).add_marble(pit.get_marbles()[0])
            pit.remove_marbles()
            opposite_pit = pit.opposite_pit()
            opposite_marbles = opposite_pit.get_marbles()
            opposite_pit.remove_marbles()
            for m in opposite_marbles:
                self.board.get_basket(self.top_player).add_marble(m)

    def game_over(self):
        return self.board.check_game_over(self.top_player)

    def update_baskets_gameover(self):
        self.board.update_baskets_gameover(self.top_player)

    def print_game_over(self):
        self.board.move_marbles()
        self.board.draw_board(self.win)
        self.board.draw_game_over(self.win)
        pygame.display.update()
    
    def gamestate(self):
        return self.board.generate_gamestate(self.top_player)
        