import pygame


class Balle:
    def __init__(self, position_x, position_y, vitesse_x, vitesse_y, couleur, taille):
        self.position_x = position_x
        self.position_y = position_y
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
        self.couleur = couleur
        self.taille = taille

    def avance(self, t, ww, wh):
        self.position_x = int(self.vitesse_x * t) % ww
        self.position_y = int(self.vitesse_y * t) % wh

    def dessine(self, s):
        pygame.draw.circle(s, self.couleur, (self.position_x, self.position_y), self.taille)

    def contient(self, position):
        px, py = position
        distance_carree = (px - self.position_x)**2 + (py - self.position_y)**2
        return distance_carree <= self.taille**2
    

