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
class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def moveLeft(self):
        if self.x>0:
            self.x-=2
    def moveRight(self):
        if self.x<screen.get_width()-60: 
            self.x+=2
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,60,60))

class Egg:
    def spawn(self):
        self.x=random.randint(0,screen.get_width()-30)
        #self.y
p1 = Player(p1_x,p1_y)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    #movement
    if pressed[pygame.K_a] : p1.moveLeft()
    if pressed[pygame.K_d] : p1.moveRight()

    screen.fill((0,0,0))
    #screen.blit(score, ((screen.get_width()/2)-20,0))
    p1.draw()
    pygame.display.flip()