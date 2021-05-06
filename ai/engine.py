from ai.tools import is_int, draw_board


class GameState:
    def __init__(self):
        self.a_player_points = []
        self.b_player_points = []
        self.a_player_basket = 0
        self.b_player_basket = 0
        self.cur_player = ""
        self.game_over = False

    def update(self, game_state):
        a_b, a_p, b_b, b_p, top = game_state
        self.a_player_basket = a_b
        self.a_player_points = a_p
        self.b_player_basket = b_b
        self.b_player_points = b_p
        self.cur_player = "TOP" if top else "BOTTOM"
        draw_board(a_p, b_p, a_b, b_b)

    def evaluate(self):
        return self.a_player_basket - self.b_player_basket
            
    def possible_moves(self):
        moves = []
        for i in range(6):
            if self._check_move(i):
                moves.append(i)
        return moves
    
    def _check_move(self, move):
        return (self.cur_player == "TOP" and self.a_player_points[move] != 0) or \
               (self.cur_player == "BOTTOM" and self.b_player_points[move] != 0)
            
    def make_move(self, move):
        if self.check_game_over():
            self.game_over = True
            self._update_baskets_endgame()
            return True

        idx = move
        table = self.a_player_points if self.cur_player == "TOP" else self.b_player_points
        points_left = table[idx]
        table[idx] = 0

        while points_left > 0:
            if idx == 5:
                if self._update_basket(table):
                    points_left -= 1
                    if points_left == 0:
                        return True
                table = self._change_table(table)
                idx = -2
            else:
                table[idx+1] += 1
                points_left -= 1
            idx += 1
        
        if idx > -1:
            self._check_take(table, idx)
        
        return False

    def next_player(self):
        if self.cur_player == "TOP":
            self.cur_player = "BOTTOM"
        else:
            self.cur_player = "TOP"

    def _change_table(self, table):
        if table == self.a_player_points:
            table = self.b_player_points
        else:
            table = self.a_player_points
        return table

    def _update_basket(self, table):
        if self.cur_player == "TOP" and table == self.a_player_points:
            self.a_player_basket += 1
            return True
        elif self.cur_player == "BOTTOM" and table == self.b_player_points:
            self.b_player_basket += 1
            return True
        else:
            return False

    def _check_take(self, table, idx):
        if self.cur_player == "TOP" and table == self.a_player_points:
            if self.a_player_points[idx] == 1 and self.b_player_points[5 - idx] != 0:
                self.a_player_basket += self.b_player_points[5 - idx]
                self.b_player_points[5 - idx] = 0
                self.a_player_basket += 1
                self.a_player_points[idx] = 0
        elif self.cur_player == "BOTTOM" and table == self.b_player_points:
            if self.b_player_points[idx] == 1 and self.a_player_points[5 - idx] != 0:
                self.b_player_basket += self.a_player_points[5 - idx]
                self.a_player_points[5 - idx] = 0
                self.b_player_basket += 1
                self.b_player_points[idx] = 0

    def check_game_over(self):
        table = self.a_player_points if self.cur_player == "TOP" else self.b_player_points
        for pt in table:
            if pt > 0:
                return False
        return True

    def _update_baskets_endgame(self):
        if self.cur_player == "TOP":
            for i in range(len(self.b_player_points)):
                self.b_player_basket += self.b_player_points[i]
                self.b_player_points[i] = 0        
        else:
            for i in range(len(self.a_player_points)):
                self.a_player_basket += self.a_player_points[i]
                self.a_player_points[i] = 0

