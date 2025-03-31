# [CLASS Clavier]
"""
Cette class est destinée aux entrées claviers du gamer. (Pour plus de détails, cf commentaire entre le nom de la class et le __init__)
Date de réalisation : 18/11/2023
Réaliser par Nathan FRUME.
TO DO : rien
"""
class Clavier:
    """
    Cette class est destinée aux entrées claviers du gamer.
    Elle permet de prendre en désactiver les touches du clavier.
    Elle prend en charge : la fenetre Tkinter("fenetre"), la class Game.
    """
    def __init__(self,fenetre,Game):
        """
        Cette méthode initialise :
        - fenetre (c'est la fenetre Tkinter)
        - et lie les touches : gauche, droite et espace. ==> ici l'utilisateur peut jouer au clavier.
        """
        # Pour le déplacement du héro
        self.fenetre = fenetre
        self.fenetre.bind('<Left>',Game.gauche)
        self.fenetre.bind('<Right>',Game.droite)
        # Pour les tirs du héro
        self.fenetre.bind('<space>',Game.tirJoueur)
    def Unbind(self):
        """
        Cette méthode permet : 
        de "détacher" les touches :  gauche, droite et espace. ==> ici l'utilisateur ne peut pas jouer au clavier.
        (Nous l'utilisons pour que le joueur joue à la manette, sans appuyer sur le clavier simultanément)
        """
        # Pour le déplacement du héro
        self.fenetre.unbind('<Left>')
        self.fenetre.unbind('<Right>')
        # Pour les tirs du héro
        self.fenetre.unbind('<space>')