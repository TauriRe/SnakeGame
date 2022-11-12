import random

import pygame

# Main THEMES


#SONGS
'''songs = ['music.mp3']
song_finished = pygame.USEREVENT + 1'''
pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(0)
pygame.mixer.music.play(loops=-1)



pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/music.mp3'), maxtime=600)

'''def back_sound():
    clock = pygame.time.Clock()
    song_idx  = 0 #The index of current song
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == song_finished:
                pygame.mixer.music.load(random.choice(songs))
                pygame.mixer.music.play(0)
                
'''