Project to solve a specific kinf of maze problem involving rods. 
The problem has been solved usin Python and OOP, splitting the game elements into Rod, Labyrinth, Node and gameEngine, and using only the basics of the lagnuage.

The strategy followed consisted in:  
 1- surrounding the maze with walls to prevent problems with indexes when moving  
 2- determining the (usually) two winning positions (one horizontal + one vertical)  
 3- using A* assisted by the rules of the movements  
 4- getting the smallest paths between the winning positions  

ANSWER DIRECTLY FROM TERMINAL:

*********** Game Starts! ***********  

Labyrinth to solve:  
['.', '.', '.', '.', '.', '.', '.', '.', '.']  
['#', '.', '.', '.', '#', '.', '.', '.', '.']  
['.', '.', '.', '.', '#', '.', '.', '.', '.']  
['.', '#', '.', '.', '.', '.', '.', '#', '.']  
['.', '#', '.', '.', '.', '.', '.', '#', '.']  


gameArea with walls and rod  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  
['#', 'r', 'r', 'r', '.', '.', '.', '.', '.', '.', '#']  
['#', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#']  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  


Maze solved. Minimum number of transformations is: 11  

*********** Game Starts! ***********   

Labyrinth to solve:   
['.', '.', '.', '.', '.', '.', '.', '.', '.']  
['#', '.', '.', '.', '#', '.', '.', '#', '.']  
['.', '.', '.', '.', '#', '.', '.', '.', '.']  
['.', '#', '.', '.', '.', '.', '.', '#', '.']  
['.', '#', '.', '.', '.', '.', '.', '#', '.']  


gameArea with walls and rod  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  
['#', 'r', 'r', 'r', '.', '.', '.', '.', '.', '.', '#']
['#', '#', '.', '.', '.', '#', '.', '.', '#', '.', '#']  
['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#']  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  


Maze without a solution!  

*********** Game Starts! ***********  

Labyrinth to solve:  
['.', '.', '.']  
['.', '.', '.']  
['.', '.', '.']  


gameArea with walls and rod  
['#', '#', '#', '#', '#']  
['#', 'r', 'r', 'r', '#']  
['#', '.', '.', '.', '#']  
['#', '.', '.', '.', '#']  
['#', '#', '#', '#', '#']  


Maze solved. Minimum number of transformations is: 2  

*********** Game Starts! ***********  

Labyrinth to solve:  
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '#', '.', '.', '.', '.', '#', '.', '.', '.']  
['.', '#', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '#', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '#', '.', '.', '.', '#', '.', '.', '.', '.']  
['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']  
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  


gameArea with walls and rod  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  
['#', 'r', 'r', 'r', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#']  
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  


Maze solved. Minimum number of transformations is: 16  