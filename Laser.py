# [CLASS Laser] et [CLASS LaserFort]
"""
Cette class est destinée aux lasers normaux que tirent les ennemis. (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 16/11/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
TO DO : rien
"""
class Laser:
    """
    Cette class est destinée aux lasers normaux que tirent les ennemis.
    Elle prend en charge la position du laser(definie par position1 et position2).
    """
    def __init__(self, position1, position2):
        """
        Cette méthode initialise la position du laser.
        La position est définie par position1 et position2 qui sont des listes(de taille 2).
        - position1 = (x1,y1) (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = (x2,y2) (ici (x2,y2) est le point en bas à droite de l'image)
        """
        self.position1 = position1
        self.position2 = position2
    def changementPosition(self,valeurAAjouter): # valeurAAjouter = ( valeurAAjouterX, valeurAAjouterY )
        """
        Cette méthode actualise la position du laser.
        Entrées : self c'est à dire (position1 et position2) et valeurAAjouter = [valeurAAjouterX, valeurAAjouterY] avec valeurAAjouterX et valeurAAjouterY des int.
        """
        self.position1[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x1
        self.position2[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x2
        self.position1[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y1
        self.position2[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y2

class LaserFort(Laser):
    """
    Cette class est destinée aux supers lasers (les lasers trop forts) que tirent les ennemis.
    Elle prend en charge la position du laser(definie par position1 et position2).
    """
    def __init__(self, position1, position2):
        super().__init__(position1, position2) # NATHAN FAUDRA QUE TU M'EXPLIQUES LE SUPER à QUOI CA SERT stp ?
        