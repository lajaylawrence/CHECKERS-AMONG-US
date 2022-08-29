import pygame
import startpage.button  
from checkers.constants import *
from checkers.board import *
pygame.font.init()


def Select_players():
        PLAYER1 = Piece_menu()
        if PLAYER1 == ORANGE_PLAYER:
            PLAYER2 = BLUE_PLAYER   #random.choice(BLUE_PLAYER, WHITE_PLAYER)
        if PLAYER1 == BLUE_PLAYER:
            PLAYER2 = WHITE_PLAYER  #random.choice(ORANGE_PLAYER, WHITE_PLAYER)
        if PLAYER1 == WHITE_PLAYER:
            PLAYER2 = PINK_PLAYER #random.choice(ORANGE_PLAYER, BLUE_PLAYER)
        if PLAYER1 == PINK_PLAYER:
            PLAYER2 = ORANGE_PLAYER
        return PLAYER1, PLAYER2

def main_menu():
    game_paused = False
    run_startpage = True
    while run_startpage:

        SCREEN.fill(WHITE)
        SCREEN.blit(STARTPAGE_BK, (STARTPAGE_BK_rect))

        
        #print button
        if game_paused == False:
             #if SELECPLAYER_BTN.draw(SCREEN):
                #Piece_menu()
                #run_startpage = False
             if LEVELS_BTN.draw(SCREEN):
                game_paused = True
             if PLAY_BTN.draw(SCREEN):
                PLAYERS.append(Select_players()[0])
                PLAYERS.append(Select_players()[1])
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


def Piece_menu():
    pygame.display.set_caption("Pieces Menu")
    pygame.init()

    #game variables
    game_paused = False


    run = True
    while run:

        SCREEN.fill(WHITE)
        SCREEN.blit(PLAYERPAGE_BK, (STARTPAGE_BK_rect))

        
        #print button
        if game_paused == False:
             if ORANGE_BTN.draw(SCREEN):
                PIECE = ORANGE_PLAYER
                return PIECE
             if BLUE_BTN.draw(SCREEN):
                PIECE = BLUE_PLAYER
                return PIECE
             if WHITE_BTN.draw(SCREEN):
                PIECE = WHITE_PLAYER
                return PIECE
             if PINK_BTN.draw(SCREEN):
                PIECE = PINK_PLAYER
                return PIECE
                #pygame.quit()
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