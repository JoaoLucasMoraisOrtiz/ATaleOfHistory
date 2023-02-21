import pygame

class Tree(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        self.type = 'image'
        self.image = pygame.image.load('./assets/maps/lv1/objects/bigTree.png')
        self.rect = self.image.get_rect(topleft = pos)

class OldTree(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        self.type = 'image'
        self.image = pygame.image.load('./assets/maps/lv1/objects/bigOldTree.png')
        self.rect = self.image.get_rect(topleft = pos)

class Wall(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        self.type = 'block'
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        #self.image = pygame.Surface((16, 16))
        self.image.fill((255, 255, 0, 1))
        #self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class drawObjects():
    def drawObjects(ob, group):
        match ob:
            case 'tree':
                #isto virá do banco de dados
                pos = [(20, 15), (12, 18), (100, 34), (9, 200), (960, 960)]
                for position in pos:
                    
                    #create the colision points
                    for count in range(1, 4):

                        for l in range(1, 3):
                            
                            if l == 1:
                                wposX =  position[0] + count*(16)
                                wposY = position[1] + (16*4)
                            else:
                                wposX =  position[0] + count*(16)
                                wposY = position[1] + (16*2)
                            Wall((wposX, wposY), group)
                    
                    Tree(position, group)
                    
            case 'oldTree':
                #isto virá do banco de dados
                pos = [(100, 15), (45, 65), (542, 97), (254, 39)]
                for position in pos:
                    #create the colision points
                    for count in range(1, 4):
                        for l in range(1, 3):
                            
                            if l == 1:
                                wposX =  position[0] + count*(16)
                                wposY = position[1] + (16*4)
                            else:
                                wposX =  position[0] + count*(16)
                                wposY = position[1] + (16*2)
                            Wall((wposX, wposY), group)
                             
                    OldTree(position, group)

            case 'groundColision':

                #a tupla é no modelo x, y, n onde x é a posição em x, y a posição em y,
                # e n p número de blocos 16x16 que serão colocados, crescendo em x
                pos = [(16, 304, 22), (500, 308, 7), (790, 400, 40), (84, 940, 18), (500, 940, 7), (920, 976, 16), (16, 1132, 8), (372, 1132, 14), (1298, 1164, 17), (10, 1332, 1), (146, 1324, 14), (492, 1324, 17), (918, 1356, 14),(16, 1584, 27)]
                for item in pos:
                    for count in range(1, item[2]+1):
                        Wall((item[0]+(16*count), item[1]), group)
                        Wall((item[0]+(16*count), item[1]-16), group)
            
