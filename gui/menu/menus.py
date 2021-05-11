from gui.menu.button import Button


class Menu:
    def __init__(self, state):
        self.state = state
        
    def display(self, win, font):
        ...

    def click(self, pos):
        ...


class PickPlayersMenu(Menu):
    def __init__(self, state):
        super().__init__(state)
        self.but1 = Button(130, 280, 350, 150, "Player")
        self.but2 = Button(600, 280, 350, 150, "MiniMax")
        self.but3 = Button(1050, 280, 350, 150, "AlfaBeta")

    def display(self, win, font):
        text = "Pick Top Player" if self.state.top_player else "Pick Bottom Player"
        font.render_to(win, (560, 150), text, (30, 30, 200))
        self.but1.draw(win, font)
        self.but2.draw(win, font)
        self.but3.draw(win, font)
    
    def click(self, pos):
        if self.but1.is_over(pos):
            if self.state.top_player:
                self.state.player1 = True
                self.state.top_player = not self.state.top_player
            else:
                self.state.player2 = True
                self.state.both_initialized = True
                self.state.running = False
        elif self.but2.is_over(pos):
            if self.state.top_player:
                self.state.player1 = False
                self.state.alpha_beta_1 = False
            else:
                self.state.player2 = False
                self.state.alpha_beta_2 = False
            self.state.current_menu = self.state.pick_depth
        elif self.but3.is_over(pos):
            if self.state.top_player:
                self.state.player1 = False
                self.state.alpha_beta_1 = True
            else:
                self.state.player2 = False
                self.state.alpha_beta_2 = True
            self.state.current_menu = self.state.pick_depth


class PickDepthMenu(Menu):
    def __init__(self, state):
        super().__init__(state)
        self.buttons = []
        self.buttons.append(Button(130, 280, 250, 100, "1"))
        self.buttons.append(Button(460, 280, 250, 100, "2"))
        self.buttons.append(Button(790, 280, 250, 100, "3"))
        self.buttons.append(Button(1120, 280, 250, 100, "4"))
        self.buttons.append(Button(130, 450, 250, 100, "6"))
        self.buttons.append(Button(460, 450, 250, 100, "8"))
        self.buttons.append(Button(790, 450, 250, 100, "10"))
        self.buttons.append(Button(1120, 450, 250, 100, "12"))

    def display(self, win, font):
        text = "Pick Top AI Depth" if self.state.top_player else "Pick Bottom AI Depth"
        font.render_to(win, (560, 150), text, (30, 30, 200))

        for but in self.buttons:
            but.draw(win, font)
    
    def click(self, pos):
        for but in self.buttons:
            if but.is_over(pos):
                if self.state.top_player:
                    self.state.depth_1 = int(but.text)
                else:
                    self.state.depth_2 = int(but.text)
                self.state.current_menu = self.state.pick_heur
                return


class PickHeurMenu(Menu):
    def __init__(self, state):
        super().__init__(state)
        self.heur1 = Button(550, 280, 350, 150, "Default")

    def display(self, win, font):
        text = "Pick Heuristic for Top AI" if self.state.top_player else "Pick Heuristic fot Bottom AI"
        font.render_to(win, (560, 150), text, (30, 30, 200))

        self.heur1.draw(win, font)

    def click(self, pos):
        if self.heur1.is_over(pos):
            if self.state.top_player:
                self.state.heur1 = 1
                self.state.top_player = not self.state.top_player
                self.state.current_menu = self.state.pick_player
            else:
                self.state.heur2 = 1
                self.state.both_initialized = True
                self.state.running = False