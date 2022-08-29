import pygame
import random
import startpage.button
from pygame.locals import *
from pygame import mixer
import os
pygame.font.init()
mixer.init()
#from startpage.startwindow import PLAYERS 
#from main import PLAYERS

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS


# rgb
PINK = (255, 192, 203)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# import common assets
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (37, 43))
BOARD = pygame.transform.scale(pygame.image.load('assets/board.png'), (800, 800))
GLOW = pygame.transform.scale(pygame.image.load('assets/yellow_glow.png'), (270, 60))

#*********************START UP PAGES CONSTANTS ************************

STARTPAGE_BK = pygame.image.load("images/startbackgound.png")
PLAYERPAGE_BK = pygame.image.load("images/playerBackGroung.png")
ORANGE_KILLP = pygame.image.load("images/orange_kill_pink.png")
CYAN_KILLW = pygame.image.load("images/cyan_kill_white.png")
CYAN_KILLO = pygame.image.load("images/cyan_kill_orange.png")
ORANGE_KILLC = pygame.image.load("images/orange_kill_cyan.png")
PINK_KILLW = pygame.image.load("images/pink_kill_white.png")
WHITE_KILLC = pygame.image.load("images/white_kill_cyan.png")
WHITE_KILLP = pygame.image.load("images/white_kill_pink.png")
PINK_KILLO = pygame.image.load("images/pink_kill_orange.png")
VICTORY = pygame.image.load("images/victory.jpeg")
DEFEAT =  pygame.image.load("images/defeat.jpeg")


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
STARTPAGE_BK_rect = STARTPAGE_BK.get_rect(topleft = (0,0))  

ORANGE_KILLP_rect = ORANGE_KILLP.get_rect(topleft = (0,0))
CYAN_KILLW_rect = CYAN_KILLW.get_rect(topleft = (0,0))
CYAN_KILLO_rect = CYAN_KILLO.get_rect(topleft = (0,0))
ORANGE_KILLC_rect = ORANGE_KILLC.get_rect(topleft = (0,0))
PINK_KILLW_rect = PINK_KILLW.get_rect(topleft = (0,0))
WHITE_KILLC_rect = WHITE_KILLC.get_rect(topleft = (0,0))
WHITE_KILLP_rect = WHITE_KILLP.get_rect(topleft = (0,0))
PINK_KILLO_rect = PINK_KILLO.get_rect(topleft = (0,0))
VICTORY_rect = VICTORY.get_rect(topleft = (0,0))
DEFEAT_rect = DEFEAT.get_rect(topleft = (0,0))


#define fonts
font = pygame.font.Font('font/ShortBaby-Mg2w.ttf', 40) #number is font size
page_font = pygame.font.Font('font/ShortBaby-Mg2w.ttf', 180)

#load button images
SELECPLAYER_IMG = pygame.image.load("images/selectplayersbtn.png").convert_alpha()
LEVELS_IMG = pygame.image.load("images/levelsbtn.png").convert_alpha()
PLAY_IMG = pygame.image.load("images/playbtn.png").convert_alpha()
QUIT_IMG = pygame.image.load("images/quitbtn.png").convert_alpha()
ORANGE_IMG = pygame.image.load("images/orangeplayer.png").convert_alpha()
BLUE_IMG = pygame.image.load("images/blueplayer.png").convert_alpha()
WHITE_IMG = pygame.image.load("images/whiteplayer.png").convert_alpha()
PINK_IMG = pygame.image.load("images/pinkplayer.png").convert_alpha()
MAINMENU_IMG = pygame.image.load("images/mainmenu.png").convert_alpha()
QUIT_BTN_IMG = pygame.image.load("images/quitbtn.png").convert_alpha()

#create button instances
SELECPLAYER_BTN = startpage.button.Button(350, 350, SELECPLAYER_IMG, 1)
LEVELS_BTN = startpage.button.Button(350, 450, LEVELS_IMG, 1)
PLAY_BTN = startpage.button.Button(350, 550, PLAY_IMG, 1)
QUITE_BTN = startpage.button.Button(350, 650, QUIT_IMG, 1)

ORANGE_BTN = startpage.button.Button(80, 400, ORANGE_IMG, 1)
BLUE_BTN = startpage.button.Button(255, 400, BLUE_IMG, 1)
WHITE_BTN = startpage.button.Button(430, 400, WHITE_IMG, 1)
PINK_BTN = startpage.button.Button(605, 400, PINK_IMG, 1)
MAINMENU_BTN = startpage.button.Button(400, 650, MAINMENU_IMG, 1)
QUIT_BTN = startpage.button.Button(200, 650, QUIT_BTN_IMG, 1)


# Set Piece Graphics ==========================
ORANGE_PLAYER = pygame.transform.scale(pygame.image.load('assets/orangeplayer_ingame.png'), (64, 85))
PINK_PLAYER = pygame.transform.scale(pygame.image.load('assets/pinkplayer_ingame.png'), (64, 85))
BLUE_PLAYER = pygame.transform.scale(pygame.image.load('assets/blueplayer_ingame.png'), (64, 85))
WHITE_PLAYER = pygame.transform.scale(pygame.image.load('assets/whiteplayer_ingame.png'), (64, 85))

PLAYERS = []

#Music
# music1 = pygame.mixer.music.load('music/alien_kill.ogg')
# music2 = pygame.mixer.music.load('music/gun_kill.ogg')
# music3 = pygame.mixer.music.load('music/knife_kill.ogg')
# music4 = pygame.mixer.music.load('music/neck_kill.ogg')
# GAMEOVER_SOUND = pygame.mixer.music.load('music/game_over_music.ogg')

MUSIC = "/Users/dachanelle/Desktop/CHECKERS-AMONG-US/music"
# all_mp3 = [os.path.join(MUSIC, f) for f in os.listdir(MUSIC) if f.endswith('.mp3')]
# RANDOM = random.choice(all_mp3)

# MUSIC = pygame.mixer.music.Sound('music/neck_kill.ogg')