"""
Cette class est destinée au train (en haut). (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 09/12/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
TO DO : rien
"""

class Train:
    """
    Cette class est destinée au train (en haut).
    Elle prend en charge la position du train(definie par position1 et position2).
    """
    def __init__(self,position):
        """
        Cette méthode initialise la position du train.
        La position est définie par position1 et position2 qui sont des listes(de taille 2).
        - position1 = [x1,y1] (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = [x2,y2] (ici (x2,y2) est le point en bas à droite de l'image)
        """
        self.positionX = position[0]
        self.positionY = position[1]
        
    def changementPosition(self,valeurAAjouter): # valeurAAjouter = ( valeurAAjouterX, valeurAAjouterY )
        """
        Cette méthode actualise la position du train.
        Entrées : self c'est à dire (position1 et position2) et valeurAAjouter = [valeurAAjouterX, valeurAAjouterY] avec valeurAAjouterX et valeurAAjouterY des int.
        """
        self.positionX += valeurAAjouter[0] #x
        self.positionY += valeurAAjouter[1] #y
