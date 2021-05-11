class ParametersNotInitializedException(Exception):
    def __init__(self):
        super().__init__("Try passing parameters to the game object constructor")