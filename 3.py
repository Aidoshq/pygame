import pygame as pg
pg.init()

w = 400
h = 600

screen = pg.display.set_mode((w , h))
pg.display.set_caption("Balll")
r = True

clock = pg.time.Clock()

x = 0
y = 0
v = 20

while r:
    screen.fill('White')
    circle = pg.draw.circle(screen, 'Black' , (x , y) , 25)
    x = max(50 , min(x , w -50))

    y = max(50, min(y , h -50))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = 0
            pg.quit()
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x -= v
            if event.key == pg.K_RIGHT:
                x += v
            if event.key == pg.K_UP:
                y -= v
            if event.key == pg.K_DOWN:
                y += v

    clock.tick(60)



