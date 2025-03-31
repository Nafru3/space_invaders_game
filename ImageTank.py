"""
Cette classe permet d'avoir accès à toutes les images.
Date de réalisation : 09/12/2023
Réaliser par Nathan FRUME.
TO DO : rien
"""
# Importation de PIL pour avoir accès aux images
from PIL import ImageTk,Image
class ImageTank:
    """
    Cette classe permet d'avoir accès à toutes les images.
    """
    def __init__(self):
        """
        Cette méthode est décomposée est 3 parties :
        - Importation des images (qui sont toutes aux formats png)
        - Redimensionnement des images
        - Convertion des images pour qu'elles puissent être affiché par Tkinter
        """
        #On importe les images
        fond = Image.open("Image/ecran_vide.png")
        mur = Image.open("Image/mur.png")
        balle = Image.open("Image/balle.png")
        balle_mechante = Image.open("Image/balle_mechante.png")
        balle_mechante = balle_mechante.rotate(180)
        superballe = Image.open("Image/superballe.png")
        superballe_mechante=Image.open("Image/superballe_mechante.png")
        tank = Image.open("Image/tank.png")
        tank_mechant = Image.open("Image/tank_mechant.png")
        tank_mechant_super = Image.open("Image/tank_mechant_super.png")
        tank_mechant_super_amoche = Image.open("Image/tank_mechant_super_amoche_v2.png")
        gameover=Image.open("Image/ecran_game_over.png")
        ecran_debut=Image.open("Image/ecran_debut.png")
        explo_1 = Image.open("Image/explo_1.png")
        explo_2 = Image.open("Image/explo_2.png")
        explo_3 = Image.open("Image/explo_3.png")
        explo_4 = Image.open("Image/explo_4.png")
        fum_1 = Image.open("Image/fum_1.png")
        fum_2 = Image.open("Image/fum_2.png")
        fum_3 = Image.open("Image/fum_3.png")
        fum_4 = Image.open("Image/fum_3.png")
        fumee_anim_1 = Image.open("Image/fumee_anim_1.png")
        fumee_anim_2 = Image.open("Image/fumee_anim_2.png")
        fumee_anim_3 = Image.open("Image/fumee_anim_3.png")
        fumee_anim_4 = Image.open("Image/fumee_anim_4.png")
        fumee_anim_5 = Image.open("Image/fumee_anim_5.png")
        train = Image.open("Image/train.png")
        balle_grande = Image.open("Image/balle_grande.png")
        superballe_grande = Image.open("Image/superballe_grande.png")
       

        #On redimensionne les images
        fond=fond.resize((600,500))
        mur=mur.resize((25,25))
        balle = balle.resize((5,30))
        balle_mechante = balle_mechante.resize((5,25))
        superballe = superballe.resize((10,40))
        superballe_mechante = superballe_mechante.rotate(180)
        superballe_mechante = superballe_mechante.resize((10,40))
        tank =tank.resize((30,45))
        tank_mechant = tank_mechant.resize((30,45))
        tank_mechant_super = tank_mechant_super.resize((30,45))
        tank_mechant_super_amoche = tank_mechant_super_amoche.resize((30,45))
        gameover = gameover.resize((600,500))
        ecran_debut = ecran_debut.resize((600,500))
        explo_1=explo_1.resize((80,80))
        explo_2=explo_2.resize((80,80))
        explo_3=explo_3.resize((80,80))
        explo_4=explo_4.resize((90,90))
        fum_1=fum_1.resize((40,40))
        fum_2=fum_2.resize((40,40))
        fum_3=fum_3.resize((40,40))
        fum_4=fum_4.resize((40,40))
        fumee_anim_1 = fumee_anim_1.resize((30,30))
        fumee_anim_2 = fumee_anim_2.resize((30,30))
        fumee_anim_3 = fumee_anim_3.resize((30,30))
        fumee_anim_4 = fumee_anim_4.resize((30,30))
        fumee_anim_5 = fumee_anim_5.resize((30,30))
        train = train.resize((150,35))
        balle_grande = balle_grande.resize((10,30))
        superballe_grande = superballe_grande.resize((10,45))

        
        #On convertit les images pour qu'elles soient compatibles avec TKinter
        self.fond = ImageTk.PhotoImage(fond)
        self.mur= ImageTk.PhotoImage(mur)
        self.balle = ImageTk.PhotoImage(balle)
        self.balle_mechante = ImageTk.PhotoImage(balle_mechante)
        self.superballe = ImageTk.PhotoImage(superballe)
        self.superballe_mechante = ImageTk.PhotoImage(superballe_mechante)
        self.tank = ImageTk.PhotoImage(tank)
        self.tank_mechant = ImageTk.PhotoImage(tank_mechant)
        self.tank_mechant_super = ImageTk.PhotoImage(tank_mechant_super)
        self.tank_mechant_super_amoche = ImageTk.PhotoImage(tank_mechant_super_amoche)
        self.gameover = ImageTk.PhotoImage(gameover)
        self.ecran_debut=ImageTk.PhotoImage(ecran_debut)
        self.explo_1 = ImageTk.PhotoImage(explo_1)
        self.explo_2 = ImageTk.PhotoImage(explo_2)
        self.explo_3 = ImageTk.PhotoImage(explo_3)
        self.explo_4 = ImageTk.PhotoImage(explo_4)
        self.fum_1 = ImageTk.PhotoImage(fum_1)
        self.fum_2 = ImageTk.PhotoImage(fum_2)
        self.fum_3 = ImageTk.PhotoImage(fum_3)
        self.fum_4 = ImageTk.PhotoImage(fum_4)
        self.fumee_anim_1 = ImageTk.PhotoImage(fumee_anim_1)
        self.fumee_anim_2 = ImageTk.PhotoImage(fumee_anim_2)
        self.fumee_anim_3 = ImageTk.PhotoImage(fumee_anim_3)
        self.fumee_anim_4 = ImageTk.PhotoImage(fumee_anim_4)
        self.fumee_anim_5 = ImageTk.PhotoImage(fumee_anim_5)
        self.train = ImageTk.PhotoImage(train)
        self.balle_grande = ImageTk.PhotoImage(balle_grande)
        self.superballe_grande = ImageTk.PhotoImage(superballe_grande)

        