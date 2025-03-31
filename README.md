[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12808498&assignment_repo_type=AssignmentRepo)

Bonjour,
Merci d'avoir installé le jeu : Earth Invader.
En espérant que celui-ci vous plaira !
Ce jeu a été réalisé par Nathan et Raphaël étudiant en 3 ETI (Groupe C) à CPE Lyon.
Pour lancer le jeu, il suffit d'exécuter le programme : PP.py

_____________________LES REGLES DU JEU_____________________
    --- OBJECTIF ---
    Détruire les envahisseurs (tanks ennemis): 
    Le joueur contrôle un tank situé en bas de l'écran et doit éliminer tous les envahisseurs qui descendent vers lui 
    (et bien sur éviter les balles).

    --- GAMEPLAY ---
    Déplacements du héro (tank) : 
    Le joueur peut se déplacer horizontalement (gauche et droite) en bas de l'écran pour éviter les tirs ennemis et tirer sur les tanks adverses.
    Il peut soit utiliser les touches du clavier (left,right et space), soit une manette.

    --- TANKS ENNEMIS ---
    Il existe 2 types de tanks ennemis : les "normaux" et les "Supers Tanks".
    Les "normaux" possèdent 1 vie et tirent une balle normale qui enlève 1 vie et rapportent 10 points de scores.
    Les "Supers Tanks" possèdent 2 vie et tirent une super balle qui enlève 2 vie et rapportent 15 points de scores.

    --- BARRIERES PROTECTRICES ---
    Le joueur peut se rejugier derrières les barrières, pour éviter les feux ennemis.
    Cependant si les ennemis atteignent les barrières, elles disparaissent.

    --- TRAIN ---
    Tchou ! Tchou ! En effet, un train circule en haut de l'écran.
    Si le joueur arrive à le toucher : le tank héro gagne soit une vie et 20 points de scores.

    --- MECANIQUES DU JEU ---
    --> VIE : Le joueur dispose initialement de 3 vies. La partie se termine, lorsqu'il pert toutes ses vies.
    --> SCORE : 
        Le joueur gagne s'il touche avec un missile un :
        - tank normal : 10 points
        - Super Tank : 15 points (à sa destruction)
        - Train : 20 points

    --- DIFFICULTES CROISSANTES ---
    --> A chaques vagues d'ennemis, il y a de plus en plus de super Tank, la cadence de tir des tanks est améliorées et il y a plus de tanks qui tirent.

    --- Ajout de certaines fonctionnalités :
    - les codes de triches
    raze ==> permet d'avoir des supers munitions 
    stormtrooper ==> permet d'avoir les munitions de base
    tropsimple ==> permet d'avoir qu'un seul ennemi qui tire
    champignon1up ==> permet d'avoir 7 vies bonus
    tricheur ==> permet de commencer la partie avec 1000 points de score
    bonnechance ==> tous les tanks tirent des missiles normaux
    impossible ==> tous les tanks tirent des supers missiles
    modeenfant ==> le joueur ne prend pas de dégat par balle
    ragequit ==> le jeu se ferme
    iliketrains ==> il y a plus de trains qui passent



Implémentation des outils : liste, file et pile :
- LISTE :
La liste est la variable qui contient les images des boucliers, elle est représentée (dans le fichier "Jeu.py" (pour la "class Jeu", méthode "DebutJeu")) par : self.bouclierCanvas.
Nous avons utiliser une liste car nous devons avoir accès à nimporte quel des éléments de la liste quand le bouclier est touché par un missile.
Le principe est de pouvoir changer nimporte quel éléments de cette liste, de le supprimer ou encore d'en rajouter d'autres .
- FILE :
La file est le chargeur de munition du joueur, elle est représentée (dans le fichier "Jeu.py" (pour la "class Jeu", méthode "Recommencer")) par : self.munition = [0,0,0,0,1]
Nous faisons les opérations sur la file dans la class Hero(fichier "Hero.py") avec notre méthode "gestionTir".
Le principe est d'enlèver le premier élément de la liste puis de le rajouter à la fin de celle-ci.

- PILE :
la pile est la vie du joueur, elle est représentée (dans le fichier "Jeu.py" (pour la "class Jeu", méthode "Recommencer")) par : self.vie = [1,1,1]
Nous faisons les opérations sur la pile dans la class Hero (fichier "Hero.py") avec notre méthode "changementVie".
Le principe est d'ajouter un 1 à la fin de la liste pour rajouter une vie en plus, ou d'enlever un 1 à la fin de la liste pour enléver une vie.


 L’adresse de notre répertoire GIT
https://github.com/cpe-lyon/groupe-c-berger-frume-csdev-spaceinvaders



Remerciment  :
- à notre designer Quentin FRUME pour toutes ces magnifiques images.
- à notre compositeur Quentin FRUME pour cette magnifique musique.
- aux nombreuses idées de Thibaud DAUBIGNEY (Notamment pour les munitions)
- à Olivier MERMET pour l'idée du déplacement du joueur qui permet de se téléporter aux bords de l'écran 
