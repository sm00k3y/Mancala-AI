# from gui.main_menu import main_menu
import gui.main as game

if __name__=="__main__":
    # For windows pyinstaller
    # if getattr(sys, 'frozen', False):
    #     os.chdir(sys._MEIPASS)

    # main_menu()
    game.run()
   