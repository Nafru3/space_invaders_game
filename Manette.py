"""
Cette classe permet de gérer le fait qu'on puisse jouer à la manette. (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 18/11/2023
Réaliser par Nathan FRUME.
TO DO : rien
"""
# Importation (Car on a besoin de Pygame pour jouer à la manette)
import pygame
class Manette:
    """
    Cette classe permet de gérer le fait qu'on puisse jouer à la manette
    Elle prend en entrée la référence à la classe Game (Notament pour appeler les méthodes de déplacements)
    """
    def __init__(self,Game): #pygame.joystick.Joystick(0) correspond à la manette qui est branchée
        self.Game = Game
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0 : #S'il y au moins une manette branchée
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            
    def Entree(self):
        """
        Cette méthode permet de vérifier quels sont les touches appuyées sur la manette
        Si c'est le bouton A => Appel de la méthode dans Game pour tirer
        Si c'est le Joystick => Appel des méthodes dans Game pour se déplacer
        """
        pygame.joystick.init()
        self.joystick.init()
        if  pygame.joystick.get_count() > 0:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN: # On vérifie si le bouton A est appuyé
                    if self.joystick.get_button(0):
                        self.Game.tirJoueur(self.Game)
            if self.joystick.get_axis(0)<-0.1: #On vérifie si le joystick est incliné vers la gauche
                self.Game.gauche(self.Game)
            if self.joystick.get_axis(0)>0.1: #On vérifie si le joystick est incliné vers la droite
                self.Game.droite(self.Game)
                
    def VerifManetteBranchee(self):
        """
        Cette méthode renvoie True si une manette est branchée. False sinon
        """
        return pygame.joystick.get_count() == 1
