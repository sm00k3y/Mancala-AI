from gui.menu.menu_handler import MenuHandler
from gui.game import Game


# Run the game
def run():
    menu = MenuHandler()

    while True:
        menu.run()
        params = menu.get_params()
        print(params)
        if params[-1] == False:
            break
        game = Game(params[:-1])
        game.run()
        menu.reset()
