import pygame, assets, inputcontrol, functions, globalvars, battlesystem
from pygame.locals import *

width = globalvars.width 
height = globalvars.height
objectsPerWidth = 20
pygame.init()
screen = pygame.display.set_mode((width,height+128))
turn = 0

#Idea: Have a main.py in game engine (like physics engine). make a dictionary in that. for all future games, import that as object (main()) 
#then, those future games can simply main.whiletrue.add(NAME OF FUNCTION, LAMBDA FUNCTION HERE). In main.py, this gets called while 1.
#so it's an engine for event handling and looping
   
    
def loadImage(filename):
    return pygame.image.load(filename)

font = pygame.font.SysFont("monospace", 15)
clock = pygame.time.Clock()
squareSprites = assets.classSquareSprites()
squares = []

def drawCursor(sprite):
    mx,my = pygame.mouse.get_pos()
    screen.blit(sprite,(mx,my))
    
    
#Load images
squareSprites.grass = loadImage("art\squaregrass.png")
squareSprites.unit = loadImage("art\squareunit.png")
squareSprites.unitSelected = loadImage("art\squareunitselected.png")
squareSprites.hudEndTurn = loadImage("art\hud\hudendturn.png")
squareSprites.hudEndTurnClicked = loadImage("art\hud\hudendturnclicked.png")
squareSprites.hudOpenMenu = loadImage("art\hud\hudopenmenu.png")
squareSprites.hudOpenMenuClicked = loadImage("art\hud\hudopenmenuclicked.png")
squareSprites.hudInformationPanel = loadImage("art\hud\hudinformationpanel.png")
squareSprites.hudAirforce = loadImage("art\hud\hudairforce.png")
squareSprites.hudAirforceClicked = loadImage("art\hud\hudairforceclicked.png")
squareSprites.hudFort = loadImage("art\hud\hudfort.png")
squareSprites.hudFortClicked = loadImage("art\hud\hudfortclicked.png")
squareSprites.hudUnit = loadImage("art\hud\hudunit.png")
squareSprites.hudUnitClicked = loadImage("art\hud\hudunitclicked.png")
squareSprites.cursorUnit = loadImage("art\cursors\cursorunit.png")
squareSprites.unitEnemy = loadImage("art\squareunit.png")
    
#Create GUI objects
button = []
button.append(assets.classGuiButton(880,height,squareSprites.hudEndTurn,squareSprites.hudEndTurnClicked,screen))
button.append(assets.classGuiButton(400,height,squareSprites.hudAirforce,squareSprites.hudAirforceClicked,screen))
button.append(assets.classGuiButton(400+160,height,squareSprites.hudUnit,squareSprites.hudUnitClicked,screen,"reinforcements",font))
button.append(assets.classGuiButton(400+160+160,height,squareSprites.hudFort,squareSprites.hudFortClicked,screen))
unitInformationPanel = assets.classUnitInformationPanel(0,height,screen,squareSprites.hudInformationPanel)

#Set each button to have an action
button[0].action = button[0].actionEndTurn
button[1].action = button[1].actionEndTurn    
button[2].action = button[2].actionPlaceUnit
button[3].action = button[3].actionEndTurn        
    
#Create squares
for ii in range(height/64):
    for i in range(width/64):
        squares.append(assets.classSquare(i*64,ii*64,squareSprites.grass))
        
#For testing purposes [sets a unit at position]
unit = []
unit.append(assets.classTypeUnit(0,squareSprites.unit,squareSprites.unitSelected,True))
unit.append(assets.classTypeUnit(45,squareSprites.unit,squareSprites.unitSelected,False,100))
unit.append(assets.classTypeUnit(23,squareSprites.unit,squareSprites.unitSelected,False,90))

#For testing purposes [sets enemy units at positions]
enemyUnit = []
enemyUnit.append(assets.classTypeEnemyUnit(3,squareSprites.unitEnemy))

#Create battles
battles = []
for ii in range((height/64)*(width/64)):
        battles.append(battlesystem.battle(False,ii,screen))

while 1:
    clock.tick(60)
    screen.fill((0,0,0))
    unitInformationPanel.drawSelf("", font, False)
    #Draw unit information panel
    for idx, i in enumerate(unit):
        if unit[idx].selected == True:
            unitInformationPanel.drawSelf(unit[idx], font, True)
    #Change images of squares to reflect changes of positions of units. Draw squares.
    for indx,i in enumerate(squares):
        i.type = squareSprites.grass
        for ii, iii in enumerate(unit):
            if indx == unit[ii].idx:
                if unit[ii].selected == True:
                    i.type = squareSprites.unitSelected
                    
                else: 
                    i.type = squareSprites.unit
                    screen.blit(i.type,(i.x,i.y))
        for ii, iii in enumerate(enemyUnit):
            if indx == enemyUnit[ii].idx:
                i.type = squareSprites.unitEnemy
        screen.blit(i.type,(i.x,i.y))
    #Draw gui buttons or battle GUI
    for idx,i in enumerate(button):
        button[idx].drawSelf()
    for idx,i in enumerate(battles):
        if battles[idx].selected == True:
            battles[idx].drawSelf()
    #Draw cursor
    if globalvars.placenewunit == True:
        drawCursor(squareSprites.cursorUnit)
    #Draw selected units (so they are drawn last)
    for i,ii in enumerate(unit):
        for iii, iiii in enumerate(squares):
            if unit[i].selected == True:
                if unit[i].idx == iii:
                    screen.blit(squareSprites.unitSelected,(squares[iii].x,squares[iii].y))
    pygame.display.flip()
    for event in pygame.event.get():
        #Move units
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for ii, iii in enumerate(unit):
                if globalvars.turn == 0:
                    if unit[ii].selected == True:
                        if functions.returnForUnitPosition(width,height,unit[ii].idx,objectsPerWidth) == True:
                            for inde,i in enumerate(squares):
                                for aa, bb in enumerate(enemyUnit):
                                    if functions.returnForPositionAvailable(width, height, unit[ii].idx, enemyUnit[aa].idx, objectsPerWidth):                                       
                                        i.type = squareSprites.grass
                                        unit[ii].idx = inputcontrol.getMouseOverSquare(width, height,objectsPerWidth)
                                    else: 
                                        if battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].active == False:
                                            battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].active = True
                                            battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].battleUnitPlayer.append(unit[ii])
                                        else:
                                            a = 0
                                            for o in battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].battleUnitPlayer:
                                                if unit[ii] is o:
                                                    a = 1
                                            if a == 0:
                                                battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].battleUnitPlayer.append(unit[ii])
                                                
                                        
    
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Place new units/other objects if needed
            if globalvars.placenewunit == True:
                if inputcontrol.getMouseOverObject(0, 0, width, height):
                    unit.append(assets.classTypeUnit(inputcontrol.getMouseOverSquare(width, height, objectsPerWidth),squareSprites.unit,squareSprites.unitSelected,True))
                    globalvars.placenewunit = False
            #Select units
            for ii, iii in enumerate(unit):
                unit[ii].selected = False
                if unit[ii].idx == inputcontrol.getMouseOverSquare(width, height,objectsPerWidth):
                    c = 0
                    for a,b in enumerate(unit):
                        if unit[a].selected == True:
                            c += 1
                            if c > 1:
                                break
                            else: unit[a].selected = True
                    if c == 0:
                        unit[ii].selected = True
            for a in battles:
                a.selected = False
            for ii, iii in enumerate(enemyUnit):
                if enemyUnit[ii].idx == inputcontrol.getMouseOverSquare(width, height, objectsPerWidth):
                    battles[inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)].selected = True
                    
            #Button actions
            for idx,i in enumerate(button):
                button[idx].action()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for idx,i in enumerate(button):
                button[idx].actionMouseOff()
        if event.type == QUIT:
            pygame.quit()
            
"""To do:
buttons
unit information panel (strength/health [same thing - it is based on # of units in division], name, turn developed etc)
unit information panel picture of unit
airforce panel (will have to add airforce in later)
new unit panel (and new unit system - so hq system too)
each unit can only have x number of moves per turn
place fort panel
MAYBE save/open game?
start menu, options menu
screen scaling
terrain
enemy ai (just make random for now?)
"""