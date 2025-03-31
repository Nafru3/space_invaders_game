# [VUE --> affichage tkinter]
"""
Ce programme est une class : Jeu
La class "Jeu" est un mélange entre le vue et le controlleur.
Car Tkinter utilise les 2 pour fonctionner.
Les différentes méthode de cette classe : 
-  __init__(self)
- ManetteMet(self)
- ClavierMet(self)
- DebutJeu(self)
- Recommencer(self)
- destructionbouclier(self)
- mouvementAlien(self,laserCanvas,laserClass)
- gauche(self,event)
- droite(self,event)
- tirJoueur(self,event)
- tirAlien(self)
- mouvementTirAlien(self,laserCanvas,laserClass)
-  mouvementTir(self,i)
- GestionExplosion(self,positionX,positionY,explosion,i,listeTankFortTouche)
- Animation(self,temps,listeanimation,imageanimation)
- train(self)
- ScoreAZero(self)
- MeilleurScore(self, score)
- majBarreDeVie(self, value)
- FinDePartie(self,win)
"""
"""
Date de réalisation : 09/11/2023
Réaliser par Raphaël BERGER et Nathan FRUME.
To do : Tout est fini ! (on aurait pu rajouter une augmentation de la vitesse des ennemis, ainsi que l'ajout de pseudo pour les meilleurs scores)
""" 
# --- Importation ---
from tkinter import ttk,Tk,Menu,Canvas,Button,Label,StringVar,Entry
from Alien import Alien,AlienFort
from Hero import Hero
from Bouclier import Bouclier
from Clavier import Clavier
from Laser import Laser,LaserFort
from Manette import Manette
from random import randint
from ImageTank import ImageTank
from Train import Train
from Musique import Musique

class Jeu:
    def __init__(self):
        """
        Cette méthode permet de :
        - Créer la fenêtre Tkinter 
        - appeler la méthode Recommencer
        Entrée : self
        """
        self.fenetre = Tk()
        self.Recommencer()
        
    def ManetteMet(self):
        """ 
        Cette méthode permet de : 
        - Passer en mode : On ne joue qu'à la manette
        Entrée : self
            Pour accéder à :
                self.manetteBranchee : True si une manette est branchée, False sinon
                self.manetteClass : Class de Manette() qui permet de jouer à la manette
                self.clavierClass : Class de Clavier() qui permet de jouer au clavier
        """
        self.manetteBranchee = True
        try: #Si la manette n'existe pas, on la crée
            self.manetteClass 
        except AttributeError:
            self.manetteClass = Manette(self)
        try:
            self.clavierClass.Unbind()
            del self.clavierClass
        except AttributeError:
            None
        
    def ClavierMet(self):
        """
        Cette méthode permet :
        - Passer en mode : On ne joue qu'au clavier
        - S'il y a une manette brachée, on appelle la méthode Manette()
        Entrée : self
            Pour accéder à :
                self.manetteBranchee : True si une manette est branchée, False sinon
                self.manetteClass : Class de Manette() qui permet de jouer à la manette
                self.clavierClass : Class de Clavier() qui permet de jouer au clavier
        """
        self.manetteBranchee = False
        try:
            self.clavierClass
        except AttributeError:
            self.clavierClass = Clavier(self.fenetre,self)
        self.manetteClass = Manette(self)
        if self.manetteClass.VerifManetteBranchee():
            del self.manetteClass
            self.ManetteMet()

    def Recommencer(self):
        """
        Cette méthode permet :
        - de lancer la fenêtre avec l'écran titre du jeu
        - Servir aussi de fonction quand on clique sur recommencer donc elle réinitialise toutes les variables, arrête tous les After et enleve tous les textes
        - Initialiser les variables dont on va avoir besoin tous au long du jeu (exemple : score, munitions etc)
        - Afficher le menu en haut à gauche de l'écran
        - Créer le bouton et le canvas
        - Gerer le reste de la fenetre (titre,taille etc)
        Entrée : self
            Pour accéder à :
                self.___texte : Reference du texte placé sur l'écran
                self.fenetre : Fenetre principale
                self.Recommencer : Méthode pour recommencer la partie 
                self.ScoreAZero : Méthode pour réinitialiser le meilleur score
                self.CodeTriche : Méthode pour créer une fenetre pour rentrer un code triche
                self.NouvellePartie : Méthode pour lancer la partie
        """
        self.stopAfter()
        # ----------------Enlève tous les textes --------------------
        try:
            self.vagueTexte.destroy()
        except:
            None
        try:
            self.scoreTexte.destroy()
        except:
            None
        try :
            self.Musique.stopMusique()
        except:
            None
        try :
            self.textevieBonus.destroy()
        except:
            None
        try:
            self.canvasMunition.destroy()
        except:
            None
        try:
            self.barreVie.destroy()
        except:
            None
        try:
            self.meilleurScoreTexte.destroy()
        except:
            None
        try:
            self.boutonStart.place_forget()
        except:
            None
        try:
            self.labelVague.destroy()
        except:
            None

        # -------------Initialisations des variables pour le jeu---------------
        self.nbrTir = 3
        self.ajoutTir = 1
        self.vie = [1,1,1] # Notre pile
        try :
            self.vieBonus 
        except:
            self.vieBonus = 0
        self.munition = [0,0,0,0,1] # Notre file (Une idée de Thibaud Daubigney)
        self.score = 0
        self.nbrAlienFort = 3
        self.tempsentredeuxtirs = 4000
        try :
            self.heroClass.score = 0
        except:
            None
        self.invincible = False
        self.traintriche = False
        self.clavierClass = Clavier(self.fenetre,self)
        self.manetteClass = Manette(self)
        self.manetteBranchee = False
        self.verifTir = True
        self.ImageTank = ImageTank() #Importation des images
        self.Musique = Musique() #Importation de la musique


        self.fenetre.quit() #Réinitialisation de la fenetre

        # --------------- Création du Menu --------------------
        menuPrincipal = Menu(self.fenetre)
        menuPrincipal.add_command(label = "Recommencer",command = self.Recommencer)
        menuPrincipal.add_command(label = "Quitter", command = exit)#self.fenetre.destroy)
        menuPrincipal.add_command(label = "Réinitialiser le meilleur score", command = self.ScoreAZero)
        menuPrincipal.add_command(label = "Rentrez un code triche",command = self.CodeTriche)
        self.fenetre.config(menu = menuPrincipal)
        self.fenetre.protocol("WM_DELETE_WINDOW", exit)

        # ------------------ Création du Canvas -------------------

        self.canvas = Canvas(self.fenetre, width = 600, height = 500)
        self.canvas.place(x = 200, y = 100)


        # ------------------ Création du Bouton pour Commencer ----------------
        self.boutonStart = Button(self.fenetre,text="Commencer La Partie",height=1 , width=20,command=self.NouvellePartie)
        self.boutonStart.place(x=450,y=70)

        # ------------------ Création de la fenetre -------------------
        self.fonddebut = self.canvas.create_image(0, 0, image = self.ImageTank.ecran_debut, anchor = "nw")
        self.fenetre.resizable(width = False, height=False)
        self.fenetre.title("Earth Invaders")
        self.fenetre.iconbitmap("Image/logo_balle.ico")
        self.fenetre.geometry("1000x700")
        self.fenetre.mainloop()

    def stopAfter(self):
        """
        Cette méthode permet :
        - Stopper tous les self.canvas.after() du programme pour éviter des problèmes (quand on recommence par exemple)
        Entrée : self
            Pour accéder à :
                self.fenetre : Fenetre principale
                self.After______ : Cela correspond à tous les self.canvas.after() du programme
        """
        try:
            self.fenetre.after_cancel(self.AfterAppelVague)
        except:
            None        
        try : 
            self.fenetre.after_cancel(self.AfterTrain)
        except:
            None
        try:
            self.fenetre.after_cancel(self.AfterDeplacementMunition)
        except:
            None
        try:
            self.fenetre.after_cancel(self.afterMouvementAlien)
        except:
            None
        try:
            self.fenetre.after_cancel(self.afterTirAlien)
        except:
            None
        try:
            self.fenetre.after_cancel(self.afterMouvementTirAlien)
        except:
            None
        try:
            self.fenetre.after_cancel(self.afterMouvementTir)
        except:
            None
        try:
            self.fenetre.after_cancel(self.AfterGestionExplosion)
        except:
            None


    def NouvellePartie(self):
        """
        Cette méthode permet :
            D'enlever les éléments graphiques du menu principal du jeu
            D'afficher tous les éléments graphiques (vie,score etc)
            Appel de la méthode Appelvague() pour lancer le jeu

        Entrée : self
            Pour accéder à :
                self.fenetre : Fenetre principale
                self.Recommencer : Méthode pour recommencer la partie 
                self.ScoreAZero : Méthode pour réinitialiser le meilleur score
                self.majBarreDeVie : Méthode pour actualiser la barre de vie
                self.AppelVague : Méthode pour lancer une vague d'ennemi
                self.vieBonus : Vie en plus que le héro a (les coeurs verts)
                self.convertisseurVieenCoeur : Méthode qui permet de mettre des coeurs à la place du nombre de vie bonus
        """
        # -------------------Suppression éléments page d'avant -------------------
        self.boutonStart.place_forget()
        self.canvas.delete(self.fonddebut)

        # ---------------- Création des labels ------------------
        # Couleur pour les labels : 
        couleur_fond = "#869cae"  # Fond gris foncé
        couleur_texte = "#FDFDFD"  # Texte blanc cassé


        # Affichage de la vie totale
        if self.vieBonus == 0 :
             self.textevieBonus = Label(self.fenetre, text = "", font = ("Arial", 25), fg = "green", anchor='center', justify = 'center')
        else:
            self.textevieBonus = Label(self.fenetre, text = "+ "+ self.convertisseurVieenCoeur(self.vieBonus), font = ("Arial", 25), fg = "green", anchor='center', justify = 'center')
        self.textevieBonus.place(x = 810, y = 60)

        # Affichage du score actuel
        self.scoreTexte = Label(self.fenetre, text = "Score : "+ str(self.score),font = ("Arial", 12), fg = couleur_texte, bg = couleur_fond, anchor = 'center', justify = 'center')
        self.scoreTexte.place(x = 250, y = 70)

        # Affichage du meilleur score
        self.meilleurScoreTexte = Label(self.fenetre, text ="Meilleurs score : " + str(self.MeilleurScore('0')))
        self.meilleurScoreTexte.place(x=75, y=70)

        # -------------------- Création de la barre de vie -----------------------
        self.barreVie = ttk.Progressbar(self.fenetre, orient = 'horizontal', length = 200, mode = 'determinate')
        self.barreVie.place(x = 600, y = 70)

        # On definit une valeur initiale pour la barre de vie
        health_value = 100
        self.majBarreDeVie(health_value)
        
        self.vague = 1 #Numéro de la vague
        self.AppelVague()

    def AppelVague(self):
        """
        Cette méthode permet :
            Gérer graphiquement le début de la vague
            Créer le héro (Visuellement et toutes ses variables)
            Choisir entre Manette ou Clavier
            Gérer l'apparition de l'endroit des munitions
        Entrée : self
            Pour accéder à :
                self.fenetre : Fenetre principale
                self.canvas : Canvas où il y a le jeu
                self.ImageTank : Class qui contient toutes les images
                self.score : Entier qui correspond au score
                self.munition : Liste qui contient les munitions du héro
                self.vie : Liste qui correspond à la vie du héro
                self.manetteBranchee : True si une manette est branchée, False sinon
                self.StartGame : Permet de lancer la partie (Apparition des ennemis etc)
                self.scoreTexte : Texte qui affiche le score du Joueur
        """
        # ----------Partie visuel de l'appel de la vague -------------
        self.fond=self.canvas.create_image(0, 0, image = self.ImageTank.fond,anchor = "nw")
        #Création d'un nouveau menu sans 
        menuJeu = Menu(self.fenetre)
        menuJeu.add_command(label = "Recommencer",command = self.Recommencer)
        menuJeu.add_command(label = "Quitter", command = exit)
        menuJeu.add_command(label = "Réinitialiser le meilleur score", command = self.ScoreAZero)
        self.fenetre.config(menu = menuJeu)
        self.labelVague = self.canvas.create_text(300, 200, text = "VAGUE " + str(self.vague), font = ("Arial", 100,"bold"), fill = 'dark green')
        try: #Ici on enleve le petit texte vie en bas à gauche de l'écran quand on est sur l'écran de changement de vague
            self.vagueTexte.destroy()
        except:
            None

        # ---------------Création du héro---------------
        try:
            self.score = self.heroClass.score
        except:
            None    
        self.heroCanvas = self.canvas.create_image(100,450, image = self.ImageTank.tank,anchor="nw",tags = ("imagehero")) 
        self.heroClass = Hero([100,475],[130,520],self.score,self.munition,self.vie) 
        self.scoreTexte["text"]= "Score : " + str(self.score)
        # --- Vérification si la manette est branchée ---
        if self.manetteBranchee == True:
            self.manetteClass = Manette(self)
        else:
            self.clavierClass = Clavier(self.fenetre,self)
        self.fin = False # Variable qui devient True quand il y Game Over ou l'appel d'une autre vague
        self.mouvementGauche = 0
        self.mouvementDroite = 0

        # --- Création du canvas avec munition --- (en bas à droite de l'écran)
        self.canvasMunition = Canvas(self.fenetre, width=100, height=40, highlightbackground="black")
        self.canvasMunition.place(x=700,y=604)
        self.munitionImage = []
        for i,missile  in enumerate(self.munition):
            if missile == 1:
                self.munitionImage.append(self.canvasMunition.create_image(10+20*i,2,image=self.ImageTank.superballe_grande,anchor="nw"))
            else:
                self.munitionImage.append(self.canvasMunition.create_image(10+20*i,10,image=self.ImageTank.balle_grande,anchor="nw"))
        
        # ------------------ Lancement de la partie --------------------
        self.AfterAppelVague = self.canvas.after(1000,self.DebutJeu)

    def DebutJeu(self):
        """
        Cette méthode permet :
        - Gerer l'affichage de la vague
        - Créer les aliens, les boucliers et le train
        - Lancer le déplacement des aliens et leurs tirs
        Entrée : self 
            Pour accéder à :
                self.fenetre : Fenetre principale
                self.canvas : Canvas où il y a le jeu
                self.vagueTexte : Petit texte en bas à gauche de l'écran pour indiquer à quel vague est ce que l'on est
                self.vague : Numéro de la vague auquel on est
                self.ImageTank : Class qui contient toutes les images
                self.mouvementAlien : Méthode qui permet de faire déplacer les aliens
                self.tirAlien : Méthode qui permet de faire tirer les aliens
                self.traintriche : True si le code triche : iliketrains est rentré (Apparition de beaucoup de train)
        """
        # --------------- Gestion Graphique de la vague ---------------
        self.vagueTexte = Label(self.fenetre, text = "Vague " + str(self.vague))
        self.vagueTexte.place(x = 200, y = 610)
        self.canvas.delete(self.labelVague)


        #---------------- Création Alien -------------------

        # Choix coordonnées Alien trop fort
        self.alienCanvas = []
        self.alienClass = []
        listePosition = []
        for alien in range(self.nbrAlienFort):
            choixcolonneale = randint(0, 9)
            choixligneale = randint(0, 2)
            while (choixcolonneale,choixligneale) in listePosition:
                choixcolonneale = randint(0, 9)
                choixligneale = randint(0, 2)
            listePosition.append((choixcolonneale,choixligneale))

        
        # Création de tous les aliens
        for j in range(3):
            for i in range(10):
                if (i, j) in listePosition:
                    self.alienCanvas.append(self.canvas.create_image(2 + 50*i, 60 + 50*j, image = self.ImageTank.tank_mechant_super, anchor = "nw", tags = ("imagealien")))
                    self.alienClass.append(AlienFort(1, [2 + 50*i, 60 + 50*j], [32 + 50*i, 105 + 50*j], 2))
                else :
                    self.alienCanvas.append(self.canvas.create_image(2+50*i,60+50*j, image = self.ImageTank.tank_mechant,anchor = "nw", tags = ("imagealien")) )
                    self.alienClass.append(Alien(1,[2+50*i,60+50*j],[32+50*i,105+50*j]))

        # ------------ Création bouclier --------------
        self.bouclierCanvas = []
        self.bouclierClass = []
        for i in range(3): #Pour chaque ilot
            for colonne in range(5): #Pour chaque colonne
                for ligne in range(4): #Pour chaque ligne
                    self.bouclierCanvas.append(self.canvas.create_image(i*200+50+colonne*25,320+ligne*25, image = self.ImageTank.mur,anchor="nw",tags = ("imagebouclier")))
                    self.bouclierClass.append(Bouclier((i*200+50+colonne*25,320+ligne*25),(i*200+75+colonne*25,345+ligne*25)))

        # -------------- Gestion du déplacement des ennemis ---------------- 
        self.compteurAlien = 30
        self.mouvementAlien(0,True)
        self.afterTirAlien = self.canvas.after(1000,self.tirAlien)
        # -------------------Création du train --------------------
        if self.traintriche:
            tempstrain = 100
        else:
            tempstrain = randint(30000,45000)
        self.trainCanvas = self.canvas.create_image(650,25,anchor="nw",image = self.ImageTank.train,tags = ("imagetrain"))
        self.trainClass = Train((650,25))
        self.AfterTrain = self.canvas.after(tempstrain,self.train)

    

    def CodeTriche(self):
        """
        Cette méthode permet :
        - D'afficher une nouvelle fenetre où rentrer les codes triches
        Entrée : self 
            Pour accéder à :
                self.Triche : Méthode qui gère si le code est bon ou non
        """
        fenetreTriche = Tk()
        fenetreTriche.title("Code Triche")
        # --------------------- Création du Label ------------------
        label = Label(fenetreTriche,text = "Rentrez le code-triche : ")
        label.place(x = 85, y = 5)
        codetriche = StringVar()
        champ = Entry(fenetreTriche,textvariable = codetriche)
        champ.focus_set()
        champ.place(x = 87, y = 32)
        bouton = Button(fenetreTriche,text="Valider",command = lambda:self.Triche(champ,fenetreTriche))
        bouton.place(x = 125, y = 60)
        fenetreTriche.resizable(width = False, height = False)
        fenetreTriche.iconbitmap("Image/logo_balle.ico")
        fenetreTriche.geometry("300x100")
        fenetreTriche.mainloop()

    def Triche(self,champ,fenetreTriche):
        """
        
        Cette méthode permet de :
        - fermer la fenetre triche
        - Verifier si le code triche est bon, si oui faire son effet
        Entrée : self, champ, fenetreTriche
        - champ : Référence de l'endroit où on écrit
        - fenetreTriche : Fenetre où l'on rentre les codes triches
        - self :
        Pour accéder à :
            self.munition : Liste qui contient les munitions du héro
            self.nbrTir : Nombre d'alien qui tire en même temps
            self.ajoutTir : Nombre d'alien qui vont tirer en plus à chaque vague
            self.vie : Liste qui correspond à la vie du héro
            self.vieBonus : Vie en plus que le héro a (les coeurs verts)
            self.score : Entier qui correspond au score
            self.nbrAlienFort : Nombre d'alien qui sont fort
            self.tempsentredeuxtirs : Temps entre deux tirs d'alien
            self.invincible : Si True, le héro ne reçoit plus de dégat
            self.traintriche : True si le code triche : iliketrains est rentré (Apparition de beaucoup de train)
        """
        code = champ.get()
        fenetreTriche.destroy()
        # -------------- Gestion des codes rentrés ------------------
        if code == "raze":
            self.munition = [1,1,1,1,1]
        elif code == "stormtrooper":
            self.munition = [0,0,0,0,0]
        elif code == "tropsimple":
            self.nbrTir = 1
            self.ajoutTir = 0
        elif code == "champignon1up": 
            self.vie=[1,1,1]
            self.vieBonus = 7
        elif code == "tricheur":
            self.score += 1000
        elif code == "bonnechance":
            self.nbrTir = 30
        elif code == "impossible":
            self.nbrAlienFort = 30
            self.nbrTir = 30
            self.tempsentredeuxtirs = 1500
        elif code == "modeenfant":
            self.invincible = True
        elif code == "ragequit":
            exit()
        elif code == "iliketrains":
            self.traintriche = True
    
    def destructionbouclier(self): #Changer sa place
        """
        Cette méthode permet de :
        - supprimer l'ensemble des boucliers
        Entrée : self
        Pour accéder à :
            self.bouclierClass : Liste contenant les class des boucliers
            self.bouclierCanvas : Liste contenant les numéros ID des images des boucliers
            self.canvas : Canvas où il y a le jeu
        """
        for i in range(60):
            if self.bouclierClass[i] != 0:
                self.bouclierClass[i] = 0
                self.canvas.delete(self.bouclierCanvas[i])
            

    def mouvementAlien(self,n,right):
        """
        Cette méthode permet de :
        - pouvoir déplacer les Aliens de gauche à droite puis de droite à gauche et qu'ils puissent descendre.
        - vérifier si les Aliens décendent en dessous des boucliers, alors les boucliers disparaissent.
        - vérifier si les Aliens décendent en dessous de "450", la partie est finie (défaite).

        Entrée : self, n, right
        - n : Compteur pour répéter cette Méthode 125 fois
        - right : booléan si true l'alien va à droite sinon à gauche.
        - self :
        Pour accéder à :
            self.manetteClass : Class de Manette() qui permet de jouer à la manette
            self.Manette : Passer en mode : On ne joue qu'à la manette
            self.ClavierMet : Passer en mode : On ne joue qu'au clavier
            self.canvas : Canvas où il y a le jeu
            self.alienCanvas : Liste contenant les numéros ID des images des aliens
            self.alienClass : Liste contenant les class des aliens
            self.mouvementAlien : Méthode qui permet de faire déplacer les aliens
            self.bouclierClass : Liste contenant les class des boucliers
            self.destructionbouclier : Méthode qui permet de détruire tous les boucliers
            self.FinDePartie : Méthode qui permet de lancer soit le Game Over, soit l'appel d'une nouvelle vague
        """

        try:
            if self.manetteClass.VerifManetteBranchee():
                self.ManetteMet()
                self.manetteClass.Entree() #Permet de vérifier entrée des qu'alien se deplace (tout le temps donc)
            else:
                self.ClavierMet()
        except AttributeError:
            self.ClavierMet()
        
        if n < 118:
            for i in range(30):
                if self.alienClass[i] != 0 : #Quand un alien meurt, il est remplacé par un 0 dans self.alienClass, on ne prend donc que les aliens en vie
                    deplac = self.alienClass[i].deplacement(right) # deplac c'est soit negatif pour aller à gauche, soit positif pour aller à droite
                    self.canvas.move(self.alienCanvas[i],deplac,0)
                    self.alienClass[i].changementPosition((deplac,0))
            self.afterMouvementAlien=self.canvas.after(45,lambda:self.mouvementAlien(n+1,right))
            
        else :
            if n <125: #Pour faire descendre l'Alien
                for i in range(30):
                    if self.alienClass[i] != 0:
                        deplac = self.alienClass[i].deplacement(right)
                        self.canvas.move(self.alienCanvas[i],0,abs(deplac)) # abs(deplac) permet de garantir que les Aliens se déplacent vers le bas (et pas vers le haut)
                        self.alienClass[i].changementPosition((0,abs(deplac)))
                        for j in range(60):
                            if self.bouclierClass[j] != 0:
                                if self.alienClass[i].position2[1] >= self.bouclierClass[j].position1[1] : # si les Aliens dépassent les boucliers ==> on supprime les boucliers
                                    self.destructionbouclier()
                        if self.alienClass[i].position2[1] >= 450: #si les Aliens dépassent la position 450 (en bas de l'écran) alors la partie est perdue
                            self.FinDePartie(False)
                self.afterMouvementAlien = self.canvas.after(45,lambda:self.mouvementAlien(n+1,right))
            else :
                self.afterMouvementAlien = self.canvas.after(45,lambda:self.mouvementAlien(0,not right))     

    def tirAlien(self): 
        """
        Cette méthode permet de :
            Choisir les aliens qui vont tirer
            Faire tirer ces aliens (apparition des lasers)
            D'appeler la méthode pour faire avancer ces lasers
        Entrée : self 
        Pour accéder à :
            self.fin : True si c'est la fin de la partie. False sinon
            self.alienClass : Liste contenant les class des aliens
            self.alienCanvas : Liste contenant les numéros ID des images des aliens
            self.nbrTir : Nombre d'alien qui tire en même temps
            self.canvas : Canvas où il y a le jeu
            self.ImageTank : Class qui contient toutes les images
            self.mouvementTirAlien : Méthode qui permet de gérer le déplacement du tir des aliens
            self.tirAlien : Méthode qui permet de faire tirer les aliens
        """
        # -------------------------- Choix de quels aliens vont tirer -------------------------------
        nombreAlien = 0
        listeAlien = []
        alienQuiTir = []
        listeAlienCanvas = []
        if not self.fin:
            for i in range(30):
                if self.alienClass[i] != 0:
                    nombreAlien += 1
                    listeAlien.append(self.alienClass[i])
                    listeAlienCanvas.append(self.alienCanvas[i])
            if nombreAlien >= self.nbrTir: # permet de faire tirer les aliens de façon aléatoire mais ils doivent être plus que 3
                while len(alienQuiTir) != self.nbrTir:
                    random = randint(0,29)
                    if self.alienClass[random] != 0 and random not in alienQuiTir:
                        alienQuiTir.append(random)
            else:   # Tous les aliens qui restent tirent
                for alien in self.alienCanvas:
                    if alien in listeAlienCanvas:
                        alienQuiTir.append(self.alienCanvas.index(alien))
            # -------------------------------- Création des tirs -------------------------------
            laserCanvas = []
            laserClass = []
            for alien in alienQuiTir:
                if isinstance(self.alienClass[alien],AlienFort):  
                    laserCanvas = self.canvas.create_image(self.alienClass[alien].position2[0]-15, self.alienClass[alien].position2[1]-7, image = self.ImageTank.superballe_mechante,anchor="nw",tags = ("laserennemi"))
                    laserClass = LaserFort([self.alienClass[alien].position2[0]-15, self.alienClass[alien].position2[1]-7] ,[ self.alienClass[alien].position2[0]-5, 33 +self.alienClass[alien].position2[1]])
                else:
                    laserCanvas = self.canvas.create_image(self.alienClass[alien].position2[0]-15, self.alienClass[alien].position2[1]-7, image = self.ImageTank.balle_mechante,anchor = "nw",tags = ("laserennemi"))
                    laserClass = Laser([self.alienClass[alien].position2[0]-15, self.alienClass[alien].position2[1]-7 ],[self.alienClass[alien].position2[0]-10, 18 +self.alienClass[alien].position2[1]])
                self.mouvementTirAlien(laserCanvas,laserClass,)
            self.afterTirAlien = self.canvas.after(self.tempsentredeuxtirs,self.tirAlien)

    def mouvementTirAlien(self,laserCanvas,laserClass):
        """
        Cette méthode permet de :
        - Déplacer les tirs des aliens
        - Gérer les différentes collisions avec le héro, les boucliers
        Entrée : self, laserCanvas, laserClass
        - laserCanvas : ID de l'image du Laser qui avance
        - laserClass : Class du Laser qui avance
        - self :
        Pour accéder à :
            self.fin : True si c'est la fin de la partie. False sinon
            self.canvas : Canvas où il y a le jeu
            self.heroClass : Class de Hero() 
            self.mouvementTirAlien : Méthode qui permet de gérer le déplacement du tir des aliens
            self.invincible : Si True, le héro ne reçoit plus de dégat
            self.majBarreDeVie : Méthode pour actualiser la barre de vie
            self.barreVie : Barre de vie du héro
            self.vieBonus : Vie en plus que le héro a (les coeurs verts)
            self.textevieBonus : Texte avec les coeurs verts qui est affiché
            self.bouclierClass : Liste contenant les class des boucliers
            self.bouclierCanvas : Liste contenant les numéros ID des images des boucliers
            self.convertisseurVieenCoeur : Méthode qui permet de mettre des coeurs à la place du nombre de vie bonus
            self.FinDePartie : Méthode qui permet de lancer soit le Game Over, soit l'appel d'une nouvelle vague
        """
        if not self.fin:
            if laserClass.position1[1] < 502: #Permet de vérifier s'il touche la bordure.
                ObjetTouche = self.canvas.find_overlapping(laserClass.position1[0], laserClass.position1[1], laserClass.position2[0],laserClass.position2[1]) #Tuple contenant des toutes les ID des images que le laser touche
                if not len(ObjetTouche) > 2 or "imagealien" in self.canvas.gettags(ObjetTouche[1]) or "imagelaser" in self.canvas.gettags(ObjetTouche[1]) or "imageexplo" in self.canvas.gettags(ObjetTouche[1]): #Si rien ne touche le laser ou laser touche alien ou le laser touche laser gentil
                    self.canvas.move(laserCanvas,0,5)
                    laserClass.changementPosition((0,5))   
                    self.afterMouvementTirAlien = self.canvas.after(25,lambda:self.mouvementTirAlien(laserCanvas,laserClass))
                    
                elif "imagehero" in self.canvas.gettags(ObjetTouche[1]): #Touche le héro
                    if not self.invincible:
                        self.majBarreDeVie(self.barreVie['value'] - (1/3)*100)
                        if isinstance(laserClass, LaserFort) and len(self.heroClass.vie) != 1:
                            self.majBarreDeVie(self.barreVie['value'] - (1/3)*100)
                            self.heroClass.changementVie(-1)
                        self.heroClass.changementVie(-1)
                        self.canvas.delete(laserCanvas)
                        del laserClass
                        if len(self.heroClass.vie) < 3 and  self.vieBonus >= 1: # permet que si le hero a un point bonus de le convertir en vie.
                            while len(self.heroClass.vie) != 3 and self.vieBonus != 0:
                                self.majBarreDeVie(self.barreVie['value'] + (1/3)*100)                
                                self.vieBonus -= 1
                                self.heroClass.changementVie(1)
                                self.textevieBonus["text"] = self.convertisseurVieenCoeur(self.vieBonus)
                        if self.heroClass.vie == []:
                            self.FinDePartie(False)
                    else: # Cas hero invincible donc on detruit missile
                        self.canvas.delete(laserCanvas)
                        del laserClass
                elif "imagebouclier" in self.canvas.gettags(ObjetTouche[1]): # Touche des protections
                    index = self.bouclierCanvas.index(ObjetTouche[1])
                    self.canvas.delete(self.bouclierCanvas[index])
                    self.bouclierClass[index] = 0 
                    if not isinstance(laserClass, LaserFort):
                        self.canvas.delete(laserCanvas)
                        del laserClass
                    else:
                        self.canvas.move(laserCanvas,0,5)
                        laserClass.changementPosition((0,5))
                        self.afterMouvementTirAlien = self.canvas.after(25,lambda:self.mouvementTirAlien(laserCanvas,laserClass))
                else:
                    self.canvas.move(laserCanvas,0,5)
                    laserClass.changementPosition((0,5))

                    self.afterMouvementTirAlien = self.canvas.after(25,lambda:self.mouvementTirAlien(laserCanvas,laserClass))
            else:
                self.canvas.delete(laserCanvas)
                del laserClass
        else:
            self.canvas.delete(laserCanvas)
            del laserClass

    def convertisseurVieenCoeur(self,nbrVieBonus):
        """
        Cette méthode permet :
        - de convertir un nombre (on l'utilise pour le nombre de vie bonus) en des coeurs.
        Entree : self, nbrVieBonus correspond au nombre de vie bonus à convertir en coeur
        Sortie : "l", c'est la liste avec les coeurs.
        """
        coeur = "♥"
        l = ""
        for i in range(nbrVieBonus):
            l = l + coeur
        return l
      
    # ---------------------------------------- Mouvement Joueur -----------------------------------------
    def gauche(self,event):
        """
        Cette méthode permet de :
        - Déplacer le héro vert la gauche
        Entrée : self, event
        - event : Car c'est une méthode que l'on appelle à  travers un input
        - self :
            Pour accéder à :
                self.heroClass : Class de Hero() 
                self.mouvementGauche : Compteur pour répéter cette méthode 10 fois et créer une impression de glissement
                self.canvas : Canvas où il y a le jeu
                self.gauche : Méthode qui permet de déplacer le héro vers la gauche
        """
        if self.heroClass.position2[0] > 0 :
            if self.mouvementGauche < 10:
                self.canvas.move(self.heroCanvas,-1,0)
                self.heroClass.changementPosition((-1,0))
                self.mouvementGauche += 1                
                self.canvas.after(2,lambda:self.gauche(event))
            else:
                self.mouvementGauche = 0
        else: # Gère le fait de traverser l'écran d'un bout à l'autre (Idée donnée par Olivier Mermet)
            self.canvas.move(self.heroCanvas,621,0)
            self.heroClass.changementPosition((621,0))
            self.mouvementGauche = 0

    def droite(self,event):
        """
        Cette méthode permet de :
        - Déplacer le héro vert la droite
        Entrée : self, event
        - event : Car c'est une méthode que l'on appelle à travers un input
        - self :
            Pour accéder à :
                self.heroClass : Class de Hero() 
                self.mouvementDroite : Compteur pour répéter cette méthode 10 fois et créer une impression de glissement
                self.canvas : Canvas où il y a le jeu
                self.droite : Méthode qui permet de déplacer le héro vers la droite
        """
        if self.heroClass.position1[0] < 601:
            if self.mouvementDroite < 10:
                self.canvas.move(self.heroCanvas,1,0)
                self.heroClass.changementPosition((1,0))
                self.mouvementDroite += 1
                self.canvas.after(2,lambda:self.droite(event))
            else :
                self.mouvementDroite = 0
        else : # Gère le fait de traverser l'écran d'un bout à l'autre (Idée donnée par Olivier Mermet)
            self.canvas.move(self.heroCanvas,-621,0)
            self.heroClass.changementPosition((-621,0))

            self.mouvementDroite = 0

    def tirJoueur(self,event):
        """
        Cette méthode permet de :
        - Faire apparaître une balle
        Entrée : self, event
        - event : Car c'est une méthode que l'on appelle à  travers un input
        - self :
            Pour accéder à :
                self.fin : True si c'est la fin de la partie. False sinon
                self.verifTir : True si le hero peut tirer. False sinon
                self.canvas : Canvas où il y a le jeu
                self.heroClass : Class de Hero() 
                self.ImageTank : Class qui contient toutes les images
                self.munition : Liste qui contient les munitions du héro
                self.munitionImage : Liste qui contient les images des munitions
                self.deplacementMunition : Méthode qui permet de dépacer les munitions
                self.mouvementTir : Méthode qui gère le déplacement des missiles du héro
        """
        if not self.fin:
            if self.verifTir: 
                if self.heroClass.gestionTir(): # Créer laser normal ou laser fort
                    self.laserJoueurCanvas = self.canvas.create_image(12 + self.heroClass.position1[0], 430, image = self.ImageTank.balle,anchor="nw",tags = ("imagelaser"))
                    self.laserJoueurClass = Laser([12 + self.heroClass.position1[0], 430] ,[20 + self.heroClass.position1[0], 460])
                else:
                    self.laserJoueurCanvas = self.canvas.create_image(12 + self.heroClass.position1[0], 420, image = self.ImageTank.superballe,anchor="nw",tags = ("imagelaser"))
                    self.laserJoueurClass = LaserFort([12 + self.heroClass.position1[0], 430] ,[17 + self.heroClass.position1[0], 470])
                self.verifTir = False
                # Gestion animation fumée de tir:
                self.imagefumeetir = self.canvas.create_image( self.heroClass.position1[0], 430, image = None, anchor = "nw",tags = ("animfumeetir"))
                self.Animation(50,[self.ImageTank.fumee_anim_1,self.ImageTank.fumee_anim_2,self.ImageTank.fumee_anim_3,self.ImageTank.fumee_anim_4,self.ImageTank.fumee_anim_5],self.imagefumeetir)
                
                if self.munition[-1] == 1:
                    self.munitionImage.append(self.canvasMunition.create_image(110,2,image=self.ImageTank.superballe_grande,anchor = "nw"))
                else:
                    self.munitionImage.append(self.canvasMunition.create_image(110,10,image=self.ImageTank.balle_grande,anchor = "nw"))
                self.deplacementMunition(0)
                self.mouvementTir()

    def deplacementMunition(self,i): 
        """
        Cette méthode permet :
        - Déplacer les munitions vers la gauche et d'en créer une nouvelle (visuellement)
        Entrée : self,i
        - i : Compteur pour répéter cette Méthode 5 fois
        - self :
            Pour accéder à :
                self.munitionImage : Liste qui contient les images des munitions
                self.canvasMunition : Canvas où les munitions se trouve
                self.deplacementMunition : Méthode qui permet de dépacer les munitions
        """
        if i != 5:
            for missile in self.munitionImage:
                self.canvasMunition.move(missile,-4,0)
            self.AfterDeplacementMunition = self.canvasMunition.after(25,lambda:self.deplacementMunition(i+1))
        else : 
            self.canvasMunition.delete(self.munitionImage[0])
            self.munitionImage.pop(0)

    def mouvementTir(self): 
        """
        Cette méthode permet :
        - Déplacer le laser du héro qui a été tiré
        Entrée : self
            Pour accéder à :
                self.fin : True si c'est la fin de la partie. False sinon
                self.laserJoueurClass : Class du laser du joueur
                self.canvas : Canvas où il y a le jeu
                self.laserJoueurCanvas : ID de l'image du Laser du héro qui avance
                self.mouvementTir : Méthode qui permet de faire avancer le laser du héro
                self.mortAlien : Méthode qui permet de détruire l'alien créé 
                self.Animation : Méthode qui permet de gérer des animations
                self.ImageTank : Class qui contient toutes les images
                self.bouclierClass : Liste contenant les class des boucliers
                self.bouclierCanvas : Liste contenant les numéros ID des images des boucliers
                self.trainCanvas : ID de l'image du train
                self.trainClass : Class du train
                self.majBarreDeVie : Méthode pour actualiser la barre de vie
                self.barreVie : Barre de vie du héro
                self.vieBonus : Vie en plus que le héro a (les coeurs verts)
                self.textevieBonus : Texte avec les coeurs verts qui est affiché
                self.verifTir : True si le hero peut tirer. False sinon
        """
        if not self.fin:
            if self.laserJoueurClass.position2[1] > 0:
                ObjetTouche = self.canvas.find_overlapping(self.laserJoueurClass.position1[0], self.laserJoueurClass.position1[1], self.laserJoueurClass.position2[0],self.laserJoueurClass.position2[1])
                if not len(ObjetTouche) > 2: #Si le laser ne touche rien => Il avance
                    self.canvas.move(self.laserJoueurCanvas,0, -1.25) # vitesse de l'objet
                    self.laserJoueurClass.changementPosition((0, -1.25))
                    self.afterMouvementTir = self.canvas.after(1,self.mouvementTir)
                else:
                    
                    if self.heroCanvas not in ObjetTouche: #Permet de ne pas prendre en compte les collisions entre le Laser et le Joueur
                        if "imagealien" in self.canvas.gettags(ObjetTouche[1]): #On vérifie s'il sagit d'un Alien
                            self.mortAlien(ObjetTouche[1],None)
                            if isinstance(self.laserJoueurClass,LaserFort): #Si le Laser est Fort : Création d'une explosion
                                self.positionX = self.laserJoueurClass.position1[0] + 5
                                self.positionY = self.laserJoueurClass.position1[1] - 30
                                explosionanim = self.canvas.create_image(self.positionX-30, self.positionY-30, image = None, anchor = "nw", tags = ("imageexplo"))
                                self.Animation(110,[self.ImageTank.explo_1,self.ImageTank.explo_2,self.ImageTank.explo_3,self.ImageTank.explo_4], explosionanim) #Animation de l'explosion
                        
                        elif "imagebouclier" in self.canvas.gettags(ObjetTouche[1]): #Il s'agit d'un bouclier
                            index = self.bouclierCanvas.index(ObjetTouche[1])
                            self.canvas.delete(self.bouclierCanvas[index])
                            self.bouclierClass[index] = 0

                        elif "imagetrain" in self.canvas.gettags(ObjetTouche[1]): # Il s'agit du train
                            self.heroClass.changementScore(20)
                            self.canvas.delete(self.trainCanvas)
                            self.trainClass = 0
                            if len(self.heroClass.vie) < 3 :
                                self.majBarreDeVie(self.barreVie['value'] + (1/3)*100)
                                self.heroClass.changementVie(1)
                            else : 
                                self.vieBonus += 1
                                self.textevieBonus["text"] = " + " + self.convertisseurVieenCoeur(self.vieBonus)

                        if "animfumeetir" not in self.canvas.gettags(ObjetTouche[2]): #Gère les collisions avec l'animation de fumée quand le Joueur tire
                            self.canvas.delete(self.laserJoueurCanvas)
                            del self.laserJoueurClass
                            self.verifTir = True
                        else:
                            self.canvas.move(self.laserJoueurCanvas,0, -1.25) # vitesse de l'objet
                            self.laserJoueurClass.changementPosition((0, -1.25))
                            self.afterMouvementTir = self.canvas.after(1,self.mouvementTir)   

                    else : #Si le laser touche le héro : il continue à avancer
                        self.canvas.move(self.laserJoueurCanvas,0, -1.25) # vitesse de l'objet
                        self.laserJoueurClass.changementPosition((0, -1.25))
                        self.afterMouvementTir = self.canvas.after(1,self.mouvementTir)
                       
            else: # Si le laser a atteind le bord de l'écran : On le supprime
                self.canvas.delete(self.laserJoueurCanvas)
                del self.laserJoueurClass
                self.verifTir = True
        else: # Si c'est la fin : on détruit le laser
            self.canvas.delete(self.laserJoueurCanvas)
            del self.laserJoueurClass

    def GestionExplosion(self,positionX,positionY,i,listeTankFortTouche):
        """
        Cette méthode permet :
        - Calculer si l'objet touche l'explosion 
        - Si l'alien est touché on appelle la méthode pour le tuer
        Entrée : self,positionX,positionY,explosion,i,listeTankFortTouche
        - positionX : position X de l'explosion
        - positionY : position Y de l'explosion
        - i : Compteur pour répéter cette Méthode 10 fois
        - listeTankFortTouche : Liste qui contient les ID des Tanks forts qui ont été touché par l'explosion
        - self
            Pour accéder à :
                self.canvas : Canvas où il y a le jeu
                self.alienCanvas : Liste contenant les numéros ID des images des aliens
                self.mortAlien : Méthode qui permet de détruire l'alien créé 
                self.GestionExplosion : Méthode qui permet de vérifier si les images sont dans le rayon de l'explosion
        """
        for item in self.canvas.find_all():
            if item in self.alienCanvas and item not in listeTankFortTouche:
                        # ----------------- Récupération des coordonnées du centre de l'explosion ------------------------ 
                bbox = self.canvas.bbox(item)
                center_x = (bbox[0] + bbox[2]) / 2
                center_y = (bbox[1] + bbox[3]) / 2
                distance = ((center_x - positionX)**2 + (center_y - positionY)**2)**0.5 # Calcul de la distance entre le centre de l'explosion et les aliens
                if distance <= 60: # Si l'élément se trouve à l'intérieur du cercle de l'explosion
                    self.mortAlien(item,listeTankFortTouche)           
        if i != 10 :
            self.AfterGestionExplosion = self.canvas.after(20,lambda:self.GestionExplosion(positionX,positionY,i+1,listeTankFortTouche))
    
    def mortAlien(self,item,listeTankFortTouche):
        """
        Cette méthode permet :
        - Supprimer un tank
        - Changer d'image quand on tire sur un tank fort (et lui retirer une vie)
        Entrée : self,positionX,positionY,explosion,i,listeTankFortTouche
        - item : ID du tank ennemi qui a été touché
        - listeTankFortTouche : Liste qui contient les ID des Tanks forts qui ont été touché par l'explosion
        - self
            Pour accéder à :
                self.canvas : Canvas où il y a le jeu
                self.alienClass : Liste contenant les class des aliens
                self.alienCanvas : Liste contenant les numéros ID des images des aliens
                self.ImageTank : Class qui contient toutes les images
                self.heroClass : Class de Hero() 
                self.scoreTexte : Texte qui affiche le score du Joueur
                self.compteurAlien : Nombre d'aliens encore en vie
                self.Animation : Méthode qui permet de gérer des animations
                self.FinDePartie : Méthode qui permet de lancer soit le Game Over, soit l'appel d'une nouvelle vague
        """
        index = self.alienCanvas.index(item)
        if isinstance(self.alienClass[index],AlienFort) and self.alienClass[index].death():
            self.canvas.itemconfig(self.alienCanvas[index],image = self.ImageTank.tank_mechant_super_amoche)
            try:
                listeTankFortTouche.append(item)
            except:
                None
        else:
            if isinstance(self.alienClass[index],AlienFort):
                scoreAAjouter = 15
            else:
                scoreAAjouter = 10
            if self.alienClass[index] != 0:
                self.heroClass.changementScore(scoreAAjouter)
                self.scoreTexte["text"]= "Score : " + str(self.heroClass.score)
                self.compteurAlien -= 1
                self.alienClass[index] = 0
                self.Animation(60,[self.ImageTank.fum_1,self.ImageTank.fum_2,self.ImageTank.fum_3,self.ImageTank.fum_4],self.alienCanvas[index])
        if self.compteurAlien == 0:
            self.FinDePartie(True) 

    def Animation(self,temps,listeanimation,imageanimation):
        """
        Cette méthode permet :
        - Gérer les animations
        - Créer une explosion en appelant une autre méthode
        Entrée : self,temps,listeanimation,imageanimation
        - temps : Temps d'attente entre 2 images
        - listeanimation : Liste qui contient toutes les images pour former une animation
        - imageanimation : ID de l'image que l'on doit modifier
        - self
            Pour accéder à :
                self.canvas : Canvas où il y a le jeu
                self.ImageTank : Class qui contient toutes les images
                self.GestionExplosion : Méthode qui permet de vérifier si les images sont dans le rayon de l'explosion
                self.positionX : Position X de l'image pour placer explosion
                self.positionY : Position Y de l'image pour placer explosion
                self.Animation : Méthode qui permet de gérer des animations
        """
        if listeanimation == []:
            self.canvas.delete(imageanimation)
        else:
            self.canvas.itemconfig(imageanimation,image = listeanimation[0])
            if listeanimation[0] == self.ImageTank.explo_4:
                self.GestionExplosion(self.positionX,self.positionY,0,[])
                temps = 200
            self.canvas.after(temps,lambda:self.Animation(temps,listeanimation[1:],imageanimation))
        
    def train(self):
        """
        Cette méthode permet :
        - Gérer le déplacement du train
        - Gérer l'apparition infinie des trains si le code triche est rentrée
        Entrée : self
            Pour accéder à :
                self.canvas : Canvas où il y a le jeu
                self.trainCanvas : ID de l'image du train
                self.trainClass : Class du train
                True si le code triche : iliketrains est rentré (Apparition de beaucoup de train)
                self.train : Méthode qui gère le déplacement du train
                self.ImageTank : Class qui contient toutes les images
        """
        if self.trainClass != 0 : #On vérifie s'il le train n'est pas mort
            if self.trainClass.positionX > -200:
                self.canvas.move(self.trainCanvas,-3,0)
                self.trainClass.changementPosition([-3,0])
                self.AfterTrain = self.canvas.after(25,self.train)
            else:
                self.trainClass = 0
                self.canvas.delete(self.trainCanvas)
                self.AfterTrain = self.canvas.after(25,self.train)
        else:
            if self.traintriche: #Permet de gérer le code triche don
                self.trainCanvas = self.canvas.create_image(650,25,anchor="nw",image = self.ImageTank.train,tags = ("imagetrain"))
                self.trainClass = Train((650,25))
                self.AfterTrain = self.canvas.after(100,self.train)

    def ScoreAZero(self):
        """
        Cette méthode permet de supprimer toutes les données du fichier jusqu'à la 1ère ligne (où on laisse un 0)
        Entrée : self
            Pour accéder à :
            - self.Recommencer : Méthode pour recommencer la partie 
        """
        fichier = open("meilleursScores.txt",'r+') # ouverture du fichier en mode r+ (lecture et écriture)
        fichier.truncate(1) # permet de supprimer les données du fichier jusqu'à la 1ere ligne (on laisse le 0 du début dans le fichier)
        self.Recommencer()

    def MeilleurScore(self, score):
        """
        Cette méthode permet de garder le meilleur score entre le score de la partie et le meilleur score des anciennes parties. 
        Et cette méthode garde que le valeur du meilleur score sur la 2eme ligne du fichier "meilleursScores.txt".
        Entrée : self, score
        - score : score de la partie
        Sortie : scoreMax (on retourne le meilleur score)
        """
        # lecture du fichier
        fichier = open("meilleursScores.txt",'a') 
        fichier.write('\n' + score)
        fichier.close()
        fichier = open("meilleursScores.txt",'r')
        contenu = fichier.read()
        fichier.close()
        listeScore = contenu.split('\n')
        listeScoreint = []
        for valeur in listeScore: # on convertit la liste avec les scores(String) en liste des scores(int)
            listeScoreint.append(int(valeur))
            scoreMax = max(listeScoreint)

        # On enlève les valeurs qui occupent le fichier :
        fichier = open("meilleursScores.txt",'r+')
        fichier.truncate(1) # permet de supprimer les données du fichier jusqu'à la 1ere ligne (on laisse le 0 du début dans le fichier)
        # On rajoute le score max du fichier
        fichier = open("meilleursScores.txt",'a')
        fichier.write('\n' + str(scoreMax))
        fichier.close()
        return(scoreMax) # on retourne le max de tous les scores(cad de la listeScore)

    def majBarreDeVie(self,valeur):
        """
        Cette méthode permet de mettre à jour la longueur de la barre de vie en fonction de la valeur donnée ("valeur").
        Entrées : self, valeur
        - valeur : entier au quel on doit mettre à jour la barre
        - self : 
            Pour accéder à :
                self.barreVie : Barre de vie du héro
        """
        self.barreVie['value'] = valeur

    def FinDePartie(self,win):
        """
        Cette méthode permet :
        - Afficher l'écran de Game Over ou Appeler la vague d'après
        - Supprmier ce qui reste encore à l'écran que le héro n'a pas détruit
        - Augmenter la difficulté de la vague d'après
        - Changer le meilleur score
        Entrée : self,win
        - win : True si le héro a tué tous les aliens. False si le héro n'a plus de vie
        - self
            Pour accéder à :
                self.MeilleurScore : Méthode qui permet de modifier le meilleur score
                self.heroClass : Class de Hero() 
                self.meilleurScoreTexte : Texte où est affiché le meilleur score
                self.alienCanvas : Liste contenant les numéros ID des images des aliens
                self.canvas : Canvas où il y a le jeu
                self.destructionbouclier : Méthode qui permet de détruire tous les boucliers
                self.vague : Numéro de la vague auquel on est
                self.vie : Liste qui correspond à la vie du héro
                self.munition : Liste qui contient les munitions du héro
                self.nbrTir : Nombre d'alien qui tire en même temps
                self.ajoutTir : Nombre d'alien qui vont tirer en plus à chaque vague
                self.nbrAlienFort : Nombre d'alien qui sont fort
                self.tempsentredeuxtirs : Temps entre deux tirs d'alien
                self.stopAfter : Méthode qui permet de stopper tous les After
                self.AppelVague : Méthode pour lancer une vague d'ennemi
                self.ImageTank : Class qui contient toutes les images
        """
        if self.MeilleurScore(str(self.heroClass.score)) == str(self.heroClass.score) :
            self.meilleurScoreTexte["text"] = "Meilleurs Score : " + self.MeilleurScore(str(self.heroClass.score))
        
        self.fin = True 
        
        for v in self.alienCanvas:
            if v != 0:
                self.canvas.delete(v)
        self.destructionbouclier()
        if win: # Si le héro a tué tous les aliens => Appel d'une nouvelle vague
            self.vague += 1
            self.vie = self.heroClass.vie
            self.munition = self.heroClass.munition
            self.canvas.delete('all')
            if self.nbrTir != 30:
                self.nbrTir += self.ajoutTir
            if self.nbrAlienFort != 30:
                self.nbrAlienFort += 3
            if self.tempsentredeuxtirs != 1500:
                self.tempsentredeuxtirs -= 100
            self.stopAfter()
            self.AppelVague()
        else:
            self.canvas.delete(self.fond)
            self.fond = self.canvas.create_image(0,0, image = self.ImageTank.gameover, anchor = "nw")
