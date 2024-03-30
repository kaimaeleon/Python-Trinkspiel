class Control:
    def __init__(self,screen,width,height,refresh,event, iMode, iState, players):
        self.screen = screen
        self.width = width
        self.height = height
        self.refresh = refresh
        self.event = event
        self.iMode = iMode
        self.iState = iState
        self.players = players

class Event:
    def __init__(self, new, mouseX, mouseY, key, funcKey):
        self.new = new
        self.mouseX = mouseX
        self.mouseY = mouseY
        self.key = key
        self.funcKey = funcKey

class Player:
    def __init__(self, name, field, nr):
        self.name = name
        self.field = field
        self.nr = nr

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
