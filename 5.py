import pygame as pg
from random import randrange

pg.init()

pg.display.set_caption("Snake!")


WINDOW = 750
TILE_SIZE = 40
RANGE = (TILE_SIZE // 2 , WINDOW - TILE_SIZE // 2 , TILE_SIZE)
get_random_position =lambda: [randrange(*RANGE),randrange(*RANGE)]
snake = pg.rect.Rect([0,0,TILE_SIZE-1, TILE_SIZE-1])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time = 0
time_step = 150
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()
dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1,pg.K_RIGHT: 1}


pg.mixer.music.load('snake_music.mp3')
pg.mixer.music.play()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and dirs[pg.K_UP]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1,pg.K_RIGHT: 1}
            if event.key == pg.K_DOWN and dirs[pg.K_DOWN]:
                snake_dir = (0 , TILE_SIZE)
                dirs = {pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1,pg.K_RIGHT: 1}
            if event.key == pg.K_LEFT and dirs[pg.K_LEFT]:
                snake_dir = (-TILE_SIZE , 0)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1,pg.K_RIGHT: 0}
            if event.key == pg.K_RIGHT and dirs[pg.K_RIGHT]:
                snake_dir = (TILE_SIZE , 0)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0,pg.K_RIGHT: 1}

    screen.fill('black')
    #check borders and selfeating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center = get_random_position()
        food.center = get_random_position()
        length = 1
        snake_dir = (0,0)
        segments = [snake.copy()]
    #check food
    if snake.center == food.center:
        food.center = get_random_position()
        length +=1
    #draw food
    pg.draw.rect(screen, 'white' , food)
    #draw snake
    [pg.draw.rect(screen, 'pink' , segment)for segment in segments]
    #move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pg.display.flip()
    clock.tick(60)
     