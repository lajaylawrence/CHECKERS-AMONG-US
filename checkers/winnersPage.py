import pygame 
from checkers.constants import *
from checkers.board import *
from startpage.startwindow import main_menu, Select_players
pygame.font.init()


# WINNNERS PAGEs
def winning_menu(game):
    pygame.display.set_caption("WinnerScreen")
    run = True
    # game.board.get_winner_image()
    # p1, p2 = Select_players()
    # print(p1)
    p1 = PLAYERS[0]
    p2 = PLAYERS[1]

    while run:
            # print("blue_player")
        game.board.get_winner_image(p1,p2)
         
        
        # new
        # SCREEN.fill(BLACK)
        # SCREEN.blit(ORANGE_KILLP, (ORANGE_KILLP_rect))
        # game.board.get_winner_image(p1,p2)
        #print button
        if MAINMENU_BTN.draw(SCREEN):
            main_menu()
        if QUIT_BTN.draw(SCREEN):
            run = False
            pygame.quit()
        
            

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    # PLAYERS = []

    pygame.quit()
