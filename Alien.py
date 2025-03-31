# [CLASS Alien]
"""
Cette class est destinée aux tanks ennemis "normaux". (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 11/11/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
TO DO : rien
"""
class Alien:
    """
    Cette class est destinée aux tanks ennemis "normaux".
    Elle prend en charge : le déplacement (on utilise le pas (pour aller à droite ou à gauche)) la position des tanks ennemis.
    """
    def __init__(self,pas, position1, position2):  # position1 = (positionX1,positionY1) et position2 = (positionX2, positionY2)
        """
        Cette méthode initialise : 
        - le pas : float de combien l'alien va se déplacer
        - position1 = (x1,y1) (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = (x2,y2) (ici (x2,y2) est le point en bas à droite de l'image)
        """
        self.pas = pas
        self.position1 = position1
        self.position2 = position2
    
    def deplacement(self,right):
        """
        Méthode qui renvoie un pas positif si l'alien va à droite et un pas negatif s'il va à gauche
        Entrée : right : True si l'alien va à gauche, False sinon
        """
        if right :
            return self.pas 
        return -self.pas
    
    def changementPosition(self,valeurAAjouter):
        """
        Cette méthode actualise la position des tanks ennemis.
        Entrées : self c'est à dire (position1 et position2) et valeurAAjouter = [valeurAAjouterX, valeurAAjouterY] avec valeurAAjouterX et valeurAAjouterY des int.
        """
        self.position1[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x1
        self.position2[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x2
        self.position1[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y1
        self.position2[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y2

class AlienFort(Alien):
    """
    Cette class est destinée aux tanks forts ennemis .
    Elle prend en charge : les mêmes paramètres que la classe Alien
    La classe AlienFort possède la variable vie contrairement à la classe Alien
    """
    def __init__(self, pas, position1, position2,vie):
        """
        Cette méthode permet d'initialiser la classe
        - le pas : float de combien l'alien va se déplacer
        - position1 = (x1,y1) (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = (x2,y2) (ici (x2,y2) est le point en bas à droite de l'image)
        - vie : La vie de l'alien
        """
        super().__init__(pas, position1, position2)
        self.vie = vie
        
    def death(self):
        """
        Cette méthode renvoie False si alien n'a plus de vie et renvoie True + retire une vie s'il lui rete encore des vies
        """
        if self.vie != 0:
            self.vie -= 1
        return self.vie != 0 