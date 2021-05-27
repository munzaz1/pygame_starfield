#!/usr/bin/python3


import pygame
import random
import sys


class Star():
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.setRandomPosition()


    def setRandomPosition(self):
        self.x = random.randint(-self.width / 4, self.width / 4)
        self.y = random.randint(-self.height / 2, self.height / 2)
        self.z = random.randint(1, self.width)
        self.r = random.choice([1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7])


    def draw(self, screen):
        sx = self.maps((self.x) / self.z, 0, 1, 0, self.width)
        sy = self.maps((self.y) / self.z, 0, 1, 0, self.height)
        mr  = max(1, self.maps(self.z, 0, self.width, self.r, 0))
        #r = 10
        pygame.draw.circle(screen, (255, 255, 255), (int(sx + (self.width / 2)), int(sy + (self.height / 2))), mr)


    def maps(self, num, inMin, in_max, out_min, out_max):
        return (num - inMin) * (out_max - out_min) / (in_max - inMin) + out_min


    def update(self):
        self.z -= self.width / 200
        if (self.z < 1):
            self.setRandomPosition()


def main():
    fps = 60

    #screen = pygame.display.set_mode((1000, 600))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    width, height = pygame.display.get_surface().get_size()


    pygame.display.set_caption('Starfield')
    clock = pygame.time.Clock()

    stars = []
    for i in range(1000):
        s = Star(width, height)
        stars.append(s)


    finished = False
    while not finished:
        clock.tick(fps)

        screen.fill((0, 0, 0))
        for s in stars:
            s.update()
            s.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   finished = True

    pygame.quit()


if __name__=="__main__":
  main()
