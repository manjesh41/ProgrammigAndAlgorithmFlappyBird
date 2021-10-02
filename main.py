import pygame, sys
def MakeFloor():
    screen.blit(FloorSurface, (FloorXPosition, 412))
    screen.blit(FloorSurface, (FloorXPosition + 288, 412))


pygame.init()
screen= pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

BgSurface=pygame.image.load('C:/Users/ACER/Downloads/background-day.png').convert()

FloorSurface = pygame.image.load('C:/Users/ACER/Downloads/base.png').convert()
FloorXPosition=0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
    screen.blit(BgSurface,(0,0))
    FloorXPosition -=1
    MakeFloor()
    if FloorXPosition <=-288:
        FloorXPosition=0


    pygame.display.update()
    clock.tick(90)