import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import JAN_WIDTH, JAN_HEIGHT


class Menu:
    def __init__(self, janela):
        self.janela: Surface = janela
        self.surf = pygame.image.load('./asset/Background_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/MenuSound.wav')  # falta adicionar a musica
        pygame.mixer_music.play(-1)
        while True:
            self.janela.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Nav Game", (255, 128, 0), ((JAN_WIDTH / 2), 70))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str,  text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.janela.blit(source=text_surf, dest=text_rect)
