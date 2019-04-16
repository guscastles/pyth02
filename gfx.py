import pygame
import sys
import random

pygame.init()


# info = pygame.display.Info()
# screen = pygame.display.set_mode((info.current_w - 200, info.current_h))
screen = pygame.display.set_mode((800,600))
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

screen.fill(0)

def ri(max=255):
    return random.randint(0, max)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             # and event.key == pygame.K_ESCAPE:
             pygame.quit()
             sys.exit()

    # pygame.draw.rect(
    #   screen,
    #   (ri(), ri(), ri()),
    #   (ri(640), ri(480), ri(200), ri(200)),
    #   4
    # )

    # screen.fill(0)

    mx, my = pygame.mouse.get_pos()
    # pygame.draw.rect(screen, (255,0,0), (mx, my, 20, 20), 0)

    pygame.draw.circle(
      screen,
      (ri(), ri(), ri()),
      (mx, my),
      10,
      0
    )

    pygame.display.update()

    # end of main while draw loop
