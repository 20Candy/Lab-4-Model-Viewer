import pygame
from pygame.locals import *
from gl import Renderer
import shader1
import shader2
import shader3

deltaTime = 0.0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)


renderer = Renderer(screen)
renderer.setShaders(shader1.vertex_shader, shader1.fragment_shader)
renderer.createObjects()

cubeX = 0
cubeZ = 0

isPlaying = True
while isPlaying:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cubeX -= 2 * deltaTime
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cubeX += 2 * deltaTime
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cubeZ -= 2 * deltaTime
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cubeZ += 2 * deltaTime

    if keys[pygame.K_c]:
        renderer.rotaY()
    if keys[pygame.K_x]:
        renderer.rotaX()
    if keys[pygame.K_z]:
        renderer.rotaZ()

    if keys[pygame.K_1]:
        renderer.setShaders(shader1.vertex_shader, shader1.fragment_shader)
    if keys[pygame.K_2]:
        renderer.setShaders(shader2.vertex_shader, shader2.fragment_shader)
    if keys[pygame.K_3]:
        renderer.setShaders(shader3.vertex_shader, shader3.fragment_shader)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isPlaying = False
    renderer.translateCube(cubeX, 0, cubeZ)

    renderer.render()


    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time()/1000

pygame.quit()
