import pygame
import numpy as np
import gameFunctions

DARK_GREY = (64,64,64)
LIGHT_GREY = (224,224,224)

def background(WIDTH, HEIGHT):
    image = pygame.image.load("bg-menue.jpg")
    return pygame.transform.scale(image, (WIDTH, HEIGHT))

def titleText(screen, WIDTH, HEIGHT):
    font = pygame.font.Font("ComicSansbold.ttf", 256)
    textObj = font.render("Happy Drinks", True, DARK_GREY)
    text_rect = textObj.get_rect(center=(WIDTH//2,3*HEIGHT//9))
    screen.blit(textObj, text_rect)

def startButton(screen, WIDTH, HEIGHT):
    startButtonOutline = gameFunctions.Rect(3*WIDTH/10, (6*HEIGHT/10), 4*WIDTH/10, (HEIGHT/10))
    startButtonInline = gameFunctions.Rect(startButtonOutline.x+5,startButtonOutline.y+5,startButtonOutline.width-10,startButtonOutline.height-10)
    pygame.draw.rect(screen, DARK_GREY, (startButtonOutline.x, startButtonOutline.y, startButtonOutline.width, startButtonOutline.height))
    pygame.draw.rect(screen, LIGHT_GREY, (startButtonInline.x, startButtonInline.y, startButtonInline.width, startButtonInline.height))
    font = pygame.font.Font("ComicSans.ttf", 80)
    textObj = font.render("START", True, DARK_GREY)
    text_rect = textObj.get_rect(center=(startButtonOutline.x + startButtonOutline.width // 2, startButtonOutline.y + startButtonOutline.height // 2))
    screen.blit(textObj, text_rect)

def mainMenue(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey,iState):
    
    if event:
        if 3*WIDTH/10 <= mousex <= (3*WIDTH/10 + 4*WIDTH/10) and 6*HEIGHT/10 <= mousey <= 6*HEIGHT/10 + HEIGHT/10:
            print("Start")
            iState = 1
            event = False

    if refresh == True:
        background_image = background(WIDTH,HEIGHT)
        screen.blit(background_image, (0, 0))
        startButton(screen, WIDTH, HEIGHT)
        titleText(screen, WIDTH, HEIGHT)
        refresh == False

    return screen, refresh, event, iState

def charCreation(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey, iMode, iState):
    background_image = background(WIDTH,HEIGHT)
    screen.blit(background_image, (0, 0))
    
def main(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey, iState):
    iMode = 0
    if iState == 0:
        screen, refresh, event, iState = mainMenue(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey,iState)

    elif iState == 1:
        charCreation(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey, iMode, iState)
    
    return screen, refresh, event, iMode, iState
   
   