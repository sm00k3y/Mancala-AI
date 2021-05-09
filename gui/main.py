from gui.menu.menu_handler import MenuHandler

# Run the game
def run():
    menu = MenuHandler()
    # game = Game()

    while True:
        menu.run()
        params = menu.get_params()
        print(params)
        if params[-1] == False:
            break
        # game.run(params)
