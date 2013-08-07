import pygame, inputcontrol, globalvars

class colours:
    lblue = (51,255,255)
    blue = (0,0,255)
    dblue = (0,0,102)
    red = (255,0,0)
    pink = (255,51,153)
    purple = (153,51,255)
    lgreen = (204,255,0)
    green = (51,255,0)
    dgreen = (0,102,0)
    yellow = (255,255,255)
    orange = (153,255,51)
    brown = (152,102,51)
    dbrown = (102,51,0)
    white = (255,255,255)
    black = (0,0,0)
    grey = (204,204,204)
    dgrey = (50,50,50)

class classSquareSprites:
    """Every art asset placed here"""
    def __init__(self):
        self.grass = None
        self.unit = None
        self.unitSelected = None
        self.hudEndTurn = None
        self.hudEndTurnClicked = None
        self.hudOpenMenu = None
        self.hudOpenMenuClicked = None
        self.hudInformationPanel = None
        self.hudAirforce = None
        self.hudAirforceClicked = None
        self.hudFort = None
        self.hudFortClicked = None
        self.hudUnit = None
        self.hudUnitClicked = None
        self.cursorUnit = None
        self.unitEnemy = None
        
class classSquare:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        
class classTypeUnit:
    def __init__(self,idx,sprite,spriteSelected,selected,maxStrength=1000):
        self.idx = idx
        self.sprite = sprite
        self.spriteUnselected = sprite
        self.spriteSelected = spriteSelected
        self.selected = selected
        self.strength = maxStrength
        self.maxStrength = maxStrength
        self.name = "Unit"
        
class classTypeEnemyUnit:
    def __init__(self,idx,sprite,maxStrength=1000):
        self.idx = idx
        self.sprite = sprite
        self.maxstrength = maxStrength


class classGuiButton:
    def __init__(self,x,y,sprite,spriteClicked,screen,var="",font=""):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.spriteUnclicked = sprite
        self.spriteClicked = spriteClicked
        self.action = None
        self.screen = screen
        self.var = var
        self.font = font
        
    def drawSelf(self):
        self.screen.blit(self.sprite,(self.x,self.y))
        if self.var != "":
            if self.var == "reinforcements":
                label = self.font.render(str(globalvars.reinforcements), 1, (255,255,0))
                self.screen.blit(label,(self.x+32,self.y+48))
            
#Actions (for buttons and other inputs)
    def actionEndTurn(self):
        ix,iy = self.sprite.get_size()
        if(inputcontrol.getMouseOverObject(self.x, self.y, ix, iy) == True):
            self.sprite = self.spriteClicked
            if(globalvars.turn == 0):
                globalvars.turn = 1
                globalvars.currentTurn += 1
    
    def actionAirforce(self):
        ix,iy = self.sprite.get_size()
        if(inputcontrol.getMouseOverObject(self.x, self.y, ix, iy) == True):
            self.sprite = self.spriteClicked
    
    def actionPlaceUnit(self):
        ix,iy = self.sprite.get_size()
        if(inputcontrol.getMouseOverObject(self.x, self.y, ix, iy) == True):
            self.sprite = self.spriteClicked
            if(globalvars.reinforcements > 0):
                globalvars.placenewunit = True
                globalvars.reinforcements -= 1
            
        
    def actionMouseOff(self):
        self.sprite = self.spriteUnclicked
        
class classUnitInformationPanel:
    def __init__(self,x,y,screen,sprite):
        self.x = x
        self.y = y
        self.screen = screen
        self.sprite = sprite
    
    def drawSelf(self,selectedUnit,font,do):
        self.screen.blit(self.sprite,(self.x,self.y))
        if do == True:
            labelName = font.render(str(selectedUnit.name), 1, (255,255,0))
            labelStrength = font.render(str(selectedUnit.strength)+"/"+str(selectedUnit.maxStrength),1,(255,255,0))
            self.screen.blit(labelName,(self.x+64,self.y+64+16))
            self.screen.blit(labelStrength,(self.x+64,self.y+64+32))
        
        