import pygame
import startpage.button  
from checkers.constants import *
pygame.font.init()



def Piece_menu():
    pygame.display.set_caption("Pieces Menu")

    #game variables
    game_paused = False


    run = True
    while run:

        SCREEN.fill(WHITE)
        SCREEN.blit(PLAYERPAGE_BK, (STARTPAGE_BK_rect))

        
        #print button
        if game_paused == False:
             if ORANGE_BTN.draw(SCREEN):
                pass #generate player screen
             if BLUE_BTN.draw(SCREEN):
                pass #main()
             if WHITE_BTN.draw(SCREEN):
                pygame.quit()
             #if QUITE_BTN.draw(SCREEN):
                #run = False  #this currently end the start screen but need to end entire game
        else:
             ORANGE_BTN.draw(SCREEN)
            

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
            #if event.type == pygame.QUIT:
                # run = False

        pygame.display.update()

    pygame.quit()