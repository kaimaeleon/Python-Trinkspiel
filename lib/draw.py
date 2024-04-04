import pygame
import lib.gameClass as gameClass

#Color Sheet
DARK_GREY = (64,64,64)
LIGHT_GREY = (224,224,224)
DARK_PAPER = (230,230,177)
LIGHT_PAPER = (255,255,213)
DARK_RED = (150,0,0)
LIGHT_RED = (226,0,0)
DARK_BLUE = (0,0,50)
LIGHT_BLUE = (0,0,220)
DARK_GREEN = (0,100,0)
LIGHT_GREEN = (0,200,0)
DARK_YELLOW = (222,222,0)
LIGHT_YELLOW = (255,255,0)
DARK_ORANGE = (170,115,0)
LIGHT_ORANGE = (255,170,0)
DARK_PURPLE = (100,0,130)
LIGHT_PURPLE = (170,0,235)
DARK_PINK = (150,0,150)
LIGHT_PINK = (240,0,255)
DARK_CYAN = (0,102,102)
LIGHT_CYAN = (0,204,204)
DARK_BROWN = (110,50,0)
LIGHT_BROWN = (170,70,0)



def background(w, h, image):
    image = pygame.image.load(image)
    return pygame.transform.scale(image, (w, h))

def fill(screen, color=LIGHT_PAPER):
    screen.fill(color)
    

def text(screen, text , x, y, color=DARK_GREY, center=False):
    font = pygame.font.Font("ComicSansbold.ttf", 32)
    textObj = font.render(text, True, color)
    if not center:
        text_rect = textObj.get_rect()
        text_rect.topleft = (x,y)
    elif center:
        text_rect = textObj.get_rect(center=(x,y))
    screen.blit(textObj, text_rect)

def titleText(screen, text, x, y, color=DARK_GREY, center=False):
    font = pygame.font.Font("ComicSansbold.ttf", 256)
    textObj = font.render(text, True, color)
    if not center:
        text_rect = textObj.get_rect()
        text_rect.topleft = (x,y)
    elif center:
        text_rect = textObj.get_rect(center=(x,y))
    screen.blit(textObj, text_rect)

def subtitleText(screen, text , x, y, color=DARK_GREY, center=False):
    font = pygame.font.Font("ComicSansbold.ttf", 96)
    textObj = font.render(text, True, color)
    if not center:
        text_rect = textObj.get_rect()
        text_rect.topleft = (x,y)
    elif center:
        text_rect = textObj.get_rect(center=(x,y))
    screen.blit(textObj, text_rect)

def rect(screen, color, x,y,w,h, center=False):
    if center:
        pygame.draw.rect(screen, color, (x-w/2,y-h/2,w,h))
    else:
        pygame.draw.rect(screen, color, (x,y,w,h))

def rectText(screen, x, y, w, h, str,format="text",center=False, colorRectOut=DARK_GREY, colorRectIn=LIGHT_GREY, colorText=DARK_GREY):
    rect(screen, colorRectOut, x,y, w, h)
    rect(screen, colorRectIn,x+5,y+5, w-10, h-10)
    if format == "text" and center:
        text(screen, str, x+w//2, y+h//2, colorText, center)
    elif format == "text":
        text(screen, str, x+10, y+10, colorText)
    if format == "subtitle" and center:
        subtitleText(screen, str, x+w//2, y+h//2, colorText, center)
    elif format == "subtitle":
        subtitleText(screen, str, x+10, y+10, colorText)
    if format == "title" and center:
        titleText(screen, str, x+w//2, y+h//2, colorText, center)
    elif format == "title":
        titleText(screen, str, x+10, y+10, colorText)
    
  


