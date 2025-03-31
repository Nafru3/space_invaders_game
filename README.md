# Earth Invader

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12808498&assignment_repo_type=AssignmentRepo)

## Introduction
Welcome to **Earth Invader**! Thank you for installing our game—we hope you enjoy playing it!

This game was developed by **Nathan and Raphaël**, students in **3 ETI (Group C) at CPE Lyon**.
To launch the game, simply run the file: `PP.py`.

## Game Rules

### Objective
Destroy the invaders (enemy tanks):
The player controls a tank at the bottom of the screen and must eliminate all invading tanks descending toward them while avoiding enemy bullets.

### Gameplay
- **Player movement:** The player can move horizontally (left and right) at the bottom of the screen to evade enemy fire and shoot at enemy tanks.
- **Controls:** The player can use either the keyboard (Left, Right, and Space keys) or a game controller.

### Enemy Tanks
There are two types of enemy tanks:
- **Normal Tanks**: 1 HP, fire normal bullets (-1 HP to the player), and reward 10 points upon destruction.
- **Super Tanks**: 2 HP, fire super bullets (-2 HP to the player), and reward 15 points upon destruction.

### Protective Barriers
- The player can take cover behind protective barriers to avoid enemy fire.
- If enemies reach the barriers, they will disappear.

### Train Mechanic
- A train occasionally moves across the top of the screen.
- Shooting the train grants **+1 life** and **+20 points**.

### Game Mechanics
- **Lives**: The player starts with 3 lives. The game ends when all lives are lost.
- **Scoring:**
  - Destroying a Normal Tank: +10 points
  - Destroying a Super Tank: +15 points
  - Hitting the train: +20 points

### Increasing Difficulty
With each new wave of enemies:
- More **Super Tanks** appear.
- Enemy fire rate increases.
- More tanks are capable of shooting.

## Cheat Codes
The following cheat codes can be used in the game:
- `raze` → Grants super ammunition.
- `stormtrooper` → Resets to basic ammunition.
- `tropsimple` → Only one enemy tank shoots.
- `champignon1up` → Grants 7 bonus lives.
- `tricheur` → Starts the game with 1000 points.
- `bonnechance` → All tanks fire normal missiles.
- `impossible` → All tanks fire super missiles.
- `modeenfant` → The player takes no bullet damage.
- `ragequit` → Closes the game.
- `iliketrains` → More trains appear.

## Implementation of Data Structures

### **List (Array)**
- **Usage**: Stores shield images.
- **Implementation**: `self.bouclierCanvas` in `Jeu.py` (Class `Jeu`, method `DebutJeu`).
- **Reason**: The list allows access to any shield element when it is hit by a missile, enabling modifications, additions, and removals.

### **Queue (FIFO)**
- **Usage**: Represents the player’s ammunition loader.
- **Implementation**: `self.munition = [0,0,0,0,1]` in `Jeu.py` (Class `Jeu`, method `Recommencer`).
- **Operations**: Managed in `Hero.py` (Class `Hero`, method `gestionTir`).
  - The first element is removed and added to the end of the queue.

### **Stack (LIFO)**
- **Usage**: Represents the player's lives.
- **Implementation**: `self.vie = [1,1,1]` in `Jeu.py` (Class `Jeu`, method `Recommencer`).
- **Operations**: Managed in `Hero.py` (Class `Hero`, method `changementVie`).
  - A `1` is added to gain a life, and a `1` is removed to lose a life.
 
## Credits
- **Quentin FRUME**: Design and artwork.
- **Quentin FRUME**: Music composition.
- **Thibaud DAUBIGNEY**: Various game mechanics, including ammunition system.
- **Olivier MERMET**: Idea for player teleportation at screen edges.

Thank you for playing Earth Invader! We hope you enjoy the experience!
