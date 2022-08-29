import pygame
from checkers.game import *
from checkers.constants import *
from checkers.board import Board
from startpage.startwindow import Piece_menu, main_menu
from startpage.button import Button
from startpage.startwindow import Piece_menu
from re import I

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Among-Us')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE  
    col = x // SQUARE_SIZE
    return row, col  

def main():

    main_menu()

    run = True
    clock = pygame.time.Clock() 
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            # print(game.winner())
            SCREEN.fill(BLACK)
            print(game.winner(game.board))
            # game.board.pink_left = game.board.blue_left = 12

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