import pygame
pygame.init()

#Font
small_font = pygame.font.SysFont("comic sans ms", 25, True)
medium_font = pygame.font.SysFont('comic sans ms', 30, True)
large_font = pygame.font.SysFont('comic sans ms', 60, True)
clock = pygame.time.Clock()  # kell

#Pildid
snake_img=pygame.image.load("img/snake2.png")
tail_img=pygame.image.load("img/tail1.png")
apple_img=pygame.image.load("img/apple2.png")
start_bg=pygame.image.load("img/snake_game_background.jpg")

# Colors (R, G, B) ja suurused

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (250, 253, 15)
lyellow = (173, 255, 47)
fgreen = (34, 139, 34)

APPLE_SIZE = 20
TOP_WIDTH = 40
