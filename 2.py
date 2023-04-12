import pygame
pygame.init()

screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption("Arctic monkeys")

clock = pygame.time.Clock()

m1 = "mus1.mp3"
m2 = "mus2.mp3"
m3 = "mus3.mp3"

pygame.mixer.music.load("mus1.mp3")
myList = [m1 ,m2,m3]
pygame.mixer.music.play(-1)

flPause = False
index = 0
run = True

while run:
    screen.fill('Pink')
    player = pygame.image.load('icon.png')
    screen.blit(player, (75, 75))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(myList):
                    index = 0
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(myList)-1
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()

    clock.tick(20)