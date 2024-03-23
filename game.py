import pygame, random, time
import gameClass


def background_1(WIDTH, HEIGHT):
    image = pygame.image.load("bg-menue.jpg")
    return pygame.transform.scale(image, (WIDTH, HEIGHT))





def main(screen, refresh, WIDTH, HEIGHT, event, mousex, mousey):
    iMode = 1
    #Logic
    #if event:


    #Graphic
    if refresh:
        background_1(screen, WIDTH, HEIGHT)
    
    return screen, refresh, event, iMode