import pygame
from View import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.type = 'player'
        
        #instancia a classe dos sprites
        self.spritesheet = Spritesheet.Spritesheet(pygame.image.load('./assets/player/boy/walkBack.png'))
        #seta a imagem do primeiro sprite
        self.image = self.spritesheet.get_image(0, 18, 32, 1, (0, 0, 0))

        #colocamos ela em alguma posição
        self.rect = self.image.get_rect(center=pos)

        #pega as vetorizações para movimento do pygame
        self.direction = pygame.math.Vector2()

        self.newPosition = 0
        self.oldPosition = 0

        #seta a velocidade
        self.speed = 2
    
    #metodo responsável por verificar qual tecla esta sendo precionada no teclado
    def input(self):

        #pega a tecla precionada
        keys = pygame.key.get_pressed()

        #dependendo da tecla, a direção recebe um valor para y
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        #dependendo da tecla, a direção recebe um valor para x
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    #move o player efetivamente
    def update(self):

        #controla a animação
        if self.direction.x or self.direction.y != 0:
            self.image = self.spritesheet.update_frame()
        else:
            self.image = self.spritesheet.get_image(0, 18, 32, 1, (0, 0, 0))

        #chama a posição
        self.input()

        self.oldPosition = self.rect.center

        """ #as condições abaixo certificam que o player não ultrapassará o layout
        self.newPosition = self.rect.center + self.direction * self.speed
        if(self.newPosition[0] > 1888):
            self.newPosition[0] = 1888
        elif(self.newPosition[0] < 24):
            self.newPosition[0] = 24
        
        if(self.newPosition[1] > 1872):
                self.newPosition[1] = 1872
        elif(self.newPosition[1] < 8):
            self.newPosition[1] = 8 """

        #atualiza a posição do player
        self.rect.center = self.rect.center + self.direction * self.speed
    
    def colision(self, ob):
        hit = self.rect.colliderect(ob)
        #pos = (self.rect.center[0] - 16, self.rect.center[1])
        if hit:
            if self.direction.y < 0:
                self.direction.y = 0
                self.direction.x = 0
                self.rect.center = self.oldPosition
                #self.rect.center = pos
                #self.rect.center = (self.rect.center[0], ob.rect.center[1] + 25)

            if self.direction.y > 0:
                self.direction.y = 0
                self.direction.x = 0
                self.rect.center = self.oldPosition
                #self.rect.center = (self.rect.center[0], ob.rect.center[1]- ob.__sizeof__()*2)
            
            if self.direction.x > 0:
                self.direction.y = 0
                self.direction.x = 0
                self.rect.center = self.oldPosition
                #self.rect.center = (ob.rect.center[0]- ob.__sizeof__(), self.rect.center[1])

            if self.direction.x < 0:
                self.direction.y = 0
                self.direction.x = 0
                self.rect.center = self.oldPosition
                #self.rect.center = (ob.rect.center[0] + 25, self.rect.center[1])