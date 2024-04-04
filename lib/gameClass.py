class Control:
    def __init__(self,screen = None,width = None,height = None,refresh = True,event = None, iMode = 1, iState = 0, players = None, game = None):
        self.screen = screen
        self.width = width
        self.height = height
        self.refresh = refresh
        self.event = event
        self.iMode = iMode
        self.iState = iState
        self.players = players
        self.game = game

class Event:
    def __init__(self, new, mouseX, mouseY, key, funcKey):
        self.new = new
        self.mouseX = mouseX
        self.mouseY = mouseY
        self.key = key
        self.funcKey = funcKey

class Game:
    def __init__(self,actP,actPArray,curP,turnNo):
        self.actP = actP
        self.actPArray = actPArray
        self.curP = curP
        self.turnNo = turnNo
    
class Player:
    def __init__(self, name, field, nr, sips):
        self.name = name
        self.field = field
        self.nr = nr
        self.sips = sips

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
