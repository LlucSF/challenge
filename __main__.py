from gameEngine import GameEngine

labyrinth1 = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
              ["#", ".", ".", ".", "#", ".", ".", ".", "."],
              [".", ".", ".", ".", "#", ".", ".", ".", "."],
              [".", "#", ".", ".", ".", ".", ".", "#", "."],
              [".", "#", ".", ".", ".", ".", ".", "#", "."]]

labyrinth2 = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
              ["#", ".", ".", ".", "#", ".", ".", "#", "."],
              [".", ".", ".", ".", "#", ".", ".", ".", "."],
              [".", "#", ".", ".", ".", ".", ".", "#", "."],
              [".", "#", ".", ".", ".", ".", ".", "#", "."]]

labyrinth3 = [[".", ".", "."],
              [".", ".", "."],
              [".", ".", "."]]

labyrinth4 = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
              [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", "#", ".", ".", ".", "#", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

labyrinths = [labyrinth1, labyrinth2, labyrinth3, labyrinth4]
labyrinths_moves = []

for labyrinth in labyrinths:
    print('\n*********** Game Starts! ***********  ')
    print('Labyrinth to solve:  ')
    for row in labyrinth:
        print(row, '  ')
    print('')
    myGameEngine = GameEngine(game_area=labyrinth, verbose=False)  # Instancing a GameEngine to solve the labyrinth
    labyrinths_moves.append(myGameEngine.solve_game())
print('\n|||| Test results for all labyrinths: {} ||||  '.format(labyrinths_moves))