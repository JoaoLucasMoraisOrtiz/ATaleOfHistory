from View import cameraController
import pygame
from Controller import mainController, layersController, playerController, objectsController
running = True
pygame.init()
clock = pygame.time.Clock()

#cria a janela principal
window = mainController.mainController.start()
pygame.display.update()

#cria a camera e o player
camera = cameraController.Camera(window)

#layersController.LayerController.createBg(1, camera)
objectsController.drawObjects.drawObjects('tree', camera)
objectsController.drawObjects.drawObjects('oldTree', camera)
objectsController.drawObjects.drawObjects('groundColision', camera)
player = playerController.Player((600,360), camera)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = mainController.mainController.stop()

    # atualiza a camera e movimentação do player
    camera.update()
    camera.custom_draw(player)
    colision = False
    for sprite in sorted(camera.sprites(), key=lambda sprite: sprite.rect.centery):
        if sprite.type == 'block':
            colision = player.colision(sprite)
    

    # atualiza o display
    pygame.display.update()
    clock.tick(60)
