"""
Cette class est destinée à l'importation et à la gestion de la musique.
Date de réalisation : 09/12/2023
Réaliser par Nathan FRUME.
TO DO : rien
"""
import pygame
class Musique:
    def __init__(self):
        pygame.mixer.init()
        self.Musique = pygame.mixer.Sound("Son/162_extended.mp3")
        self.Musique.play(-1)
    def stopMusique(self):
        self.Musique.stop()