import pygame.display

from pygame import Surface, Rect
from code.Const import JAN_WIDTH, JAN_HEIGHT
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.janela: Surface = pygame.display.set_mode(size=(JAN_WIDTH, JAN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.janela)
            menu.run()
            pass
