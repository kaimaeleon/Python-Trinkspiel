import game, menue
import pygame
import sys
import numpy



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
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                newEvent = True

        if iMode == 0:
            screen, refresh, newEvent, iMode, iState = menue.main(screen, refresh, WIDTH, HEIGHT, newEvent, mousex, mousey, iState)
            
        elif iMode == 1:
            screen, refresh, newEvent, iMode = game.main(screen, refresh, WIDTH, HEIGHT)
        
        pygame.display.flip()  # Aktualisiere den Bildschirm
    


pygame.quit()
