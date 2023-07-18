from gameEngine import GameEngine

labyrinth = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["#", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."]]

print('\nOriginal Labyrinth')
for row in labyrinth:
    print(row)

myGameEngine = GameEngine(gameArea=labyrinth)
myGameEngine.solve_game()
