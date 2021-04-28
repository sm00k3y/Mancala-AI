from game.tools import draw_board, is_int

class Game:
    def __init__(self):
        self.a_player_points = []
        self.b_player_points = []
        self.a_player_basket = 0
        self.b_player_basket = 0
        for _ in range(6):
            self.a_player_points.append(4)
            self.b_player_points.append(4)
        self.cur_player = ""
        self.game_over = False
            
    def start_game(self):
        self.cur_player = "TOP"

        while(not self.game_over):
            self.game_loop()

        self._draw_board()
        print("GAME OVER")

    def game_loop(self):
        self._draw_board()

        while(True):
            move = input(f"Player {self.cur_player} move (1-6): ")
            if self._check_move(move):
                if not self.make_move(int(move)):
                    self._next_player()
                break
            else:
                print("Wrong Number or Empty Whole!")
        print("\n")
            
    def make_move(self, move):
        idx = move - 1
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
        
        if idx > -1:  # Nie musi tutaj nawet byc tego ifa
            self._check_take(table, idx)

        if self._check_game_over():
            self.game_over = True
            self._update_baskets_endgame()
            return True
        
        return False

    def _check_move(self, move):
        if is_int(move) and int(move) > 0 and int(move) < 7:  # N here
            if (self.cur_player == "TOP" and self.a_player_points[int(move) - 1] != 0) or \
                (self.cur_player == "BOTTOM" and self.b_player_points[int(move) - 1] != 0):
                return True
        return False

    def _next_player(self):
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

    def _check_game_over(self):
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

    def _draw_board(self):
        draw_board(self.a_player_points, self.b_player_points, 
                   self.a_player_basket, self.b_player_basket)
