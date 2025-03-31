# [CLASS Bouclier]
"""
Cette class est destinée aux boucliers (devant le héro). (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 18/11/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
TO DO : rien
"""
class Bouclier:
    """
    Cette class est destinée aux boucliers (devant le héro).
    Elle prend en charge la position du bouclier (definie par position1 et position2).
    """
    def __init__(self,position1,position2):
        """
        Cette méthode initialise la position du bouclier.
        La position est définie par position1 et position2 qui sont des listes(de taille 2).
        - position1 = (x1,y1) (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = (x2,y2) (ici (x2,y2) est le point en bas à droite de l'image)
        """
        self.position1 = position1
        self.position2 = position2