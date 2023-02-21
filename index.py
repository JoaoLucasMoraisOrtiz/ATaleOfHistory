import pygame
from View import cameraController
from Controller import mainController
import app


running = True
pygame.init()
clock = pygame.time.Clock()

#cria a janela principal
window = mainController.mainController.start()
pygame.display.update()

#pega o nível
lv = app.getSaveLevel()

#cria a camera e o player
camera = cameraController.Camera(window, lv['lv'])

app.createLevel(lv['lv'], camera)
player = app.createPlayer(lv['lv'], camera)


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