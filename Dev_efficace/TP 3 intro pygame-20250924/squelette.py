#! /usr/bin/env python3

import pygame
import sys
from balle import *

global FPSCLOCK
FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
ARRIERE_PLAN = (42,17,51)




class Quitte(Exception ):
    pass

def isQuitEvent(event):
    return (event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE))

def handleKey(event):
    print("appui sur la touche", event.key)

def handleClick(event):
    global score, b1
    if b1.contient(event.pos):
        score += 1
    print("Clic à la position", event.pos)

def handleEvents():
    for event in pygame.event.get():
        # pour chaque évènement depuis le dernier appel de cette fonction
        if isQuitEvent(event):
            raise Quitte
        elif event.type == pygame.KEYDOWN:
            handleKey(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handleClick(event)

def refresh(s):
    s.fill(ARRIERE_PLAN)

temps_total = 0
b1 = Balle(200, 100, 0.1, 0.15, (255, 0, 255), 30)  # Création de la balle avec vitesse réduite
score = 0


def affichage(s, t, font):
    """
    Redessine l'écran. 't' est le temps écoulé depuis l'image précédente.
    """
    global temps_total, b1, score
    temps_total += t
    x = int(0.09*temps_total) % WINDOWWIDTH
    y = int(0.15*temps_total) % WINDOWHEIGHT
    b1.avance(temps_total, WINDOWWIDTH, WINDOWHEIGHT)
    refresh(s)

    # pygame.draw.circle(la fenetre, la couleur de la balle, position de la balle, la taille de la balle)
    pygame.draw.circle(s, (255,255,255), (x,y), 150)
    b1.dessine(s)
   
    
    message = "Allons chercher la baballe"
    message = font.render(message, 1, (255,255,255))
    score_render = str(score)
    score_render = font.render(score_render, 1, (255,255,255))
    s.blit(message, (0,0))
    s.blit(score_render, (0,30))


def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Baballe 4.0')
    ecran = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    font = pygame.font.Font(pygame.font.match_font('comicsans'),30)
    refresh(ecran)

    while True:  #boucle principale
        try:
            handleEvents()
            pygame.display.update()
            temps_ecoule = FPSCLOCK.tick(FPS)
            affichage(ecran, temps_ecoule, font)
        except Quitte:
            break

            
    pygame.quit()
    sys.exit(0)

main()
