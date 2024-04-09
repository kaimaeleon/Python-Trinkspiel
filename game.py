import pygame, random
import lib.gameClass as gameclass
import lib.draw as draw
import json

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
    control.game = gameclass.Game(0,0,0)
    control = activePlayers(control)
    control.board = boardCreation()
    control.iState = 1
    print("Spieler",control.game.curP,"ist am Zug")
    return control

def gameLoop(control):
    graphics(control)
    
    #Wer ist dran
    if control.iState == 1:
        if control.players[control.game.curP].tile >= 39:
            control.iState = 10
            return control
        if control.helpVar is None:
            control.helpVar = 750
        else:
            control.helpVar -= 25
        txt="Du bist dran "+str(control.players[control.game.curP].name)
        draw.textVar(control.screen,txt,control.width//2,control.height//2,center=True,alpha=control.helpVar,txtSize=128)
        if control.helpVar <= 0 and control.event.new:
            control.event.new = False
            control.helpVar = 0
            control.iState = 2
            control.game.turnNo += 1
        
    #Würfeln
    if control.iState == 2:
        if control.helpVar < 15:
            control.helpVar += 1
            control.helpStr= str(random.randint(1,6))
            draw.textVar(control.screen,control.helpStr,control.width//2,control.height//2,center=True,txtSize=512)
        else:
            control.helpVar = random.randint(1,6)
            control.players[control.game.curP].dice = control.helpVar
            control.players[control.game.curP].tileLast = control.players[control.game.curP].tile
            control.helpVar = None
            control.iState = 3   
    
    #Wurf anzeigen
    if control.iState == 3: 
        if control.helpVar is None:
            control.helpVar = 750
        else:
            control.helpVar -= 25
        txt=str(control.players[control.game.curP].dice)
        draw.textVar(control.screen,txt,control.width//2,control.height//2,center=True,alpha=control.helpVar,txtSize=512)
        if control.helpVar <= 0:
            control.helpVar = None
            control.iState = 4

    #Wurf spielen
    if control.iState == 4:
        control.players[control.game.curP].tile = control.players[control.game.curP].dice + control.players[control.game.curP].tileLast
        if control.players[control.game.curP].tile >= 40:
            control.players[control.game.curP].tile = 39
        if control.helpVar is None:
            control.helpVar = 5
        elif control.helpVar <= 0:
            control.iState = 5
            control.helpVar = None
            return control
        else:
            control.helpVar -= 1
    
    #Ergebnis anzeigen
    if control.iState == 5:
        tile = control.board[control.players[control.game.curP].tile]
        txt = tile["str"]
        draw.textVar(control.screen,txt,control.width//2,control.height//2,center=True,txtSize=128)
        if control.event.new:
            control.event.new = False
            control.iState = 6 
            return control
        
    #Aufgabe beendet
    if control.iState == 6:
        tile = control.board[control.players[control.game.curP].tile]
        txt = tile["str"]
        if control.helpVar is None:
            control.helpVar = 255
        else:
            control.helpVar -= 25
        draw.textVar(control.screen,txt,control.width//2,control.height//2,center=True,alpha=control.helpVar,txtSize=128)
        if control.helpVar <= 0:
            control.helpVar = None
            control.iState = 10  
            return control

    #next turn
    if control.iState >= 10:
        if control.helpVar is None:
            control.helpVar = 5
        elif control.helpVar <= 0:        
            control.game.curP += 1
            if control.game.curP >= control.game.actP:
                control.game.curP = 0
            print("Spieler",control.game.curP,"ist am Zug")
            control.iState = 1
            control.helpVar = None
        else:
            control.helpVar -= 1
    
    return control

def graphics(control):
    draw.fill(control.screen)
    playboard(control)
    hud(control)
    players(control)

def hud(control):
    w,h=control.width,control.height
    actP=control.game.actP
    color = ["red","blue","green","pink","yellow","purple","orange","cyan","brown"]
    for i in range(actP):
        if control.game.curP == i and control.loops%10<5:
            colorOut, colorIn, colorTxt = DARK_WHITE, LIGHT_WHITE, DARK_GREY
        else:
            colorOut, colorIn, colorTxt = draw.colorHandling(color[i])
        text = control.players[i].name
        draw.rectText(control.screen,0,i*h//actP,w//5,h//actP,text,colorRectOut=colorOut,colorRectIn=colorIn,colorText=colorTxt)
        #Sips Counter to be continued....
        #draw.text(control.screen,"Sips gesippt: "+str(control.players[actPArray[i]-1].sips),10,50+i*h//actP)
    draw.text(control.screen,"Zug: "+str(control.game.turnNo),5+w//5,5)

def playboard(control):
    w,h=control.width,control.height
    tileSize = h//6
    board = control.board
    tileCounter = 0
    draw.rect(control.screen,LIGHT_PAPER,w // 5 + 55, 55,8*tileSize+10,5*tileSize+10)
    for j in range(5):
        if j % 2 == 0: 
            for i in range(8):
                colorOut, colorIn, colorTxt = draw.colorHandling(board[tileCounter]["color"])
                draw.rectText(control.screen, w // 5 + 60 + tileSize * i, 60 + tileSize * j, tileSize, tileSize, board[tileCounter]["display"], colorRectOut=colorOut, colorRectIn=colorIn, colorText=colorTxt)
                tileCounter += 1
        else:
            for i in range(8):
                colorOut, colorIn, colorTxt = draw.colorHandling(board[tileCounter]["color"])
                draw.rectText(control.screen, w // 5 + 60 + tileSize * (7-i), 60 + tileSize * j, tileSize, tileSize, board[tileCounter]["display"], colorRectOut=colorOut, colorRectIn=colorIn, colorText=colorTxt)
                tileCounter += 1
    for i in range(2):
        pygame.draw.line(control.screen,LIGHT_PAPER,(w//5+60,60+tileSize+tileSize*2*i),(w//5+60+tileSize*7,60+tileSize+tileSize*2*i),5)
        pygame.draw.line(control.screen,LIGHT_PAPER,(w//5+60+tileSize,60+2*tileSize+tileSize*2*i),(w//5+60+tileSize*8,60+2*tileSize+tileSize*2*i),5)

def activePlayers(control):
    nonActPArray = []
    for player in control.players:
        if player.name != ("Spieler "+str(player.nr)):
            control.game.actP += 1
        else:
            nonActPArray.append(player.nr-1)
    print(control.game.actP,"Spieler sind aktiv")
    for i in reversed(nonActPArray):
        del control.players[i]
    for i in range(len(control.players)):
        control.players[i].nr = i
    #putting them in order
    return control

def boardCreation():
    file = open('tiles.json')
    data = json.load(file)
    tileCount = 0
    for key in data:
        tileCount += 1
    print(tileCount,"mögliche Felder")
    board = []
    keys = list(data.keys())
    for i in range(0,40):
        if i == 0:
            board.append(data["Start"])
            keys.remove("Start")
            keys.remove("Ende")
            print(keys)
        elif i == 39:
            board.append(data["Ende"])
        else:
            randKey = random.choice(keys)
            print(randKey)
            if "max" in data[randKey]:
                count = board.count(data[randKey])
                print(randKey,"besitzt max")
                print("kommt bisher",count,"mal vor")
                if data[randKey]["max"] <= count or "max" in board[i-1]:
                    randKey = data[randKey]["else"]
                    print("Erstezt durch ", randKey)
            board.append(data[randKey])
    return board
    
def players(control):
    w,h=control.width,control.height
    color = ["red","blue","green","pink","yellow","purple","orange","cyan","brown"]
    #tile0 middle point
    tileSize = h//6
    tileX0 = w // 5 + 60 + tileSize//2
    tileY0 = 60 +  tileSize//2

    #check for players on the same tile
    for i in range(40):
        playersOnTile = []
        x,y=0,0
        for pl in control.players:
            if i == pl.tile:
                playersOnTile.append(pl.nr)
        if (i//8)%2==0:
            x = (i%8)*tileSize+tileX0
        else:
            x = (7-(i%8))*tileSize+tileX0
        y = i//8*tileSize+tileY0
        if len(playersOnTile) == 1:
            if control.game.curP == playersOnTile[0] and control.loops%10<5:
                colorOut, colorIn = DARK_WHITE, LIGHT_WHITE
            else:
                colorOut, colorIn, colorTxt = draw.colorHandling(color[playersOnTile[0]])
            draw.circ(control.screen,x,y,35,colorIn=colorIn,colorOut=colorOut)
        else:
            i=0
            for pl in reversed(playersOnTile):
                if control.game.curP == pl and control.loops%10<5:
                    colorOut, colorIn, colorTxt = DARK_WHITE, LIGHT_WHITE, DARK_GREY
                else:
                    colorOut, colorIn, colorTxt = draw.colorHandling(color[pl])
                if i % 5 == 0:
                    draw.circ(control.screen,x,y,25,colorIn=colorIn,colorOut=colorOut)
                if i % 5 == 1:
                    draw.circ(control.screen,x-60,y+60,25,colorIn=colorIn,colorOut=colorOut)
                if i % 5 == 2:
                    draw.circ(control.screen,x+60,y+60,25,colorIn=colorIn,colorOut=colorOut)
                if i % 5 == 3:
                    draw.circ(control.screen,x-60,y-60,25,colorIn=colorIn,colorOut=colorOut)
                if i % 5 == 4:
                    draw.circ(control.screen,x+60,y-60,25,colorIn=colorIn,colorOut=colorOut)
                i+=1
    return control

    

    