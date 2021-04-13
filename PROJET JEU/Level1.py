import pygame
from pygame.locals import *
from pygame.sprite import Sprite

Fond = pygame.image.load('Graphics/Fonds/Fond.png')
Start = pygame.image.load('Graphics/Fonds/Start.png')
Quit = pygame.image.load('Graphics/Fonds/Quit.png')
MenuPause = pygame.image.load('Graphics/Fonds/Pause.png')
Continue = pygame.image.load('Graphics/Fonds/Continue.png')
MainMenu = pygame.image.load('Graphics/Fonds/MainMenu.png')
Ending = pygame.image.load('Graphics/Fonds/Ending.png')
Cursor = pygame.image.load('Graphics/Fonds/Cursor.png')


class Level1():

    def __init__(self):
        self.scroll = [0,0]

        #Graphics
        self.bg = self.background = pygame.image.load("Graphics/Fonds/Fond_2.jpg")
        self.fg = self.foreground = pygame.image.load("Graphics/Levels/Niveau_1.png")
        self.Pause = False
            

    def AffichageFenetre(self):
        self.screen.blit(self.bg, (0 - self.scroll[0]/4,0))
        self.screen.blit(self.fg, (0 - self.scroll[0],-200))
        self.drapeau.dessiner(self.screen)
        self.player.dessiner(self.screen)
        if not self.drapeau.consomme:
            self.dino1.dessiner(self.screen)
            self.dino2.dessiner(self.screen)
            self.dino3.dessiner(self.screen)
            self.dino4.dessiner(self.screen)
            self.champi1.dessiner(self.screen)
            self.champi2.dessiner(self.screen)
        self.bloc1.dessiner(self.screen)
        self.bloc5.dessiner(self.screen)
        pygame.display.update()
    
    def Pause_screen(self):
        self.continue_btn = UIElement(
            center_position=(int(960*(self.Larg/1920)), int(550*(self.Haut/1080))),
            texte=Continue,
            largeur=int(573*(self.Larg/1920)),
            hauteur=int(100*(self.Haut/1080)),
            action='Continue'
            )
        self.main_btn = UIElement(
            center_position=(int(960*(self.Larg/1920)), int(750*(self.Haut/1080))),
            texte=MainMenu,
            largeur=int(683*(self.Larg/1920)),
            hauteur=int(100*(self.Haut/1080)),
            action='MainMenu'
            )

        self.buttons = [self.continue_btn, self.main_btn]

        while True:
            self.mouse_up = False
            for event in pygame.event.get():
                if event.type == QUIT: 
                    return('quitter')

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouse_up = True
                                
            self.screen.blit(pygame.transform.scale(MenuPause, (int(1600*(self.Larg/1920)), int(743*(self.Haut/1080)))), (int(160*(self.Larg/1920)),int(168*(self.Haut/1080))))
            for button in self.buttons:
                self.ui_action = button.update(pygame.mouse.get_pos(), self.mouse_up)
                if self.ui_action is not None:
                    return self.ui_action
                button.draw(self.screen)
            self.pos = (pygame.mouse.get_pos())
            if self.pos[0] > int(160*(self.Larg/1920)) and self.pos[1] > int(168*(self.Haut/1080)) and self.pos[0] < int(1760*(self.Larg/1920)) - 68 and self.pos[1] < int(912*(self.Haut/1080)) - 69:
                pygame.mouse.set_visible(False)
                self.screen.blit(Cursor, (pygame.mouse.get_pos()))
            else:
                pygame.mouse.set_visible(True)
            pygame.display.flip()


    #Main loop
    def main(self):
        if not pygame.get_init():
            pygame.init()
        pygame.display.set_caption("Niveau1")
        self.Taille = pygame.display.Info()
        self.Larg = self.Taille.current_w
        self.Haut = self.Taille.current_h
        self.screen = pygame.display.set_mode((self.Larg, self.Haut))
        
        #Graphics
        self.bg.convert()
        self.fg.convert_alpha()

        self.clock = pygame.time.Clock()
        pygame.display.flip()
        self.scroll = [0,0]
        self.player = player(int(120*(self.Larg/1920)),int(900*(self.Haut/1080)),150,150)
        self.dino1 = rex(int(700*(self.Larg/1920)),int(900*(self.Haut/1080)),150,150,int(1200*(self.Larg/1920)))
        self.dino2 = rex(int(1520*(self.Larg/1920)),int(386*(self.Haut/1080)),150,150,int(1940*(self.Larg/1920)))
        self.dino3 = rex(int(5850*(self.Larg/1920)),int(900*(self.Haut/1080)),150,150,int(6990*(self.Larg/1920)))
        self.dino4 = rex(int(7000*(self.Larg/1920)),int(730*(self.Haut/1080)),150,150,int(8000*(self.Larg/1920)))
        self.sol1 = sol(0,int(1020*(self.Haut/1080)),72.6*(self.Larg/1920),3,"bloc",False)
        self.sol2 = sol(int(1320*(self.Larg/1920)),int(764*(self.Haut/1080)),8*(self.Larg/1920),2*(self.Haut/1080),"travers",False)
        self.sol3 = sol(int(1520*(self.Larg/1920)),int(506*(self.Haut/1080)),11.4*(self.Larg/1920),2*(self.Haut/1080),"travers",False)
        self.sol4 = sol(int(2120*(self.Larg/1920)),int(764*(self.Haut/1080)),8*(self.Larg/1920),2*(self.Haut/1080),"travers",False)
        self.sol5 = sol(int(4760*(self.Larg/1920)),int(1020*(self.Haut/1080)),39*(self.Larg/1920),3*(self.Haut/1080),"bloc",False)
        self.sol6 = sol(int(6990*(self.Larg/1920)),int(850*(self.Haut/1080)),39*(self.Larg/1920),6*(self.Haut/1080),"bloc",False)
        self.bloc1 = sol(int(415*(self.Larg/1920)),int(760*(self.Haut/1080)),1.1*(self.Larg/1920),1.1*(self.Haut/1080),"bloc",True)
        self.bloc2 = sol(int(3495*(self.Larg/1920)),int(830*(self.Haut/1080)),2.2*(self.Larg/1920),3*(self.Haut/1080),"bloc",False)
        self.bloc3 = sol(int(5260*(self.Larg/1920)),int(830*(self.Haut/1080)),2.2*(self.Larg/1920),3*(self.Haut/1080),"bloc",False)
        self.bloc4 = sol(int(5700*(self.Larg/1920)),int(675*(self.Haut/1080)),2.2*(self.Larg/1920),5.6*(self.Haut/1080),"bloc",False)
        self.bloc5 = sol(int(3900*(self.Larg/1920)),int(760*(self.Haut/1080)),1.1*(self.Larg/1920),1.1*(self.Haut/1080),"bloc",True)
        self.champi1 = objet(int(415*(self.Larg/1920)),int(760*(self.Haut/1080)),"Champi")
        self.champi2 = objet(int(3900*(self.Larg/1920)),int(760*(self.Haut/1080)),"Champi")
        self.drapeau = objet(int(8000*(self.Larg/1920)),int(172*(self.Haut/1080)),"Drapeau")
        self.continuer = True
        #Sounds 
        pygame.mixer.music.load('Sound/First_Level.mp3')
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/First_Level.mp3'), -1)
        pygame.mixer.Channel(0).set_volume(0.1)
        pygame.mixer.music.load('Sound/Jump.wav')
        pygame.mixer.music.load('Sound/Pause.wav')
        pygame.mixer.music.load('Sound/Kick.wav')
        pygame.mixer.music.load('Sound/Kick.wav')
        pygame.mixer.music.load('Sound/Appear.wav')
        pygame.mixer.music.load('Sound/Dead.wav')
        pygame.mixer.music.load('Sound/Clear_Level.mp3')
        pygame.mixer.music.load('Sound/Upgrade.wav')
        pygame.mixer.music.load('Sound/Damage.wav')
        
        while self.continuer:
            
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT: 
                    self.continuer = False
                    return('quitter')
                

            if not self.player.mort and not self.Pause and not self.drapeau.consomme:
                if self.player.hitbox[0] + self.player.hitbox[2] > 1000 and self.player.droite and self.scroll[0] + 960 < self.drapeau.x:
                    self.scroll[0] += self.player.vitesse
                elif self.player.hitbox[0] < 900 and self.player.gauche and self.scroll[0] > 0:
                    self.scroll[0] -= self.player.vitesse

                self.keys = pygame.key.get_pressed()


                if self.keys[pygame.K_ESCAPE]:
                    self.Pause = True
                    pygame.mixer.Channel(0).set_volume(0.03)
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound('Sound/Pause.wav'))
                    

                if self.keys[pygame.K_LSHIFT]:
                    if not self.player.gauche and not self.player.droite:
                        self.player.vitesse = 0
                    elif self.player.vitesse < 24:
                        self.player.vitesse += 1 
                else:
                    if self.player.vitesse > 13:
                        self.player.vitesse -= 1

                if self.keys[pygame.K_LEFT] and self.player.x > 50 + self.player.vitesse:
                    if not self.player.OnWall:
                        self.player.x -= self.player.vitesse
                        if self.player.droite:
                            self.player.vitesse = 0
                            self.player.tourne = True
                        if self.player.vitesse < 13:
                            self.player.vitesse += 1
                    self.player.gauche = True
                    self.player.droite = False

                elif self.keys[pygame.K_RIGHT] and self.player.hitbox[0] + self.player.hitbox[2] < self.drapeau.x + 960 - self.scroll[0] - self.player.vitesse:
                    if not self.player.OnWall:
                        self.player.x += self.player.vitesse
                        if self.player.gauche:
                            self.player.vitesse = 0
                            self.player.tourne = True
                        if self.player.vitesse < 13:
                            self.player.vitesse += 1
                    self.player.gauche = False
                    self.player.droite = True
                else :
                    if self.player.gauche:
                        self.player.x -= self.player.vitesse - 1
                    if self.player.droite:
                        self.player.x += self.player.vitesse - 1
                    if self.player.vitesse > 0:
                        self.player.vitesse -= 1
                    self.player.gauche = False
                    self.player.droite = False
                    self.player.ComptMarche = 0

                if self.keys[pygame.K_SPACE] or self.keys[pygame.K_UP]:
                    if self.player.OnGround:
                        self.player.InJump = True 

                self.champi1.spawn(self.bloc1)
                self.champi1.contact(self.player)
                self.champi1.interaction(self.bloc1)
                self.champi1.interaction(self.bloc2)
                self.champi1.interaction(self.sol1)
                self.champi2.spawn(self.bloc5)
                self.champi2.contact(self.player)
                self.champi2.interaction(self.bloc5)
                self.champi2.interaction(self.sol1)
                self.dino1.contact(self.player)
                self.dino1.rebond(self.player)
                self.dino2.contact(self.player)
                self.dino2.rebond(self.player)
                self.dino3.contact(self.player)
                self.dino3.rebond(self.player)
                self.dino4.contact(self.player)
                self.dino4.rebond(self.player)
                self.champi1.chute()
                self.champi2.chute()
                            
            if not self.Pause:
                self.drapeau.contact(self.player)
                self.bloc1.interaction(self.player)
                self.bloc2.interaction(self.player)
                self.bloc3.interaction(self.player)
                self.bloc4.interaction(self.player)
                self.bloc5.interaction(self.player)
                self.sol1.interaction(self.player)
                self.sol2.interaction(self.player) 
                self.sol3.interaction(self.player)
                self.sol4.interaction(self.player)
                self.sol5.interaction(self.player)
                self.sol6.interaction(self.player)
                if not self.player.mort:
                    self.player.saut()
                    self.player.chute()
                self.AffichageFenetre()
            else:
                self.Action = self.Pause_screen()
                if self.Action == 'MainMenu':
                    self.Pause = False
                    return('mort')
                elif self.Action == 'quitter':
                    self.Pause = False
                    return('quitter')
                elif self.Action == 'Continue':
                    self.Pause = False
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound('Sound/Pause.wav'))
                    pygame.mixer.Channel(0).set_volume(0.1)
            
            if not pygame.mixer.Channel(0).get_busy():
                if self.player.mort:
                    return('mort')
                elif self.player.Win:
                    return('win')

class player():
    BPerso = pygame.image.load('Graphics/Right/Big/Idle.png') 
    BMarche = [pygame.image.load('Graphics/Right/Big/Walk1.png'), pygame.image.load('Graphics/Right/Big/Walk2.png')]
    BCourse = [pygame.image.load('Graphics/Right/Big/Run1.png'), pygame.image.load('Graphics/Right/Big/Run2.png'), pygame.image.load('Graphics/Right/Big/Run3.png')]
    BSautCourse = pygame.image.load('Graphics/Right/Big/Run_Jump.png')
    BSaut = [pygame.image.load('Graphics/Right/Big/Jump1.png'), pygame.image.load('Graphics/Right/Big/Jump2.png')]
    BTourne = pygame.image.load('Graphics/Right/Big/Turn.png')
    BWin = pygame.image.load('Graphics/Right/Big/Win.png')
    SPerso = pygame.image.load('Graphics/Right/Small/Idle.png')
    SMarche = [pygame.image.load('Graphics/Right/Small/Walk1.png'), pygame.image.load('Graphics/Right/Small/Idle.png')]
    SCourse = [pygame.image.load('Graphics/Right/Small/Run1.png'), pygame.image.load('Graphics/Right/Small/Run2.png')]
    SSautCourse = pygame.image.load('Graphics/Right/Small/Run_Jump.png')
    SSaut = [pygame.image.load('Graphics/Right/Small/Jump1.png'), pygame.image.load('Graphics/Right/Small/Jump2.png')]
    STourne = pygame.image.load('Graphics/Right/Small/Turn.png')
    SWin = pygame.image.load('Graphics/Right/Small/Win.png')
    Dead = [pygame.image.load('Graphics/Right/Dead1.png'), pygame.image.load('Graphics/Right/Dead2.png')]
    def __init__(self, x, y, hauteur, largeur):
        
        self.x = x
        self.y = y
        self.hauteur = hauteur
        self.largeur = largeur
        self.vitesse = 0
        self.InJump = False
        self.ComptSaut = 10
        self.boost = 0.75
        self.gauche = False
        self.droite = False
        self.ComptMarche = 0
        self.ComptCourse = 0
        self.persoA=self.SPerso
        self.tourne = False
        self.ComptTourne = 0
        self.hitbox = [self.x, self.y, 65, 120]
        self.OnGround = True
        self.ComptRebond = 8
        self.InRebond = False
        self.ComptHauteur = self.ComptSaut
        self.OnWall = False
        self.vie = 1
        self.invincible = False
        self.ComptInvincible = 0
        self.mort = False
        self.ComptMort = 0
        self.Win = False
        self.ComptWin = 0
        self.WinPose = False
        


    def saut(self):
        if self.InJump and not self.InRebond:
            if self.OnGround:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sound/Jump.wav'))
                pygame.mixer.Channel(1).set_volume(0.5)
            self.OnGround = False
            if self.ComptSaut >= 0:
                if self.vitesse == 24 and self.ComptSaut == 10:
                    self.boost = 0.85
                self.y -= (self.ComptSaut ** 2) * self.boost
                self.ComptSaut -= 1
            else:
                self.boost = 0.75
                self.OnGround = False
                self.InJump = False

    def chute(self):
        if not self.OnGround:
            if self.ComptSaut <= 0:
                self.y +=  0.75 * (self.ComptSaut ** 2)
                if self.ComptSaut > -8:
                    self.ComptSaut -= 1
            if self.ComptRebond <= 0:
                self.y +=  0.75 * (self.ComptRebond ** 2)
                if self.ComptRebond > -8:
                    self.ComptRebond -= 1
                
            
    def dessiner(self, screen):

        if self.hitbox[1] >= 1300:
            if not self.mort:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Dead.wav'), 0)
                pygame.mixer.Channel(0).set_volume(0.5)
                self.mort = True
            
 
        if self.Win:
            self.ComptWin += 1
            if self.ComptWin < 70:
                if self.OnGround:
                    if self.vitesse < 13:
                        self.vitesse += 1
                    self.x += self.vitesse
                    self.gauche = False
                    self.droite = True
            elif self.ComptWin < 180:
                self.vitesse = 0
                if self.ComptWin == 70:
                    self.gauche = True
                else:
                    self.gauche = False
                self.droite = False
            else:
                self.WinPose = True
                self.gauche= False
                self.droite = False
            
        if self.invincible:
            if self.ComptInvincible <= 40:
                self.ComptInvincible += 1
            else:
                self.invincible = False
                self.ComptInvincible = 0

        if self.vie == 0 and not self.mort:
            self.mort = True
            self.ComptHauteur = 8
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Dead.wav'), 0)
            pygame.mixer.Channel(0).set_volume(0.5)
        if self.mort and not self.hitbox[1] >= 1300:
            self.ComptMort += 1
            if self.ComptMort < 20:
                screen.blit(pygame.transform.scale(self.Dead[0], (80, 100)), (self.x - Niveau1.scroll[0], self.y))
            elif self.ComptMort < 28:
                self.y -= self.ComptHauteur ** 2
                self.ComptHauteur -= 1
                screen.blit(pygame.transform.scale(self.Dead[(self.ComptMort // 2) % 2], (80, 100)), (self.x - Niveau1.scroll[0], self.y))
            else:
                self.y += self.ComptHauteur ** 2
                if self.ComptHauteur > -7:
                    self.ComptHauteur -= 1
                screen.blit(pygame.transform.scale(self.Dead[(self.ComptMort // 2) % 2], (80, 100)), (self.x - Niveau1.scroll[0], self.y))
                
        if self.vie == 2:
            if self.ComptMarche +1 >= 14:
                self.ComptMarche = 0
            if self.ComptCourse +1 >= 9:
                self.ComptCourse = 0
            if self.ComptTourne +1 >= 5:
                self.ComptTourne = 0
                self.tourne = False


            if self.persoA == self.SPerso:
                self.persoA = self.BPerso

            if not self.WinPose:   
                if not self.invincible or (self.ComptInvincible % 4) // 2 != 0: 
                    if self.gauche:
                        self.persoA = pygame.transform.flip(self.BPerso, True, False)
                        if self.vitesse == 24:
                            if not self.OnGround:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.BSautCourse, (80, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.BTourne, (70, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.BCourse[self.ComptCourse // 3], (75, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptCourse += 1
                                    self.ComptMarche = 0
                        else:
                            if not self.OnGround:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.BSaut[2 - ((self.ComptSaut + 21) // 10)], (65, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.BTourne, (70, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.BMarche[self.ComptMarche // 7], (70, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche += 1
                                    self.ComptCourse = 0
                        
                    elif self.droite:
                        self.persoA = self.BPerso
                        if self.vitesse == 24:
                            if not self.OnGround:
                                screen.blit(pygame.transform.scale(self.BSautCourse, (80, 120)), (self.x - Niveau1.scroll[0], self.y))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.scale(self.BTourne, (70, 120)), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.scale(self.BCourse[self.ComptCourse // 3], (75, 120)), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptCourse += 1
                                    self.ComptMarche = 0
                        else:
                            if not self.OnGround:
                                screen.blit(pygame.transform.scale(self.BSaut[2 - ((self.ComptSaut + 21) // 10)], (70, 120)), (self.x - Niveau1.scroll[0], self.y))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.scale(self.BTourne, (70, 120)), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.scale(self.BMarche[self.ComptMarche // 7], (70, 120)), (self.x - Niveau1.scroll[0], self.y))
                                    self.ComptMarche += 1
                                    self.ComptCourse = 0

                    else:
                        if not self.OnGround:
                            if self.persoA == self.BPerso:
                                screen.blit(pygame.transform.scale(self.BSaut[2 - ((self.ComptSaut + 21) // 10)], (65, 120)), (self.x - Niveau1.scroll[0], self.y))
                            else:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.BSaut[2 - ((self.ComptSaut + 21) // 10)], (65, 120)), True, False), (self.x - Niveau1.scroll[0], self.y))
                        else:
                            screen.blit(pygame.transform.scale(self.persoA, (65, 120)), (self.x - Niveau1.scroll[0],self.y))
                        self.ComptMarche = 0
                        self.ComptCourse = 0
                self.hitbox = [self.x - Niveau1.scroll[0], self.y, 65, 120]
            else:
                screen.blit(pygame.transform.scale(self.BWin, (75, 130)), (self.x - Niveau1.scroll[0], self.y - 10))


        elif self.vie == 1:
            if self.ComptMarche +1 >= 14:
                self.ComptMarche = 0
            if self.ComptCourse +1 >= 6:
                self.ComptCourse = 0
            if self.ComptTourne +1 >= 5:
                self.ComptTourne = 0
                self.tourne = False

            if self.persoA == self.BPerso:
                self.persoA = self.SPerso

            if not self.WinPose:  
                if not self.invincible or (self.ComptInvincible % 4) // 2 != 0:
                    if self.gauche:
                        self.persoA = pygame.transform.flip(self.SPerso, True, False)
                        if self.vitesse == 24:
                            if not self.OnGround:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.SSautCourse, (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.STourne, (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.SCourse[self.ComptCourse // 3], (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptCourse += 1
                                    self.ComptMarche = 0
                        else:
                            if not self.OnGround:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.SSaut[2 - ((self.ComptSaut + 21) // 10)], (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.STourne, (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.SMarche[self.ComptMarche // 7], (70, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche += 1
                                    self.ComptCourse = 0
                        
                    elif self.droite:
                        self.persoA = self.SPerso
                        if self.vitesse == 24:
                            if not self.OnGround:
                                screen.blit(pygame.transform.scale(self.SSautCourse, (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.scale(self.STourne, (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.scale(self.SCourse[self.ComptCourse // 3], (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptCourse += 1
                                    self.ComptMarche = 0
                        else:
                            if not self.OnGround:
                                screen.blit(pygame.transform.scale(self.SSaut[2 - ((self.ComptSaut + 21) // 10)], (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                self.ComptMarche = 0
                                self.ComptCourse = 0
                            else:
                                if self.tourne:
                                    screen.blit(pygame.transform.scale(self.STourne, (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche = 0
                                    self.ComptCourse = 0
                                    self.ComptTourne += 1
                                else:   
                                    screen.blit(pygame.transform.scale(self.SMarche[self.ComptMarche // 7], (70, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                                    self.ComptMarche += 1
                                    self.ComptCourse = 0

                    else:
                        if not self.OnGround:
                            if self.persoA == self.SPerso:
                                screen.blit(pygame.transform.scale(self.SSaut[2 - ((self.ComptSaut + 21) // 10)], (65, 80)), (self.x - Niveau1.scroll[0], self.y + 40))
                            else:
                                screen.blit(pygame.transform.flip(pygame.transform.scale(self.SSaut[2 - ((self.ComptSaut + 21) // 10)], (65, 80)), True, False), (self.x - Niveau1.scroll[0], self.y + 40))
                        else:
                            screen.blit(pygame.transform.scale(self.persoA, (65, 80)), (self.x - Niveau1.scroll[0],self.y + 40))
                        self.ComptMarche = 0
                        self.ComptCourse = 0
                self.hitbox = [self.x - Niveau1.scroll[0], self.y + 55, 65, 65]
            else:
                screen.blit(pygame.transform.scale(self.SWin, (80, 90)), (self.x - Niveau1.scroll[0], self.y + 30))

                

class rex():
    
    Marche2 = [pygame.image.load('Graphics/Monstres/Rex/MarcheDebout1.png'), pygame.image.load('Graphics/Monstres/Rex/MarcheDebout2.png')]
    Marche1 = [pygame.image.load('Graphics/Monstres/Rex/MarcheAssis1.png'), pygame.image.load('Graphics/Monstres/Rex/MarcheAssis2.png')]
    KO = pygame.image.load('Graphics/Monstres/Rex/Mort.png')
    Etat = [KO, Marche1, Marche2]

    def __init__(self, x, y, hauteur, largeur, fin):
        self.x = x
        self.y = y
        self.hauteur = hauteur
        self.largeur = largeur
        self.fin = fin
        self.vie = 2
        self.chemin = [self.x, self.fin]
        self.ComptMarche = 0
        self.vitesse = 5
        self.hitbox = [self.x, self.y, 65, 120]
        self.ComptMort = 0
        self.Mort = False
        self.GrandRebond = False
        self.OnMonster = False
        self.AuDessus = False
        
    def dessiner(self, screen):
        if not self.Mort:
            self.bouge()
            if self.ComptMarche +1 >= 10:
                self.ComptMarche = 0
            if self.ComptMort +1 >= 15:
                self.Mort = True

            if self.vitesse > 0:
                if self.vie > 0:
                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.Etat[self.vie][self.ComptMarche // 5], (70, 120 - 60 * (2 - self.vie))), True, False), (self.x - Niveau1.scroll[0], self.y + 60 * (2 - self.vie)))
                    self.ComptMarche += 1
                else:
                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.Etat[self.vie], (70, 30)), True, False), (self.x - Niveau1.scroll[0], self.y + 90))
                    self.ComptMort += 1   
            else:
                if self.vie > 0:
                    screen.blit(pygame.transform.scale(self.Etat[self.vie][self.ComptMarche // 5], (70,120 - 60 * (2 - self.vie))), (self.x - Niveau1.scroll[0], self.y + 60 * (2 - self.vie)))
                    self.ComptMarche += 1
                else:
                    screen.blit(pygame.transform.scale(self.Etat[self.vie], (70, 30)), (self.x - Niveau1.scroll[0], self.y + 90))
                    self.ComptMort += 1
            self.hitbox = [self.x - Niveau1.scroll[0], self.y + 60 * (2 - self.vie), 65, 120 - 60 * (2 - self.vie)]
            

    def bouge(self):
        if self.ComptMort == 0:
            if self.vitesse > 0:
                if self.x + self.vitesse < self.chemin[1]:
                    self.x += self.vitesse
                else:
                    self.vitesse = self.vitesse * -1
                    self.ComptMarche = 0
            else:
                if self.x + self.vitesse > self.chemin[0]:
                    self.x += self.vitesse
                else:
                    self.vitesse = self.vitesse * -1
                    self.ComptMarche = 0

    def contact(self, player):
        if self.vie > 0:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                if (player.ComptSaut < 0 or player.ComptRebond < 0) and (player.hitbox[1] + player.hitbox[3] + 0.75 * (player.ComptSaut ** 2) or player.hitbox[1] + player.hitbox[3] + 0.75 * (player.ComptRebond ** 2)) >= self.hitbox[1] and self.AuDessus:
                    self.vie -= 1
                    self.OnMonster = True
                    player.InRebond = True
                    self.AuDessus = False
                    player.ComptSaut = 9
                    player.ComptRebond = 8
                elif player.hitbox[1] > self.hitbox[1] + self.hitbox[3]:
                    self.AuDessus = False
                    self.OnMonster = False
                elif player.hitbox[1] + player.hitbox[3] < self.hitbox[1]:
                    self.AuDessus = True
                    self.OnMonster = False
            else:
                self.AuDessus = False
                self.OnMonster = False
            if not player.invincible:
                if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
                    self.ACote = True
                else:
                    self.ACote = False
                if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2] and self.ACote:
                    player.vie -= 1
                    player.invincible = True
                    if player.vie > 0:
                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('Sound/Damage.wav'))
                        pygame.mixer.Channel(6).set_volume(0.5)
                    
        else:
            self.AuDessus = False
            self.OnMonster = False
        

    def rebond(self, player):
        if player.InRebond:
            if self.OnMonster:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sound/Kick.wav'))
                pygame.mixer.Channel(1).set_volume(0.5)
            if Niveau1.keys[pygame.K_SPACE] or Niveau1.keys[pygame.K_UP] and player.ComptRebond == 8:
                self.GrandRebond = True
            if self.GrandRebond:
                if player.ComptSaut > 0:
                    player.y -= (player.ComptSaut ** 2) * 0.8
                    player.ComptSaut -= 1
                else:
                    player.InRebond = False
                    self.GrandRebond = False
                    player.OnGround = False
            else:       
                if player.ComptRebond >= 0:
                    player.y -= 3 * ((player.ComptRebond / 2) ** 2)
                    player.ComptRebond -= 1
                else:
                    player.InRebond = False
                    self.OnMonster = False
                    player.OnGround = False
                    
            
        



class sol():

    Bloc = [pygame.image.load('Graphics/Objets/Bloc/Bloc1.png'), pygame.image.load('Graphics/Objets/Bloc/Bloc2.png'), pygame.image.load('Graphics/Objets/Bloc/Bloc3.png'), pygame.image.load('Graphics/Objets/Bloc/Bloc4.png')]
    Used = pygame.image.load('Graphics/Objets/Bloc/Used.png')
    
    def __init__(self, x, y, blocL, blocH, mode, contient): #2 modes différents : bloc et travers
        self.x = x
        self.y = y
        self.hauteur = 60 * blocH
        self.largeur = 60 * blocL
        self.mode = mode
        self.hitbox = [self.x, self.y, self.largeur, self.hauteur]
        self.AuDessus = False
        self.EnDessous = False
        self.AGauche = False
        self.ADroite = False
        self.Sur = False
        self.Cogne = False
        self.contient = contient
        self.ComptBloc = 0
        self.Utilise = False
        

    def interaction(self, objet):
        self.hitbox[0] = self.x - Niveau1.scroll[0]
        if self.mode == "travers":
            if objet.ComptSaut <= 0 or objet.ComptRebond <=0: 
                if objet.hitbox[0] + objet.hitbox[2] > self.hitbox[0] and objet.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                    if self.hitbox[1] >= objet.hitbox[1] + objet.hitbox[3]:
                        self.AuDessus = True
                    else:
                        self.AuDessus = False
                    if self.AuDessus:
                        if objet.hitbox[1] + objet.hitbox[3] + 0.75 * (objet.ComptSaut ** 2) >= self.hitbox[1] or objet.hitbox[1] + objet.hitbox[3] + 0.75 * (objet.ComptRebond ** 2) >= self.hitbox[1]:
                            objet.y = self.hitbox[1] - 120
                            objet.ComptSaut = 10
                            objet.ComptRebond = 8
                            objet.OnGround = True
                            objet.InJump = False
                            objet.InRebond = False
                            self.Sur = True
                        else:
                            objet.OnGround = False
                            objet.InJump = False
                            objet.InRebond = False
                else:
                    objet.OnGround = False
            elif objet.y == self.hitbox[1] - 120 and self.Sur:
                if not objet.hitbox[0] + objet.hitbox[2] >= self.hitbox[0] or not objet.hitbox[0] <= self.hitbox[0] + self.hitbox[2]:
                    objet.OnGround = False
                    objet.ComptSaut = 0
                    self.Sur = False
        elif self.mode == "bloc":
            if objet.hitbox[0] + objet.hitbox[2] >= self.hitbox[0] and objet.hitbox[0] <= self.hitbox[0] + self.hitbox[2]:
                self.ADroite = False
                self.AGauche = False
                if objet.hitbox[1] >= self.hitbox[1] + self.hitbox[3]:
                    self.AuDessus = False
                    self.EnDessous = True
                elif self.hitbox[1] >= objet.hitbox[1] + objet.hitbox[3]:
                    self.AuDessus = True
                    self.EnDessous = False
            elif objet.hitbox[1] + objet.hitbox[3] >= self.hitbox[1] and objet.hitbox[1] <= self.hitbox[1] + self.hitbox[3]:
                self.AuDessus = False
                self.EnDessous = False
                if objet.hitbox[0] >= self.hitbox[0] + self.hitbox[2]:
                    self.ADroite = True
                    self.AGauche = False
                elif self.hitbox[0] >= objet.hitbox[0] + objet.hitbox[2]:
                    self.ADroite = False
                    self.AGauche = True
            else:
                self.AuDessus = False
                self.EnDessous = False
                self.AGauche = False
                self.ADroite = False
            if (objet.ComptSaut <= 0 or objet.ComptRebond <= 0) and (objet.hitbox[1] + objet.hitbox[3] + 0.75 * (objet.ComptSaut ** 2) >= self.hitbox[1] or objet.hitbox[1] +objet.hitbox[3] + 0.75 * (objet.ComptRebond ** 2) >= self.hitbox[1]) and self.AuDessus:
                objet.ComptSaut = 10
                objet.ComptRebond = 8
                objet.OnGround = True
                objet.InJump = False
                objet.InRebond = False
                self.Sur = True
                objet.y = self.hitbox[1] - 120
                objet.OnWall = False
                self.Cogne = False
            elif (objet.ComptSaut > 0 or objet.ComptRebond > 0) and objet.hitbox[1] <= self.hitbox[1] + self.hitbox[3] and self.EnDessous:
                self.Cogne = True
                self.Utilise = True
                objet.ComptSaut = 0
                objet.ComptRebond = 0
                objet.InJump = False
                objet.InRebond = False
                objet.OnWall = False
                objet.y = self.hitbox[1] + self.hitbox[3]
            elif objet.hitbox[0] + objet.hitbox[2] + objet.vitesse >= self.hitbox[0] and self.AGauche and (objet.droite or objet.tourne):
                objet.x = self.hitbox[0] - objet.hitbox[2] + Niveau1.scroll[0] 
                objet.vitesse = 0
                objet.OnWall = True
                self.Cogne = False
            elif objet.hitbox[0] - objet.vitesse <= self.hitbox[0] + self.hitbox[2] and self.ADroite and (objet.gauche or objet.tourne):
                objet.x = self.hitbox[0] + self.hitbox[2] + Niveau1.scroll[0] 
                objet.vitesse = 0
                objet.OnWall = True
                self.Cogne = False
            else:
                objet.OnWall = False
                self.Cogne = False
            if objet.y == self.hitbox[1] - 120 and self.Sur:
                if not objet.hitbox[0] + objet.hitbox[2] >= self.hitbox[0] or not objet.hitbox[0] <= self.hitbox[0] + self.hitbox[2]:
                    objet.OnGround = False
                    objet.ComptSaut = 0
                    self.Sur = False

    def dessiner(self, screen):
        if self.contient:
            if not self.Utilise:
                if self.ComptBloc <= 12:
                    self.ComptBloc += 1
                else:
                    self.ComptBloc = 0
                screen.blit(pygame.transform.scale(self.Bloc[self.ComptBloc // 4], (75, 75)), (self.x - Niveau1.scroll[0], self.y)) 
            else:
                screen.blit(pygame.transform.scale(self.Used, (75, 75)), (self.x - Niveau1.scroll[0], self.y))




class objet():
    Champi = pygame.image.load('Graphics/Objets/Champi.png')
    Drapeau = pygame.image.load('Graphics/Objets/GoalGate.png')
    Barre = pygame.image.load('Graphics/Objets/Barre.png')

    def __init__(self, x, y, mode): #mode Champi ou Drapeau
        self.x = x
        self.y = y
        self.mode = mode
        if self.mode == 'Champi':
            self.hitbox = [self.x, self.y, 75, 75]
        elif self.mode == 'Drapeau':
            self.hitbox = [self.x + 37, self.y + 37, 112, 37]
        self.vitesse = 9
        self.SortieBloc = False
        self.apparu = False
        self.consomme = False
        self.OnGround = True
        self.droite = True
        self.gauche = False
        self.ComptChute = 0
        self.Sur = False
        self.AuDessus = False
        self.AGauche = False
        self.ADroite = False
        self.Montant = False

    def contact(self, player):
        if self.mode == "Champi":
            if self.apparu and not self.consomme:
                if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2] and player.hitbox[1] + player.hitbox[3] >= self.hitbox[1] and player.hitbox[1] <= self.hitbox[1] + self.hitbox[3]:
                    if player.vie < 2:
                        player.vie +=1
                    self.consomme = True
                    pygame.mixer.Channel(5).set_volume(0.2)
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound/Upgrade.wav'))

        if self.mode == 'Drapeau':
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2] and player.hitbox[1] + player.hitbox[3] >= self.hitbox[1] and player.hitbox[1] <= self.hitbox[1] + self.hitbox[3] and not self.consomme:
                self.consomme = True
                player.vitesse = 0
                player.Win = True
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound/Clear_Level.mp3'))
                pygame.mixer.Channel(0).set_volume(0.3)
                   

    def spawn(self, bloc):
        if self.mode == "Champi":
            if bloc.Cogne and not self.apparu and not self.SortieBloc:
                self.SortieBloc = True
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('Sound/Appear.wav'))
                pygame.mixer.Channel(3).set_volume(0.5)
            if self.SortieBloc:
                if self.hitbox[1] + self.hitbox[3] >= bloc.hitbox[1] and self.hitbox[1] <= bloc.hitbox[1] + bloc.hitbox[3]:
                    self.y -= 3
                else:
                    self.SortieBloc = False
                    self.apparu = True

    def bouge(self):
        if self.mode == "Champi":
            if self.apparu and not self.consomme:
                self.x += self.vitesse

    def chute(self):
        if self.mode == "Champi":
            if self.apparu and not self.consomme and not self.OnGround:
                if self.ComptChute <= 0:
                    self.y +=  0.75 * (self.ComptChute ** 2)
                    if self.ComptChute > -8:
                        self.ComptChute -= 1
                        
    def interaction(self, sol):
        if self.apparu:
            if self.hitbox[0] + self.hitbox[2] > sol.hitbox[0] and self.hitbox[0] < sol.hitbox[0] + sol.hitbox[2] and sol.hitbox[1] >= self.hitbox[1] + self.hitbox[3]:
                self.AuDessus = True
            else:
                self.AuDessus = False
            if self.hitbox[1] + self.hitbox[3] > sol.hitbox[1] and self.hitbox[1] < sol.hitbox[1] + sol.hitbox[3]:
                if ((self.hitbox[0] + self.hitbox[2] + abs(self.vitesse) >= sol.hitbox[0] and self.hitbox[0] < sol.hitbox[0] + sol.hitbox[2] and self.droite) or (self.hitbox[0] - abs(self.vitesse) <= sol.hitbox[0] + sol.hitbox[2] and self.hitbox[0] + self.hitbox[2] > sol.hitbox[0] and self.gauche)):
                    self.droite, self.gauche = self.gauche, self.droite
                    self.vitesse = self.vitesse * -1
            if self.AuDessus:
                if self.hitbox[1] + self.hitbox[3] + 0.75 * (self.ComptChute ** 2) >= sol.hitbox[1]:
                    self.y = sol.hitbox[1] - 75
                    self.ComptChute = 0
                    self.OnGround = True
                    self.Sur = True
                else:
                    self.OnGround = False
            if self.y == sol.hitbox[1] - 75 and self.Sur:
                if not self.hitbox[0] + self.hitbox[2] >= sol.hitbox[0] or not self.hitbox[0] <= sol.hitbox[0] + sol.hitbox[2]:
                    self.OnGround = False
                    self.Sur = False

                    

    def dessiner(self, screen):
        if self.mode == "Champi":
            self.bouge()
            if not self.consomme:
                screen.blit(pygame.transform.scale(self.Champi, (75, 75)), (self.x - Niveau1.scroll[0], self.y))
                self.hitbox = [self.x - Niveau1.scroll[0], self.y, 75, 75]
        
        if self.mode == "Drapeau":
            self.hitbox = [self.x - Niveau1.scroll[0] + 37, self.hitbox[1], 112, 37]
            screen.blit(pygame.transform.scale(self.Drapeau, (225, 675)), (self.x - Niveau1.scroll[0], self.y))
            if not self.consomme:
                if self.hitbox[1] + self.hitbox[3] < self.y + 660 and not self.Montant:
                    self.hitbox[1] += 15
                else:
                    self.Montant = True
                if self.hitbox[1] > self.y + 60 and self.Montant:
                    self.hitbox[1] -= 15
                else:
                    self.Montant = False
                screen.blit(pygame.transform.scale(self.Barre, (112, 37)), (self.hitbox[0], self.hitbox[1]))
                



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

Niveau1 = Level1()
#Niveau1.main()

