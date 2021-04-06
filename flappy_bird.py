import random
import pygame
import sys #sys.exit
from pygame.locals import *

FPS=60
SCREEN_WIDTH=289
SCREEN_HEIGHT=511
SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GROUNDY=SCREEN_HEIGHT*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='gallery/sprites/bird.png'
BACKGROUND='gallery/sprites/background.png'
PIPE='gallery/sprites/pipe.png'


def welcomeScreen():
    playerx=int(SCREEN_WIDTH/5)
    playery=int((SCREEN_HEIGHT-GAME_SPRITES['player'].get_height())/2)
    messagex=int((SCREEN_WIDTH-GAME_SPRITES['message'].get_height())/2)
    messagey=int(SCREEN_HEIGHT*0.13)
    basex=0 
    while True:
        for event in pygame.event.get():
            #to close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(basex,GROUNDY))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)



if __name__ == "__main__":
    pygame.init()
    FPS_CLOCK=pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird By Apurv')
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'](
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )
    #game sounds
    GAME_SOUNDS['die']=pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing']=pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']=pygame.image.load(player).convert_alpha()
    while True:
        welcomeScreen()
        mainGame()