# OBJECTTIVE
The game must simulate a basic version of jetpack joyride. We need to defend the boss before the time specifies.The objective of the game is to collect as many coins as possible, fight the obstacles on the way, defeat the boss enemy and rescue Baby Yoda.

# RUNNING THE GAME
```
python3 is required 
python3 run.py
```

# FEATURES
- The game is implemented in Python3
- The code is modular and follows PEP8 standards
- Uses only core Python3 packages
- Player can move right, left, fly, shoot, use shield
- Obstacles are placed in between.
- Power Boosters appear in between to increase the game speed
- You can shoot the fire beam and boss enemy
- Colors are implemented using colorama library
- After the game finishes, final score is printed

# MOVEMENT
- a - Moves Backward
- d - Moves Forward
- w - Fly
- s - Implements shield
- b - Shoots the bullet

# OOPS CONCEPT
- #### Inheritance
    - Mando(player) and Enemy class inherit from the Person class
    - vertical, horizontal, slanting, coin class inherit from the Obstacle class
- #### Polymorphism
   - Placing the Mando and Enemy and with same name
- #### Encapsulation
    - Class and object based approach for all the functionality implemented
- #### Abstraction
    - Properties of the every class are hidden from the user using abstraction and used by getter-setter method

# OBSTACLES
- three types of firebeams , coins, magnet, power boosters, and boss enemy

# BACKGROUND AND SCENERY
- • The scenery and the obstacles must change as you move in and out of the window. There is a ground/platform and the sky, and the Mandalorian can’t go below the ground or above the sky.
