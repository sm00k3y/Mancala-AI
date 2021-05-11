import math
from ai.engine import GameState
import copy


class MinMax:
    def __init__(self, alpha_beta=True, depth=2, heuristic=1):
        self.gamestate = GameState()
        self.alpha_beta = alpha_beta
        self.depth = depth
        self.heur = heuristic

    def find_move(self, game_state):
        self.gamestate.update(game_state)
        _, top_move = self._minmax(self.gamestate, self.depth, -math.inf, math.inf, game_state[-1])
        return top_move

    def _minmax(self, game_state, depth, alpha, beta, maximizing_player):
        if depth == 0 or game_state.check_game_over():
            return game_state.evaluate(), -1

        top_move = -1

        if maximizing_player:
            value = -math.inf
            for move in game_state.possible_moves():
                temp_state = copy.deepcopy(game_state)
                another_move = temp_state.make_move(move)
                if another_move:
                    val, _ = self._minmax(temp_state, depth - 1, alpha, beta, maximizing_player)
                    if val > value:
                        value = val
                        top_move = move
                else:
                    temp_state.next_player()
                    val, _ = self._minmax(temp_state, depth - 1, alpha, beta, not maximizing_player)
                    if val > value:
                        value = val
                        top_move = move
                if self.alpha_beta:
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
            return value, top_move
        else:
            value = math.inf
            for move in game_state.possible_moves():
                temp_state = copy.deepcopy(game_state)
                another_move = temp_state.make_move(move)
                if another_move:
                    val, _ = self._minmax(temp_state, depth - 1, alpha, beta, maximizing_player)
                    if val < value:
                        value = val
                        top_move = move
                else:
                    temp_state.next_player()
                    val, _ = self._minmax(temp_state, depth - 1, alpha, beta, not maximizing_player)
                    if val < value:
                        value = val
                        top_move = move
                if self.alpha_beta:
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return value, top_move
        