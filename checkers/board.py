# from pygame import mixer
import random
from .constants import *
from .piece import Piece
from pygame import mixer
from checkers.winnersPage import winning_menu




class Board:
    def __init__(self):
        self.board = []
        self.pink_left = self.blue_left = 12
        self.pink_kings = self.blue_kings = 0
        self.create_board()
    
    #manage color of board
    def draw_squares(self, win):
        win.blit(BOARD, (0,0))
        # win.fill(BLACK)
        # for row in range(ROWS):
        #     for col in range(row % 2, COLS, 2):
        #         pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #movement of pieces
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.image == PLAYERS[0]:
                self.blue_kings += 1
            else:
                self.pink_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, PLAYERS[0]))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, PLAYERS[1]))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                 
   
   #draw piece and pieces
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.image == PLAYERS[1] :
                    self.pink_left -= 1
                    # pygame.mixer.music.load(RANDOM)
                    pygame.mixer.music.load('music/neck_kill.ogg')
                    pygame.mixer.music.play(1)
                else:
                    self.blue_left -= 1
                    # pygame.mixer.music.load(RANDOM)
                    pygame.mixer.music.load('music/neck_kill.ogg')
                    pygame.mixer.music.play(1)
                  

    def winner(self, game):
        # winning_menu(game)
        if self.pink_left <= 0 or self.blue_left == 0:
            winning_menu(game)

        return None
    
    #check all possible moves available for a selected piece
    def get_valid_moves(self, piece):
        moves = {} #store the moved as the key  = to any piece that we skip to get to that move
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        #check if piece can be moved up or down base on the color or if king piece
        if piece.image == PLAYERS[1] or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.image, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.image, right))
        if piece.image == PLAYERS[0] or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.image, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.image, right))

        return moves
    
    #check left diagonal of board for valid position to move piece to 
    def _traverse_left(self, start, stop, step, image, left, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, image, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, image, left+1, skipped=last))
                break
            elif current.image == image:
                break
            else: 
                last = [current]

            left -= 1

        return moves

#check right diagonal of board for valid position to move piece to 
    def _traverse_right(self, start, stop, step, image, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, image, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, image, right+1, skipped=last))
                break
            elif current.image == image:
                break
            else: 
                last = [current]

            right += 1

        return moves
    

# Gets the image of the winner
    def get_winner_image(self,p1,p2):
        if self.blue_left <= 0:
            if p1 == ORANGE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(CYAN_KILLO, (CYAN_KILLO_rect))
            if p1 == BLUE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(WHITE_KILLC, (WHITE_KILLC_rect))
            if p1 == WHITE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(PINK_KILLW, (PINK_KILLW_rect))
            if p1 == PINK_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(ORANGE_KILLP, (ORANGE_KILLP_rect))
        elif self.pink_left <= 0:
            if p2 == ORANGE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(PINK_KILLO, (PINK_KILLO_rect))
            if p2 == BLUE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(ORANGE_KILLC, (ORANGE_KILLC_rect))
            if p2 == WHITE_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(CYAN_KILLW, (CYAN_KILLW_rect))
            if p2 == PINK_PLAYER:
                SCREEN.fill(BLACK)
                SCREEN.blit(WHITE_KILLP, (WHITE_KILLP_rect))
        
        return 
            

        