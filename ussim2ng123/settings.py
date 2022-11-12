import pygame

# Window size
frame_size_x = 720
frame_size_y = 480
# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
canvas = pygame.display.set_mode(((frame_size_x, frame_size_y)))

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()
FPS = pygame.time.Clock()

VELOCITY = 4

