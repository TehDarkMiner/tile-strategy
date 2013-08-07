import pygame, assets, globalvars

width = globalvars.width
height = globalvars.height

class battle:
    def __init__(self,active,square,screen):
        self.battleUnitPlayer = [] #Units fighting for player
        self.battleUnitEnemy = [] #Units fighting for enemy
        self.square = square
        self.active = active
        self.selected = False
        self.screen = screen
        self.active = False
        
    def drawSelf(self):
        if self.selected == True:
            pygame.draw.rect(self.screen,assets.colours.lgreen,pygame.Rect(0,height,width,height-128))