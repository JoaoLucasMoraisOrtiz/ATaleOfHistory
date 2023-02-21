from Controller import objectsController, playerController
from Model import saveMethods
def createLevel(lv, group):
    lv = saveMethods.getLevel(lv)
    for item in lv['elements']:
        
        objectsController.drawObjects.drawObjects(item, group, lv['elemPos'][item])

def createPlayer(lv, group):

    lv = saveMethods.getLevel(lv)
    return playerController.Player(eval(lv['playerPos']), group)

def getSaveLevel():
    lv = saveMethods.load_game()
    return lv
