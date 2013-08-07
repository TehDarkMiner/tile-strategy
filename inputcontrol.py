import pygame

def getMouseOverSquare(width,height,objectsPerWidth):
    mx,my = pygame.mouse.get_pos()
    if(mx < width and my < height):
        return (mx/64*width/64)/objectsPerWidth+((my/64)*width/64)

def getMouseOverObject(x,y,width,height):
    mx,my = pygame.mouse.get_pos()
    if(mx >= x and mx <= width+x):
        if my >= y and my <= height+y:
            return True
    else: return False