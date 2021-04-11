from Level1 import *
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

Fond = pygame.image.load('Title/Fond.png')
Start = pygame.image.load('Title/Start.png')
Quit = pygame.image.load('Title/Quit.png')
Cursor = pygame.image.load('Title/Cursor.png')

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)


class UIElement(Sprite):

    def __init__(self, center_position, texte, largeur, hauteur, action=None):
 
        self.mouse_over = False 

        ImageBase = pygame.transform.scale(texte, (largeur, hauteur))
        ImageSurligne = pygame.transform.scale(texte, (int(largeur * 1.2), int(hauteur * 1.2)))
        self.images = [ImageBase, ImageSurligne]
        self.rects = [ImageBase.get_rect(center=center_position), ImageSurligne.get_rect(center=center_position),]
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


def main():
    pygame.init()
    pygame.display.set_caption("Menu")

    pygame.mixer.music.load('Sound/Title_Screen.mp3')
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Title_Screen.mp3'), -1)
    pygame.mixer.Channel(0).set_volume(0.1)

    screen = pygame.display.set_mode((2135, 1200))
    game_state = GameState.TITLE
    while True:                   
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = Niveau1.main()

        if game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen):
    start_btn = UIElement(
        center_position=(1067, 700),
        texte=Start,
        largeur=405,
        hauteur=99,
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(1067, 1000),
        texte=Quit,
        largeur=267,
        hauteur=99,
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == QUIT: 
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            
        screen.blit(pygame.transform.scale(Fond, (2135,1200)), (0,0))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        screen.blit(Cursor, (pygame.mouse.get_pos()))
        pygame.display.flip()


# call main when the script is run
if __name__ == "__main__":
    main()


    
            
