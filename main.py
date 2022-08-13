import pygame, random
from checkers.game import Game
from checkers.constants import *
from checkers.board import Board
from startpage.startwindow import Piece_menu
from startpage.button  import Button

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Among-Us')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE  
    col = x // SQUARE_SIZE
    return row, col  

def Select_players():
        PLAYER1 = Piece_menu()
        if PLAYER1 == ORANGE_PLAYER:
            PLAYER2 = random.choice(WHITE_IMG, BLUE_PLAYER)
        if PLAYER1 == BLUE_PLAYER:
            PLAYER2 = random.choice(ORANGE_PLAYER, WHITE_PLAYER)
        if PLAYER1 == WHITE_PLAYER:
            PLAYER2 = random.choice(ORANGE_PLAYER, BLUE_PLAYER)
            
def main():

    #game variables
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
                Piece_menu()
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
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col =  get_row_col_from_mouse(pos)
                game.select(row, col)


        game.update()     
        
    pygame.quit()

main()