import pygame, random, time
import lib.gameClass as gameclass
import lib.draw as draw

def main(control):
    if control.iState == 0:
        control.game = gameclass.Game(0,0,0,0)
        control = activePlayers(control)
        control.iState = 1

    return control

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