import pygame as pg
pg.init()

clock = pg.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

W = 400
H = 600
sc = pg.display.set_mode((W, H))
sc.fill(WHITE)
pg.display.set_caption("Paint")

color = BLACK
shape = 'line'
width = 5
startPos, endPos = 0, 0

run = True
while run:
    for event in pg.event.get():

        pressed = pg.key.get_pressed()
        ctrl_pressed = pressed[pg.K_RCTRL] or pressed[pg.K_LCTRL]
    
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            if pressed[pg.K_DOWN] and width > 1:
                width -= 1
            if pressed[pg.K_UP]:
                width += 1
            if pressed[pg.K_b]:
                color = BLUE
            if pressed[pg.K_r]:
                color = RED
            if pressed[pg.K_g]:
                color = GREEN
            if ctrl_pressed and pressed[pg.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pg.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pg.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pg.K_r]:
                shape = 'rectangle'
            

        if shape == 'line' or shape == 'eraser':
            if event.type == pg.MOUSEBUTTONDOWN:
                startPos = pg.mouse.get_pos()
            if event.type == pg.MOUSEMOTION:
                endPos = pg.mouse.get_pos()
                if startPos:
                    if shape == 'line':
                        pg.draw.line(sc, color, startPos, endPos, width)
                    if shape == 'eraser':
                        pg.draw.line(sc, WHITE, startPos, endPos, width)
                    startPos = endPos
            if event.type == pg.MOUSEBUTTONUP:
                startPos = None
        else:
            if event.type == pg.MOUSEBUTTONDOWN:
                startPos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONUP:
                endPos = pg.mouse.get_pos()
                if shape == 'rectangle':
                    x = min(startPos[0], endPos[0])
                    y = min(startPos[1], endPos[1])
                    lx = abs(startPos[0]-endPos[0])
                    ly = abs(startPos[1]-endPos[1])
                    pg.draw.rect(sc, color, (x, y, lx, ly), width)
                if shape == 'circle':
                    x = (startPos[0]+endPos[0])/2
                    y = (startPos[1]+endPos[1])/2
                    rx = abs(startPos[0]-endPos[0])/2
                    ry = abs(startPos[1]-endPos[1])/2
                    r = (rx + ry)/2
                    pg.draw.circle(sc, color, (x, y), r, width)
                
    pg.display.update()
    clock.tick(60)

pg.quit()