import pygame
from gui.game import Game
from ai.min_max import MinMax
from const import FPS, WIDTH, HEIGHT, AI_DEPTH

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala")
clock = pygame.time.Clock()


def main_loop():

    run = True
    game_over = False

    game = Game(WIN)
    ai = MinMax()

    # Main Game Loop
    while run:
        clock.tick(FPS)

        if game.game_over():
            game.update_baskets_gameover()
            game_over = True
            run = False
        elif not game.is_moving_anim and game.top_player:
            move = ai.find_move(AI_DEPTH, game.gamestate())
            print(move)
            game.move(pit_number=move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not game.top_player and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.move(pos)
                
        game.update()

    # Print Game Over Screen until closed or mouse press
    while game_over:
        game.print_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                game_over = False
    
    # pygame.quit()