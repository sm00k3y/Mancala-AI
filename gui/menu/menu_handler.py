import pygame
import pygame.freetype
from gui.menu.button import Button
from gui.menu.menus import PickPlayersMenu, PickDepthMenu, PickHeurMenu
from const import FPS, WIDTH, HEIGHT, FONT, FONT_SIZE, SMALL_FONT_SIZE, TEXT_COLOR

# Pygame initialization
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala")
CLOCK = pygame.time.Clock()

BG = pygame.image.load("assets/bg.png")
font = pygame.freetype.Font(FONT, FONT_SIZE)
small_font = pygame.freetype.Font(FONT, SMALL_FONT_SIZE)


class MenuHandler:
    def __init__(self):
        self.pick_player = PickPlayersMenu(self)
        self.pick_depth = PickDepthMenu(self)
        self.pick_heur = PickHeurMenu(self)
        self.current_menu = self.pick_player
        
        # True --> Gracz, False --> AI
        self.player1 = True
        self.alpha_beta_1 = False
        self.depth_1 = -1
        self.heur1 = 0

        self.player2 = True
        self.alpha_beta_2 = False
        self.depth_2 = -1
        self.heur2 = 0

        self.top_player = True
        self.both_initialized = False

        self.running = True

    def run(self):
        while self.running:
            CLOCK.tick(FPS)
            WIN.fill((0, 0, 0))
            WIN.blit(BG, (0, 0))
            text = "Welcome to Mancala!"
            font.render_to(WIN, (570, 600), text, TEXT_COLOR)
            text = "Press ESC to quit"
            small_font.render_to(WIN, (1250, 580), text, TEXT_COLOR)

            for event in pygame.event.get():
                # Exit
                if event.type == pygame.QUIT:
                    self.running = False

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.current_menu.click(pos)
                
                # Key Pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            self.current_menu.display(WIN, font)
            pygame.display.update()
        
    def get_params(self):
        params = self.player1, self.alpha_beta_1, self.depth_1, self.heur1, \
                 self.player2, self.alpha_beta_2, self.depth_2, self.heur2, \
                 self.both_initialized
        return params

    def reset(self):
        self.player1 = True
        self.alpha_beta_1 = False
        self.depth_1 = -1
        self.heur1 = 0

        self.player2 = True
        self.alpha_beta_2 = False
        self.depth_2 = -1
        self.heur2 = 0

        self.top_player = True
        self.both_initialized = False

        self.running = True
        self.current_menu = self.pick_player
    
