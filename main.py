from gui.main import main_loop

if __name__=="__main__":
    # For windows pyinstaller
    # if getattr(sys, 'frozen', False):
    #     os.chdir(sys._MEIPASS)

    main_loop()