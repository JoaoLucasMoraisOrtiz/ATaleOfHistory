import pygame

class Camera(pygame.sprite.Group):

    def __init__(self, window):
        super().__init__()
        self.display_surface = window
        self.ground_surf = pygame.image.load('./assets/maps/lv1/screen1.png').convert()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))

        #zoom
        self.zoom_scale = 2
        self.internal_surf_size = (600, 600)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        
        #camera offset
        self.offset = pygame.math.Vector2()


        #camera box
        self.camera_borders = {'left': 592, 'right': 0, 'top': 352, 'bottom': 0}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)
    
    def box_target_camera(self, target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left

        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top

        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def custom_draw(self, player):

        self.box_target_camera(player)

        self.internal_surf.fill((0,0,0))

        #desenha o bg
        ground_offset = self.ground_rect.topleft - self.offset

        self.internal_surf.blit(self.ground_surf, ground_offset // 2)

        #desenha os elementos 
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            
            offset_pos = sprite.rect.topleft - self.offset

            self.internal_surf.blit(sprite.image, offset_pos//2)

        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2))

        self.display_surface.blit(scaled_surf, scaled_rect)