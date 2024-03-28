import datetime 
import os
import pygame


pygame.init()
mclock = pygame.image.load(r"lab7\mainclock.png")
second = pygame.image.load(r'lab7\leftarm.png')
minute = pygame.image.load(r"lab7\rightarm.png")

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

screen = pygame.display.set_mode((800, 850))
pygame.display.set_caption('miclock')
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        x = datetime.datetime.now()
        ang_sec = 360 - int(x.strftime("%S"))*6 
        ang_min = 311 - int(x.strftime("%M"))*6 + int(x.strftime("%S"))/60
        screen.blit(mclock, (-300,-100))
        blitRotateCenter(screen, second, (380, -100), ang_sec) 
        blitRotateCenter(screen, minute, (-300, -100), ang_min)
        pygame.display.flip()
        



