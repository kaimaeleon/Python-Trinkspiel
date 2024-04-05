import pygame, random, time
import lib.gameClass as gameclass
import lib.draw as draw
import json as js

DARK_GREY       = draw.DARK_GREY   
LIGHT_GREY      = draw.LIGHT_GREY  
DARK_PAPER      = draw.DARK_PAPER  
LIGHT_PAPER     = draw.LIGHT_PAPER 
DARK_RED        = draw.DARK_RED    
LIGHT_RED       = draw.LIGHT_RED   
DARK_BLUE       = draw.DARK_BLUE   
LIGHT_BLUE      = draw.LIGHT_BLUE  
DARK_GREEN      = draw.DARK_GREEN  
LIGHT_GREEN     = draw.LIGHT_GREEN 
DARK_YELLOW     = draw.DARK_YELLOW 
LIGHT_YELLOW    = draw.LIGHT_YELLOW
DARK_ORANGE     = draw.DARK_ORANGE 
LIGHT_ORANGE    = draw.LIGHT_ORANGE
DARK_PURPLE     = draw.DARK_PURPLE 
LIGHT_PURPLE    = draw.LIGHT_PURPLE
DARK_PINK       = draw.DARK_PINK   
LIGHT_PINK      = draw.LIGHT_PINK  
DARK_CYAN       = draw.DARK_CYAN   
LIGHT_CYAN      = draw.LIGHT_CYAN  
DARK_BROWN      = draw.DARK_BROWN  
LIGHT_BROWN     = draw.LIGHT_BROWN 
DARK_WHITE      = draw.DARK_WHITE
LIGHT_WHITE     = draw.LIGHT_WHITE

def main(control):
    if control.iState == 0:
        control = init(control)
    if control.iState >= 1:
        control = gameLoop(control)
    return control

def init(control):
    control.game = gameclass.Game(0,0,0,0)
    control = activePlayers(control)
    control.board = boardCreation()
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
    draw.fill(control.screen)
    playboard(control)
    hud(control)

def hud(control):
    w,h=control.width,control.height
    actP=control.game.actP
    actPArray = control.game.actPArray
    color = ["red","blue","green","pink","yellow","purple","orange","cyan","brown"]
    for i in range(actP):
        colorOut, colorIn, colorTxt = draw.colorHandling(color[i])
        text = control.players[actPArray[i]-1].name
        draw.rectText(control.screen,0,i*h//actP,w//5,h//actP,text,colorRectOut=colorOut,colorRectIn=colorIn,colorText=colorTxt)
        #Sips Counter to be continued....
        #draw.text(control.screen,"Sips gesippt: "+str(control.players[actPArray[i]-1].sips),10,50+i*h//actP)
    draw.text(control.screen,"Zug: "+str(control.game.turnNo),5+w//5,5)



def playboard(control):
    w,h=control.width,control.height
    tileSize = h//6
    board = control.board
    tileCounter = 0
    draw.rect(control.screen,DARK_GREY,w // 5 + 55, 55,8*tileSize+10,5*tileSize+10)
    for j in range(5):
        for i in range(8):
            colorOut, colorIn, colorTxt = draw.colorHandling(board[tileCounter]["color"])
            draw.rectText(control.screen, w // 5 + 60 + tileSize * i, 60 + tileSize * j, tileSize, tileSize, board[tileCounter]["display"], colorRectOut=colorOut, colorRectIn=colorIn, colorText=colorTxt)
            tileCounter += 1
    for i in range(2):
        pygame.draw.line(control.screen,DARK_GREY,(w//5+60,60+tileSize+tileSize*2*i),(w//5+60+tileSize*7,60+tileSize+tileSize*2*i),5)
        pygame.draw.line(control.screen,DARK_GREY,(w//5+60+tileSize,60+2*tileSize+tileSize*2*i),(w//5+60+tileSize*8,60+2*tileSize+tileSize*2*i),5)

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

def boardCreation():
    file = open('tiles.json')
    data = js.load(file)
    print( data)
    tileCount = 0
    for key in data:
        tileCount += 1
    print(tileCount,"mögliche Felder")
    board = []
    for i in range(0,40):
        if i == 0:
            board.append(data["Start"])
        elif i == 39:
            board.append(data["Ende"])
        else:
            randKey = "Start"
            while randKey == "Start" or randKey == "Ende":
                randKey = random.choice(list(data.keys()))
            board.append(data[randKey])
    return board
    
    