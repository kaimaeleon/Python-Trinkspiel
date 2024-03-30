import pygame
import lib.draw as draw
import lib.gameClass as gameClass

DARK_GREY   = draw.DARK_GREY  
LIGHT_GREY  = draw.LIGHT_GREY 
LIGHT_PAPER = draw.LIGHT_PAPER
DARK_PAPER  = draw.DARK_PAPER 

def main(control):
    #State Logic
    if control.iState == 0:
       control = startScreen(control)
    if control.iState > 0:
        control = charCreation(control)
    return control
    
def startScreen(control):
    w,h=control.width,control.height
    if control.event.new:
        control.event.new = False
        if 3*w//10 <= control.event.mouseX <= (7*w//10) and 6*h//10 <= control.event.mouseX <= (7*w//10):
            print("Start")
            control.iState = 1
            control.refresh = True
            return control
    if control.refresh:
        control.refresh = False
        backgroundImage = draw.background(w,h,"bg-menue.jpg")
        control.screen.blit(backgroundImage, (0,0))
        draw.titleText(control.screen,"Happy Drinks",w//2,h//3,center=True)
        draw.rectText(control.screen,3*w//10, 6*h//10, 4*w//10, h//10, "START",format="subtitle",center=True)
    return control

def charCreation(control):
    w,h=control.width,control.height
    if control.event.new:
        control.event.new = False
        if w//30 <= control.event.mouseX <= w//30+w//13 and 10*h//13 < control.event.mouseY <= 10*h//13+w//13:
            control.iState = 0
            control.refresh = True       
            return control
        if control.iState > 1:
            if control.event.key is not None and control.iState :
                control.players[control.iState-2].name += control.event.key
                control.event.key = None
                control.refresh = True
            elif control.event.funcKey == "backspace":
                control.event.funcKey = None
                control.players[control.iState-2].name = control.players[control.iState-2].name[:-1]
                control.refresh = True
            elif control.event.funcKey == "return":
                control.event.funcKey = None
                control.iState = 1
                control.refresh = True
        if w//30 <= control.event.mouseX <= 11*w//30:
            for player in control.players:
                if (player.nr+1)*h//13 < control.event.mouseY < (player.nr+2)*h//13:
                    print("Spieler ", player.nr)
                    control.players[player.nr-1].name = ""
                    control.iState = player.nr+1
                    control.refresh = True
                    control.event.mouseX,control.event.mouseY = 0,0

    #Graphics
    if control.refresh:
        control.refresh = False
        backgroundImage = draw.background(w,h,"bg-menue.jpg")
        control.screen.blit(backgroundImage, (0,0))
        draw.subtitleText(control.screen,"Spieler:",w//30,h//30)
        for player in control.players:
            draw.rectText(control.screen, w//30, (1+player.nr)*h//13,w//3,h//13,player.name)
        draw.rectText(control.screen, w//30, 10*h//13, w//13, w//13, "<", "subtitle",True)
    return control

