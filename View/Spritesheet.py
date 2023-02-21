import pygame

class Spritesheet():
    def __init__(self, image):
        self.sheet = image
        self.animation_colldown = 100
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
    
    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
    
    def update_frame(self):
        if pygame.time.get_ticks() - self.last_update >= self.animation_colldown:
            
            self.frame += 1
            
            self.last_update = pygame.time.get_ticks()
            
            if self.frame == 5:
                self.frame = 0
            
            return Spritesheet.get_image(self, self.frame, 18, 32, 0.8, (0, 0, 0))
        else:
            f = self.frame
            return Spritesheet.get_image(self, self.frame, 18, 32, 0.8, (0,0,0))

""" pygame.init()
screen = pygame.display.set_mode((800, 600))
last_update = pygame.time.get_ticks()
animation_colldown = 100
frame = 0

spritesheet = Spritesheet(pygame.image.load('../assets/player/boy/walkBack.png'))
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_colldown:
        frame += 1
        last_update = current_time
        screen.blit(spritesheet.get_image(frame, 18, 32, 3, (0, 0, 0)), (0,0))
        if frame == 5:
            frame = 0
    #screen.blit(spritesheet.get_image(0, 18, 32, 3, (255, 255, 255)), (0,0))
    #screen.blit(spritesheet.get_image(1, 18, 32, 3, (0, 0, 0)), (64,0))
    #screen.blit(spritesheet.get_image(2, 18, 32, 3, (0, 0, 0)), (64*2,0))
    #screen.blit(spritesheet.get_image(3, 18, 32, 3, (0, 0, 0)), (64*3,0))
    #screen.blit(spritesheet.get_image(4, 18, 32, 3, (0, 0, 0)), (64*4,0))
    #screen.blit(spritesheet.get_image(5, 18, 32, 3, (0, 0, 0)), (64*5,0))
    pygame.display.update() """