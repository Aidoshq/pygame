import pygame as pg
import sys
from pygame.locals import *
import random, time

pg.init()

#Setting up FPS 
FPS = 60
FramePerSec = pg.time.Clock()

#colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Variables for program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 10
SCORE = 0

#Setting up Fonts
font = pg.font.SysFont("Verdana", 40)
font_small = pg.font.SysFont("Verdana", 10)
game_over = font.render("ОЙЫН БІТТІ!", True, BLACK)

bg = pg.image.load("background.png")

#screen 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Race game for students")

#music for atmosphere
pg.mixer.music.load('road.music.mp3')
pg.mixer.music.play()

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.transform.scale(pg.image.load("player.png"), (100,110))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
       
    def move(self):
        klav = pg.key.get_pressed()
        if klav[K_UP]:
            self.rect.move_ip(0, -9)
        if klav[K_DOWN]:
            self.rect.move_ip(0,9)
        if klav[K_LEFT]:
            self.rect.move_ip(-9,0)
        if klav[K_RIGHT]:
            self.rect.move_ip(9,0)   
class Coins (pg.sprite.Sprite):
     def __init__ (self):
        super().__init__()
        self.image = pg.image.load("moneta.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20,SCREEN_WIDTH-20),random.randint(20,SCREEN_HEIGHT-20))   

     def move (self):
        x = random.randint(20,SCREEN_WIDTH-20)
        y = random.randint(20,SCREEN_HEIGHT-20)
        self.rect.center = (x,y)

#Setting up Sprites        
P = Player()
E = Enemy()
C = Coins()

#Creating Sprites Groups
coins = pg.sprite.Group()
coins.add(C)
enemies = pg.sprite.Group()
enemies.add(E)
all_sprites = pg.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)

#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 2000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pg.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    for entity in coins: 
        screen.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P, enemies):
          pg.mixer.music.stop()
          pg.mixer.music.load('craash.wav')
          pg.mixer.music.play()
          time.sleep(1.5)           
          screen.fill('Pink')
          screen.blit(game_over, (30,250))
          res_scores = font.render("Score: "+str(SCORE), True, BLACK)
          screen.blit(res_scores,(20,200))
          pg.display.update()


          for entity in all_sprites:
                entity.kill() 
          time.sleep(3)
          
          pg.quit()
          sys.exit()  
        

    if pg.sprite.spritecollideany(P, coins):
            pg.mixer.Sound('coins.wav').play()
            SCORE += 1
            C.move()
                      
    pg.display.update()
    FramePerSec.tick(FPS)