import pygame
from gui.game import Game
from const import FPS, WIDTH, HEIGHT

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala")

def main():
    run = True
    clock = pygame.time.Clock()

    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.move(pos)
                
        game.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()