import pygame

pygame.init()
pygame.mixer.music.load("lab7\Aeroplane.mp3")

done = False
screen = pygame.display.set_mode((1280, 720))
    
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and playing == False:
                pygame.mixer.music.play(0)
                playing = True
            if event.key == pygame.K_SPACE and playing == True:
                pygame.mixer.music.stop()
                playing = False
        pygame.display.flip()