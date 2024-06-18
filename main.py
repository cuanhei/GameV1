from os import scandir
import pygame
from pygame.constants import SCALED
pygame.init()
SCREEN = pygame.display.set_mode((800,600))

TITTLE = "Shadow"
start1 = 1
start2 = 1

clock = pygame.time.Clock()
pygame.display.set_caption(TITTLE)
icon = pygame.image.load("img/icon.png").convert()
pygame.display.set_icon(icon)



isJumping = False
turn = False
gravity = 0
playery = 50

playerx = 50
playerx2 = 0
run = True
stand2 = False

stand = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerx2 += 10
                stand2 = False
            
            if event.key == pygame.K_a:
                playerx2 -= 10
                turn = True
                stand2 = True


            if event.key == pygame.K_w and isJumping == False:
                gravity -=10
                isJumping = True 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                playerx2 = 0
            
            if event.key == pygame.K_a:
                playerx2 = 0
                turn = False
            if event.key == pygame.K_w:
                gravity =0
              
    if playerx2 >=1 :
        stand = False
    else :
        stand = True
    SCREEN.fill((255,255,255))
  
    png1 = pygame.image.load("img/player/run/"+ str(start1) +".png").convert_alpha()#run
    png2 = pygame.transform.flip(png1,True,False)
    png3 = pygame.image.load("img/player/idle/0.png").convert_alpha()#stand
    png4 = pygame.image.load("img/player/jump/"+ str(start2)+".png").convert_alpha()#jump
    png5 = pygame.transform.flip(png3,True,False)
    png6 = pygame.transform.flip(png4,True,False)
    
    
    class player ():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            if turn ==True:
                SCREEN.blit(png2,(x,y))
            elif turn == False and stand == False:
                SCREEN.blit(png1,(x,y))
            elif turn == False and stand == False and stand2 == True and isJumping == True:
                SCREEN.blit(png6,(x,y))
            elif stand2:
                SCREEN.blit(png5,(x,y))
            elif isJumping :
                SCREEN.blit(png4,(x,y))
           
            else:
                SCREEN.blit(png3,(x,y))
           
            
        def draw(self):

            SCREEN.blit(pygame.transform.flip(self,self.flip,False))
    
    
    if playery <= 515:
        playery += gravity
    if playery > 515:
        playery = 515
    playerx += playerx2
    if isJumping:
        if start2 <= 19:
            start2 += 1
        if start2 >= 19:
            start2 = 19
    if isJumping == False :
        start2 = 1
    if playery >= 515:
        gravity = 0
        isJumping = False
    else :
       gravity += 1   


    if playerx >= 754:
        playerx = 754
    if playerx <= -22:
        playerx = -22
    if playerx2 != 0 :
        if start1 >= 6:
                    start1 = 1
        else :
            start1 += 1    
    player(playerx,playery)
    pygame.display.update()
    #print(playery)
    clock.tick(30)