from game.tools import draw_board, is_int, check_move

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

    def draw_board(self):
        draw_board(self.a_player_points, self.b_player_points, 
                   self.a_player_basket, self.b_player_basket)
            
    def start_game(self):
        self.cur_player = "TOP"
        while(True):
            self.game_loop()

    def game_loop(self):
        self.draw_board()

        while(True):
            move = input(f"Player {self.cur_player} move (1-6): ")
            if check_move(move):
                if not self.make_move(int(move)):
                    self._next_player()
                break
            else:
                print("WRONG NUMBER")
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
