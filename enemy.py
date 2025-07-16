import random
import pygame as pg
# Enemy class 
class Enemy(pg.sprite.Sprite):
    def __init__(self,enemyImages,xpos,ypos):
        super().__init__()
        #defining properties
        index=random.randint(0,7)
        self.image=enemyImages[index]
        self.rect=self.image.get_rect()
        self.rect.y=ypos
        self.rect.x=xpos
        self.speed=25
    
    # moving the enemies
    def update(self,dt):
        self.rect.y+=self.speed*dt*60



