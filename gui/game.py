import pygame
from gui.engine import Engine
from ai.min_max import MinMax
from const import WIDTH, HEIGHT, FPS, FONT, FONT_SIZE, SMALL_FONT_SIZE, AI_DEPTH
from gui.exceptions import ParametersNotInitializedException


# Pygame initialization
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala")
CLOCK = pygame.time.Clock()

BG = pygame.image.load("assets/bg.png")
font = pygame.freetype.Font(FONT, FONT_SIZE)
small_font = pygame.freetype.Font(FONT, SMALL_FONT_SIZE)


class Game:
    def __init__(self, params):
        if len(params) != 8:
            raise ParametersNotInitializedException
        self.player1 = params[0]
        self.alpha_beta1 = params[1]
        self.depth1 = params[2]
        self.heur1 = params[3]
        self.player2 = params[4]
        self.alpha_beta2 = params[5]
        self.depth2 = params[6]
        self.heur2 = params[7]

    def run(self):
        run = True
        game_over = False

        engine = Engine(WIN)
        player1 = None  # Human by default
        player2 = None  # Human by default

        if not self.player1:
            player1 = MinMax(self.alpha_beta1, self.depth1, self.heur1)

        if not self.player2:
            player2 = MinMax(self.alpha_beta2, self.depth2, self.heur2)

        # Main Game Loop
        while run:
            CLOCK.tick(FPS)

            if engine.game_over():
                engine.update_baskets_gameover()
                game_over = True
                run = False
                break

            if not engine.is_moving_anim and engine.top_player and player1 != None:
                move = player1.find_move(engine.gamestate())
                print(move)
                engine.move(pit_number=move)
            elif not engine.is_moving_anim and not engine.top_player and player2 != None:
                move = player2.find_move(engine.gamestate())
                print(move)
                engine.move(pit_number=move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (engine.top_player and player1 == None) or (not engine.top_player and player2 == None):
                        pos = pygame.mouse.get_pos()
                        engine.move(pos)

                # Key Pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    
            engine.update()

        if player1:
            print("\nPlayer 1 visited:", player1.visited_nodes, "nodes, and took", player1.sum_time, "s time")
        if player2:
            print("Player 2 visited:", player2.visited_nodes, "nodes, and took", player2.sum_time, "s time")

        # Print Game Over Screen until closed or mouse press
        while game_over:
            engine.print_game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                    game_over = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_over = False

