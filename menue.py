import pygame
import numpy as np
import gameClass

DARK_GREY = (64,64,64)
LIGHT_GREY = (224,224,224)
LIGHT_PAPER = (255,255,213)
DARK_PAPER = (230,230,177)

def background(WIDTH, HEIGHT):
    image = pygame.image.load("bg-menue.jpg")
    return pygame.transform.scale(image, (WIDTH, HEIGHT))

def titleText(screen, WIDTH, HEIGHT):
    font = pygame.font.Font("ComicSansbold.ttf", 256)
    textObj = font.render("Happy Drinks", True, DARK_GREY)
    text_rect = textObj.get_rect(center=(WIDTH//2,3*HEIGHT//9))
    screen.blit(textObj, text_rect)

def subtitleText(screen, text , x, y, center=False):
    font = pygame.font.Font("ComicSansbold.ttf", 96)
    textObj = font.render(text, True, DARK_GREY)
    if not center:
        text_rect = textObj.get_rect()
        text_rect.topleft = (x,y)
    elif center:
        text_rect = textObj.get_rect(center=(x,y))
    screen.blit(textObj, text_rect)

def text(screen, text , x, y):
    font = pygame.font.Font("ComicSansbold.ttf", 32)
    textObj = font.render(text, True, DARK_GREY)
    text_rect = textObj.get_rect()
    text_rect.topleft = (x,y)
    screen.blit(textObj, text_rect)

def rect(screen, color, x,y,w,h):
    pygame.draw.rect(screen, color, (x,y,w,h))

def rectText(screen, x, y, w, h, str):
    rect(screen, DARK_GREY, x,y, w, h)
    rect(screen, LIGHT_GREY,x+5,y+5, w-10, h-10)
    subtitleText(screen, str, x+w//2, y+h//2, True)

def startButton(screen, WIDTH, HEIGHT):
    startButtonOutline = gameClass.Rect(3*WIDTH/10, (6*HEIGHT/10), 4*WIDTH/10, (HEIGHT/10))
    startButtonInline = gameClass.Rect(startButtonOutline.x+5,startButtonOutline.y+5,startButtonOutline.width-10,startButtonOutline.height-10)
    pygame.draw.rect(screen, DARK_GREY, (startButtonOutline.x, startButtonOutline.y, startButtonOutline.width, startButtonOutline.height))
    pygame.draw.rect(screen, LIGHT_GREY, (startButtonInline.x, startButtonInline.y, startButtonInline.width, startButtonInline.height))
    font = pygame.font.Font("ComicSans.ttf", 80)
    textObj = font.render("START", True, DARK_GREY)
    text_rect = textObj.get_rect(center=(startButtonOutline.x + startButtonOutline.width // 2, startButtonOutline.y + startButtonOutline.height // 2))
    screen.blit(textObj, text_rect)

def charBox(screen, WIDTH, HEIGHT, x, y, name):
    rect(screen, DARK_GREY, x,y, WIDTH//4, HEIGHT//13)
    rect(screen, LIGHT_GREY,x+5,y+5, WIDTH//4-10, HEIGHT//13-10)
    text(screen, name, x+5, y+5)

def charInterface(screen, WIDTH, HEIGHT, players):
    subtitleText(screen, "Spieler:",WIDTH//30, HEIGHT//13-25)
    for player in players:
        charBox(screen, WIDTH, HEIGHT, WIDTH//30, (player.nr+1)*HEIGHT//13+25,player.name)
    rectText(screen, WIDTH//30, 10*HEIGHT//13+50, WIDTH//15, WIDTH//15, "<")


def mainMenue(screen, refresh, WIDTH, HEIGHT, event, mousex, mousey, iState):
    #Logic
    if event:
        if 3*WIDTH/10 <= mousex <= (3*WIDTH/10 + 4*WIDTH/10) and 6*HEIGHT/10 <= mousey <= 6*HEIGHT/10 + HEIGHT/10:
            print("Start")
            iState = 1
            event = False

    #Graphics
    if refresh == True:
        background_image = background(WIDTH,HEIGHT)
        screen.blit(background_image, (0, 0))
        startButton(screen, WIDTH, HEIGHT)
        titleText(screen, WIDTH, HEIGHT)
        refresh == False

    return screen, refresh, event, iState

def charCreation(screen, refresh, WIDTH, HEIGHT,event,mousex, mousey, iMode, iState, players, key):
    #Logic
    if iState == 1:
        activePlayer = 0
    if event:
        if WIDTH//30 <= mousex <= WIDTH//30+WIDTH//15 and 10*HEIGHT//13+50 <= mousey <= 10*HEIGHT//13+50+WIDTH//15:
            iState = 0
            print("zurück")
        event = False
        if  WIDTH//30 <= mousex <= WIDTH//30+WIDTH//4:
            for player in players:
                if (player.nr+1)*HEIGHT//13+25 < mousey < (player.nr+1)*HEIGHT//13+25+HEIGHT//13:
                    activePlayer = player.nr
                    print(activePlayer)
                    iState=2
                    players[activePlayer].name = ""
        if iState ==2:
            if event and key == pygame.K_RETURN:
                iState = 1
            if event and key is not None:
                players[activePlayer].name += key.unicode
    
                    


    if iState != 1:
        return screen, refresh, event, iState, players

    #Graphics
    if refresh:
        background_image = background(WIDTH,HEIGHT)
        screen.blit(background_image, (0, 0))
        if iState == 1:
            charInterface(screen, WIDTH, HEIGHT, players)
        if iState == 2:
            rectText(screen,WIDTH//2, HEIGHT//13, 400,200, "Neuen Namen hier eingeben:")
        refresh == False
    
    return screen, refresh, event, iState, players


    
def main(screen, refresh, WIDTH, HEIGHT,event,mousex,mousey, iState, players, key):
    iMode = 0
    if iState == 0:
        screen, refresh, event, iState= mainMenue(screen, refresh, WIDTH, HEIGHT, event, mousex, mousey, iState)

    elif iState >= 1:
        screen, refresh, event, iState, players = charCreation(screen, refresh, WIDTH, HEIGHT, event, mousex, mousey, iMode, iState, players, key)
    
    return screen, refresh, event, iMode, iState, players
   
   