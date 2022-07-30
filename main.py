import pygame
from checkers.constants import *
from checkers.board import Board
from startpage.startwindow import Piece_menu
from startpage.button  import Button



FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Among-Us')


def main():

    #game variables
    game_paused = False

    run_startpage = True
    while run_startpage:

        SCREEN.fill(WHITE)
        SCREEN.blit(STARTPAGE_BK, (STARTPAGE_BK_rect))

        
        #print button
        if game_paused == False:
             if SELECPLAYER_BTN.draw(SCREEN):
                Piece_menu()
             if LEVELS_BTN.draw(SCREEN):
                game_paused = True
             if PLAY_BTN.draw(SCREEN):
                run_startpage = False
             if QUITE_BTN.draw(SCREEN):
                pygame.quit()  
        else:
            SELECPLAYER_BTN.draw(SCREEN)
            

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
            #if event.type == pygame.QUIT:
                # run = False

        pygame.display.update()

    

    run = True
    clock = pygame.time.Clock() 
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass    

        board.draw(WIN) 
        pygame.display.update()     
        
    pygame.quit()

main()