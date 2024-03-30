import game, menue
import pygame
import sys
import numpy
import gameClass



pygame.init()
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Trinkspiel")

iMode = 0
iState = 0
refresh = True
mousex, mousey = 0, 0
newEvent = False


if __name__ == "__main__":
    run = True
    players = [gameClass.Player("Spieler " + str(i), 0, i) for i in range(1, 9)]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                newEvent = True
            if event.type == pygame.KEYDOWN:
                key = event.key
                newEvent = True


        if iMode == 0:
            screen, refresh, newEvent, iMode, iState, players = menue.main(screen, refresh, WIDTH, HEIGHT, newEvent, mousex, mousey, iState, players, key)
            
        elif iMode == 1:
            screen, refresh, newEvent, iMode = game.main(screen, refresh, WIDTH, HEIGHT)
        
        pygame.display.flip()  # Aktualisiere den Bildschirm
    


pygame.quit()
