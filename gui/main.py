import pygame
from gui.game import Game
from const import FPS, WIDTH, HEIGHT

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala")

def main():
    clock = pygame.time.Clock()

    run = True
    game_over = False

    game = Game(WIN)

    # Main Game Loop
    while run:
        clock.tick(FPS)

        if game.game_over():
            game_over = True
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.move(pos)
                
        game.update()

    # Print Game Over Screen until closed or mouse press
    while game_over:
        game.print_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                game_over = False
    
    pygame.quit()


if __name__ == "__main__":
    main()