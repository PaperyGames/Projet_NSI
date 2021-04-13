from Level1 import *
import pygame.freetype
from pygame.rect import Rect
from enum import Enum


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


def main():
    pygame.init()
    pygame.display.set_caption("Menu")
    Taille = pygame.display.Info()
    Larg = Taille.current_w
    Haut = Taille.current_h


    screen = pygame.display.set_mode((Larg, Haut))
    game_state = GameState.TITLE
    while True:                   
        if game_state == GameState.TITLE or game_state == 'mort':
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = Niveau1.main()

        if game_state == 'win':
            game_state = ending_screen(screen)

        if game_state == GameState.QUIT or game_state == 'quitter':
            pygame.quit()
            return


def title_screen(screen):

    Taille = pygame.display.Info()
    Larg = Taille.current_w
    Haut = Taille.current_h

    start_btn = UIElement(
        center_position=(int(960*(Larg/1920)), int(700*(Haut/1080))),
        texte=Start,
        largeur=int(405*(Larg/1920)),
        hauteur=int(99*(Haut/1080)),
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(int(960*(Larg/1920)), int(1000*(Haut/1080))),
        texte=Quit,
        largeur=int(267*(Larg/1920)),
        hauteur=int(99*(Haut/1080)),
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    pygame.mixer.music.load('Sound/Title_Screen.mp3')
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Title_Screen.mp3'), -1)
    pygame.mixer.Channel(0).set_volume(0.1)

    while True:
        mouse_up = False
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            
        screen.blit(pygame.transform.scale(Fond, (Larg,Haut)), (0,0))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        screen.blit(Cursor, (pygame.mouse.get_pos()))
        pygame.display.flip()

def ending_screen(screen):
    time = 0
    Taille = pygame.display.Info()
    Larg = Taille.current_w
    Haut = Taille.current_h

    mainmenu_btn = UIElement(
        center_position=(int(210*(Larg/1920)), int(1020*(Haut/1080))),
        texte=MainMenu,
        largeur=int(341*(Larg/1920)),
        hauteur=int(50*(Haut/1080)),
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(int(960*(Larg/1920)), int(900*(Haut/1080))),
        texte=Quit,
        largeur=int(267*(Larg/1920)),
        hauteur=int(99*(Haut/1080)),
        action=GameState.QUIT,
    )

    buttons = [mainmenu_btn, quit_btn]
    pygame.mixer.music.load('Sound/Ending.wav')
    

    while True:
        time += 1
        if time == 20:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Ending.wav'),)
            pygame.mixer.Channel(0).set_volume(0.4)
        mouse_up = False
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == QUIT: 
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

            
        screen.blit(pygame.transform.scale(Ending, (Larg,Haut)), (0,0))
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
