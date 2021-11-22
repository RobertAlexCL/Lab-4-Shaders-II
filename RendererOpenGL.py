import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader_toon, shaders.fragment_shader_toon)

face = Model('model.obj', 'model.bmp')
face.position.z = -5

rend.scene.append( face )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camAngle -= 20 * deltaTime
    if keys[K_a]:
        rend.camAngle += 20 * deltaTime
    if keys[K_w]:
        rend.camRadius = rend.camRadius + 1 * deltaTime if rend.camRadius < 3 else 3
    if keys[K_s]:
        rend.camRadius = rend.camRadius - 1 * deltaTime if rend.camRadius > 30 else 30

    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime




    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()
            if ev.key == K_3:
                rend.setShaders(shaders.vertex_shader_toon, shaders.fragment_shader_toon)
            if ev.key == K_4:
                rend.setShaders(shaders.vertex_shader_color, shaders.fragment_shader_color)

            if ev.key == K_5:
                rend.setShaders(shaders.vertex_shader_inflado, shaders.fragment_shader_inflado)
            if ev.key == K_6:
                rend.setShaders(shaders.vertex_shader_tiempo, shaders.fragment_shader_tiempo)

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()