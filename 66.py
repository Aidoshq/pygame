import pygame, math
#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
clock = pygame.time.Clock()

#Creating colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

#Create a white screen 
W, H = 400, 600
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.set_caption("PAINT")

#Color, mode, width of shape
color = BLACK
shape = 'line'
width = 10
#Start and end points
startPos, endPos = 0, 0
run = True

while run:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL] # ctrl is pressed
    
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            #change width of shape
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            #change color of shape
            if pressed[pygame.K_b]:
                color = BLUE
            if pressed[pygame.K_r]:
                color = RED
            if pressed[pygame.K_g]:
                color = GREEN
            #change shape 
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_s]:
                shape = 'square'
            if ctrl_pressed and pressed[pygame.K_t]:
                shape = 'equilateral_triangle'
            if ctrl_pressed and pressed[pygame.K_m]:
                shape = 'right_triangle'
            if ctrl_pressed and pressed[pygame.K_h]:
                shape = 'rhombus'
        
        # line and eraser are similar in use
        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                startPos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                endPos = pygame.mouse.get_pos()
                if startPos:
                    if shape == 'line':
                        pygame.draw.line(sc, color, startPos, endPos, width)
                    if shape == 'eraser':
                        pygame.draw.line(sc, WHITE, startPos, endPos, width) #just repaints white
                    startPos = endPos
            if event.type == pygame.MOUSEBUTTONUP:
                startPos = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                startPos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                endPos = pygame.mouse.get_pos()
                if shape == 'square' or shape == 'rectangle' :
                    x = min(startPos[0], endPos[0]) #min cordinates
                    y = min(startPos[1], endPos[1])
                    lx = abs(startPos[0]-endPos[0]) #lenght
                    ly = abs(startPos[1]-endPos[1])
                    if shape == 'square':
                        lx = (lx+ly)/2  # length and width are same for square
                        ly = lx
                    pygame.draw.rect(sc, color, (x, y, lx, ly), width)
                elif shape == 'circle':
                    x = (startPos[0]+endPos[0])/2 #cordinates of center
                    y = (startPos[1]+endPos[1])/2
                    rx = abs(startPos[0]-endPos[0])/2
                    ry = abs(startPos[1]-endPos[1])/2 #radius
                    r = (rx + ry)/2
                    pygame.draw.circle(sc, color, (x, y), r, width)

                elif shape == 'right_triangle' or shape == 'equilateral_triangle':
                    x = min(startPos[0], endPos[0])  #minimal coordinate
                    y = min(startPos[1], endPos[1])
                    lx = abs(startPos[0]-endPos[0])  # length of pseudo rectangle
                    ly = abs(startPos[1]-endPos[1])
                    if shape == 'right_triangle':
                        ly = math.sqrt(lx**2 - (lx/2)**2)  # all sides are equal
                    points = (x, y+ly), (x+lx/2, y), (x+lx, y+ly)  # draw by three points
                    pygame.draw.polygon(sc, color, points, width)
                elif shape == 'rhombus':               
                    x = min(startPos[0], endPos[0])  #min coordinate
                    y = min(startPos[1], endPos[1])
                    lx = abs(startPos[0]-endPos[0])  
                    ly = abs(startPos[1]-endPos[1])
                    points = (x+lx/2, y), (x+lx, y+ly/2), (x+lx/2, y+ly), (x, y+ly/2)
                    pygame.draw.polygon(sc, color, points, width)  # draw by points
                
    pygame.display.update() #updates the window
    clock.tick(FPS) #60 frames per second

pygame.quit()