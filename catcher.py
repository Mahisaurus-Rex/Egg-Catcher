import pygame
import time
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1080,720))
done = False
p1_x=30
p1_y= screen.get_height()-60
#make player
p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,60,60))
class Egg:
    def spawn(self):
        self.x=random.randint(0,screen.get_width()-30)
        self.y

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    #movement
    if pressed[pygame.K_a] and p1_x>0: p1_x-=2
    if pressed[pygame.K_d] and p1_x<screen.get_width()-60: p1_x+=2

    screen.fill((0,0,0))
    #screen.blit(score, ((screen.get_width()/2)-20,0))
    p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,60,60))
    pygame.display.flip()