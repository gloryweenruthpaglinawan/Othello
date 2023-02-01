import pygame, sys
from button import Button
import Othello_AI
import Othello_AI_Pruning
import Othello_PVP
import menu_button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 680))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Othello.jpg")

image = pygame.image.load("assets/p1 vs ai.png").convert_alpha()
PLAY_BUTTON = menu_button.Button(0, 0, image, 0.8)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def othello_AI():
    while True:
        SCREEN.fill("black")
        Othello_AI.main()
    
def othello_AI_Pruning():
    while True:
        SCREEN.fill("black")
        Othello_AI_Pruning.main()

def othello_PVP():
    while True:
        SCREEN.fill("black")
        Othello_PVP.main()



while True:
    
        SCREEN.blit(BG, (0, 0))

        #PLAY_BUTTON.draw(SCREEN)

        if PLAY_BUTTON.draw(SCREEN):
           othello_AI_Pruning()

        pygame.display.update()  


        