import pygame
from Additional import Configurations
from pytmx.util_pygame import load_pygame
from View import Tile

class LayerController():

    #define as bordas da janela
    def screenBorder(layer):
        config = Configurations.Helper.getConfigs()

        border = pygame.Rect(0, 0, 1, 960 -1)
        pygame.draw.rect(layer, (255, 0, 0), border)

        border = pygame.Rect(0, 0, 960-1, 1)
        pygame.draw.rect(layer, (255, 0, 0), border)

        border = pygame.Rect(960 -1, 0, 1, 960)
        pygame.draw.rect(layer, (255, 0, 0), border)

        border = pygame.Rect(0, 960 -1, 960, 1)
        pygame.draw.rect(layer, (255, 0, 0), border)

        pygame.display.update()

    def __mapTiles(bg, group):
        for layer in bg.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x*16, y*16)
                    Tile.Tile(pos = pos, surf = surf, groups=group)

    def createBg(lv, group):
        if lv == 1:
            bg = pygame.image.load('./assets/maps/lv1/screen1.png')
            #LayerController.__mapTiles(bg, group)


    def create_layers(layers):
        mother = {}
        helper = Configurations.Helper.getConfigs()

        for layer in layers:
            mother[layer] = pygame.Surface((helper['width'], helper['heigth']))
        
        return mother
    
    def addElementsToLayer(layer, color, screen='1'):
        
        LayerController.__screenBorder(layer)
        
        if screen == 1:
            #                  (positionX, positionY, sizeX, sizeY)
            rect = pygame.Rect(20, 600 - 100, 100, 100)
            pygame.draw.rect(layer, color, rect)


    def showLayers(layers, window):
        for layer in layers:
            window.blit(layers[layer], (0, 0))
        pygame.display.update()
