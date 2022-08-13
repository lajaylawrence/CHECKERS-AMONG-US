import pygame
import startpage.button  
pygame.font.init()

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
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
STARTPAGE_BK_rect = STARTPAGE_BK.get_rect(topleft = (0,0))  

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


#create button instances
SELECPLAYER_BTN = startpage.button.Button(350, 350, SELECPLAYER_IMG, 1)
LEVELS_BTN = startpage.button.Button(350, 450, LEVELS_IMG, 1)
PLAY_BTN = startpage.button.Button(350, 550, PLAY_IMG, 1)
QUITE_BTN = startpage.button.Button(350, 650, QUIT_IMG, 1)
ORANGE_BTN = startpage.button.Button(100, 400, ORANGE_IMG, 1)
BLUE_BTN = startpage.button.Button(350, 400, BLUE_IMG, 1)
WHITE_BTN = startpage.button.Button(600, 400, WHITE_IMG, 1)

# Set Piece Graphics ==========================
ORANGE_PLAYER = pygame.transform.scale(pygame.image.load('assets/orangeplayer_ingame.png'), (64, 85))
PINK_PLAYER = pygame.transform.scale(pygame.image.load('assets/pinkplayer_ingame.png'), (64, 85))


