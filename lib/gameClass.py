class Control:
    def __init__(self,screen = None,width = None,height = None,refresh = True,event = None, iMode = 1, iState = 0, players = None, game = None, board = None):
        self.screen = screen
        self.width = width
        self.height = height
        self.refresh = refresh
        self.event = event
        self.iMode = iMode
        self.iState = iState
        self.players = players
        self.game = game
        self.board = board

class Event:
    def __init__(self, new, mouseX, mouseY, key, funcKey):
        self.new = new
        self.mouseX = mouseX
        self.mouseY = mouseY
        self.key = key
        self.funcKey = funcKey

class Game:
    def __init__(self,actP,curP,turnNo):
        self.actP = actP
        self.curP = curP
        self.turnNo = turnNo

class Tile:
    def __init__(self, id, color, str, sips):
        self.id = id
        self.color = color
        self.str = str
        self.sips = sips
        

class Player:
    def __init__(self, name, nr, sips, tile):
        self.name = name
        self.nr = nr
        self.sips = sips
        self.tile = tile

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
