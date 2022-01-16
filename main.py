import pygame
from stars.star import Star

FPS = 60
WIN_WIDTH = 2000
WIN_HEIGHT = 500
BLACK = (0, 0, 0)
star = Star(x=231, y=231, brightness=0, period=100, side=200)

pygame.init()  ##################
clock = pygame.time.Clock()  ##################
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  ##################


while 1:
    sc.fill(BLACK)
    for i in pygame.event.get():  ##################
        if i.type == pygame.QUIT: exit()  ##################
    star.check_brightness()
    pygame.draw.rect(sc, [star.brightness, star.brightness, star.brightness], (star.x, star.y, star.side, star.side))
    pygame.draw.rect(sc, [255, 255, 255], (0, 0, 200, 200))

    pygame.display.update()  ##################
    clock.tick(FPS)  ##################