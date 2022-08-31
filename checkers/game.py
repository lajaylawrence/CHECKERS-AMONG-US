import pygame
from .constants import *
from .board import Board
from .winnersPage import winning_menu
# from startpage.startwindow import main_menu 

class Game: 
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win) 
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    #single underscore infront means private
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYERS[0]
        self.valid_moves = {}

    def winner(self):
        # return Board.winner()
        # return self.board.winner(self)
        return self.board.winner(self)
        # return winning_menu(self)

    def reset(self):
        self._init()

    #select a piece and show if there is any valid moves
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
    
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.image == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False
    
    #allow the piece to move into a valid(new) position
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True

        
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            self.win.blit(GLOW, (col * SQUARE_SIZE - 88, row * SQUARE_SIZE + 65))
            # pygame.draw.circle(self.win, GREY, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == PLAYERS[1]:
            self.turn = PLAYERS[0]
        else:
            self.turn = PLAYERS[1]