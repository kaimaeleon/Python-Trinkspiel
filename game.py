import pygame, random, time
import lib.gameClass as gameclass
import lib.draw as draw

def main(control):
    if control.iState == 0:
        control = init(control)
    if control.iState >= 1:
        control = gameLoop(control)
        print("gameLoop")
    return control

def init(control):
    control.game = gameclass.Game(0,0,0,0)
    control = activePlayers(control)
    control.iState = 1
    return control

def gameLoop(control):
    graphics(control)
    
    #next turn
    if control.iState >= 10:
        control.game.curP += 1
        if control.game.curP >= control.game.actP:
            control.game.curP = 0
        control.game.turnNo += 1
    return control

def graphics(control):
    print("Graphics")
    draw.fill(control.screen)
    #playboard(control)
    hud(control)

def hud(control):
    w,h=control.width,control.height
    actP=control.game.actP
    actPArray = control.game.actPArray
    for i in range(actP):
        text = control.players[actPArray[i]-1].name
        draw.rectText(control.screen,0,i*h//actP,w//5,h//actP,text)
        draw.text(control.screen,"Sips gesippt: "+str(control.players[actPArray[i]-1].sips),10,50+i*h//actP)
    draw.text(control.screen,"Zug: "+str(control.game.turnNo),5+w//5,5)



def playboard(control):
    w,h=control.width,control.height
    draw.rectText(control.screen,(1/2)*(w-h),0,w-h,h,"Spielbrett", "subtitle", True)


def activePlayers(control):
    control.game.actPArray = []
    for player in control.players:
        print("Spielername:", player.name,"aktiv wenn übereinstimmt mit:","Spieler "+str(player.nr))
        if player.name != ("Spieler "+str(player.nr)):
            control.game.actP += 1
            control.game.actPArray.append(player.nr)
            print("aktiv")
        else:
            print("nicht aktiv")
    print(control.game.actP,"Spieler sind aktiv")
    print("Array:",control.game.actPArray)
    return control