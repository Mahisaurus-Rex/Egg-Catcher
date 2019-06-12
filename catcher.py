import pygame
import time
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280,720))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    

    screen.fill((0,0,0))
    screen.blit(score, ((screen.get_width()/2)-20,0))

    pygame.display.flip()