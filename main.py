import menue
import pygame
import sys
import lib.gameClass as gameClass

pygame.init()
screen_info = pygame.display.Info()
eventInstance=gameClass.Event(False,0,0,None, None)
control = gameClass.Control(screen=0,iMode=0,iState=0,width=screen_info.current_w, height=screen_info.current_h, refresh=True, event=eventInstance,players = [gameClass.Player("Spieler " + str(i), 0, i) for i in range(1, 9)])
control.screen = pygame.display.set_mode((control.width, control.height), pygame.FULLSCREEN)
pygame.display.set_caption("Trinkspiel")

if __name__ == "__main__":
    run = True
    control.iMode = 1
    players = [gameClass.Player("Spieler " + str(i), 0, i) for i in range(1, 9)]
    while run:
        #Input Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                control.event.new = True
                control.event.mouseX, control.event.mouseY = pygame.mouse.get_pos()
                print(control.event.mouseX, control.event.mouseY)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    control.event.new = True
                    control.event.funcKey = "return"
                    control.event.key = None
                    print(control.event.funcKey)
                elif event.key == pygame.K_BACKSPACE:
                    control.event.new = True
                    control.event.funcKey = "backspace"
                    control.event.key = None
                    print(control.event.funcKey)
                else:
                    control.event.new = True
                    control.event.funcKey = None
                    control.event.key = event.unicode
                    print(control.event.key)
              
        #Gamestates
        if control.iMode == 0:
            run = False
        if control.iMode == 1:
            control = menue.main(control)
        if control.iMode == 2:
            print("Game")
       
        #refresh screen
        pygame.display.flip() 
#End
pygame.quit()


