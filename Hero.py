# [CLASS HERO]
"""
Cette class est destinée au joueur (tank en bas de l'écran). (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 16/11/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
TO DO : rien
"""
class Hero:
    """
    Cette class est destinée au joueur (tank en bas de l'écran).
    Elle prend en charge la position du joueur, son score, ses munitions, et la vie du joueur.
    """
    def __init__(self, position1, position2, score,munition,vie): 
        """
        Cette méthode initialise : 
        - position1 = (x1,y1) (ici (x1,y1) est le point en haut à gauche de l'image) avec x1,y1,x2,y2 des entiers
        - position2 = (x2,y2) (ici (x2,y2) est le point en bas à droite de l'image)
        - score : c'est le score du joueur. ==> int
        - munition #Munition : [1ere,2eme...,5eme]
        - vie : du joueur ==> list. 
        """
        self.vie = vie # C'est la pile
        self.position1 = position1
        self.position2 = position2
        self.score = score
        self.munition = munition
    
    def changementPosition(self,valeurAAjouter):
        """
        Cette méthode actualise la position du joueur.
        Entrées : self c'est à dire (position1 et position2) et valeurAAjouter = [valeurAAjouterX, valeurAAjouterY] avec valeurAAjouterX et valeurAAjouterY des int.
        """
        self.position1[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x1
        self.position2[0] += valeurAAjouter[0] # on ajoute la valeurAAjouter sur x2
        self.position1[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y1
        self.position2[1] += valeurAAjouter[1] # on ajoute la valeurAAjouter sur y2

    def changementScore(self,scoreAAjouter) : # gestion du score
        """
        Cette méthode ajoute le score à ajouter ("scoreAAjouter") au score actuel. (on actualise le score)
        Entrées : self c'est à dire (score ==> int) et le scoreAAjouter ==> int
        """
        self.score += scoreAAjouter 

    def changementVie(self,vieAAjouter): #Gestion de la vie : vieAAjouter est soit à -1, soit à 1
        """
        Cette méthode permet d'ajouter une vie ou de retirer une vie au Héro. On gére la vie sous la forme d'une file.
        Entrée : vie (==> int), vieAAjouter prend la valeur -1 si l'on veut supprimer une vie et 1 si l'on veut ajouter une vie.
        """
        if vieAAjouter == -1:
            self.vie.pop(-1)
        else :
            self.vie.append(1)

    def gestionTir(self):
        """
        Cette méthode permet de gérer les munitions comme une file, on enlève le premier élément de la liste puis on le rajoute à la fin.
        (On  l'utilise dans la class game pour faire défiler les munitions de la liste qui contient les munitions du héro.
        Entrée : self c'est à dire "munition"
        """
        first = self.munition[0]
        self.munition.pop(0)
        self.munition.append(first)
        return first == 0 #Retourne True si balle normale, return False si balle trop forte

