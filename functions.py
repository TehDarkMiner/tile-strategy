import pygame, inputcontrol

def returnForUnitPosition(width,height,unitposition,objectsPerWidth):
    if inputcontrol.getMouseOverSquare(width, height, objectsPerWidth) == unitposition+1:
        if (unitposition+1) % objectsPerWidth != 0:
            return True
    elif inputcontrol.getMouseOverSquare(width, height,objectsPerWidth) == unitposition-1:

        if (unitposition) % objectsPerWidth != 0:
            return True
    elif inputcontrol.getMouseOverSquare(width, height,objectsPerWidth) == unitposition+objectsPerWidth:
        return True
    elif inputcontrol.getMouseOverSquare(width, height,objectsPerWidth) == unitposition-objectsPerWidth:
        return True
    else: return False
    
def returnForPositionAvailable(width,height,unitposition,otherposition,objectsPerWidth):
    a = 0
    b = inputcontrol.getMouseOverSquare(width, height, objectsPerWidth)
    if b == unitposition+1:
        if b == otherposition:
            a = 1
    if b == unitposition-1:
        if b == otherposition:
            a = 1
    if b == unitposition+objectsPerWidth:
        if b == otherposition:
            a = 1
    if b == unitposition-objectsPerWidth:
        if b == otherposition:
            a = 1
    if a == 0:
        return True
    elif a == 1:
        return False