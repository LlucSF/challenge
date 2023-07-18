class Labyrinth:
    """
    Class to handle all functionalities of the labyrinth gameArea
    """

    def __init__(self, gameArea):
        """
        class constructor defining required structures to manage the gameArea
        """
        # First I will surround the gameArea with walls to avoid possible indexes out of list
        self.number_rows = len(gameArea) + 2
        self.number_columns = len(gameArea[0]) + 2
        self.gameArea = [['#'] * self.number_columns for i1 in range(self.number_rows)]
        self.goal_square = [self.number_rows - 2, self.number_columns - 1]

        # Filling the desired gameArea inside the enlarged version with walls
        for row in range(1, self.number_rows - 1):
            for column in range(1, self.number_columns - 1):
                self.gameArea[row][column] = gameArea[row - 1][column - 1]

    def show_game_area(self):
        print("\ngameArea with walls")
        for row in self.gameArea:
            print(row)

    def show_game_area_with_rod(self, rod):
        print("\ngameArea with walls and rod")
        gameArea_rod = self.gameArea
        if rod.horizontal:
            gameArea_rod[rod.center_position[0]][rod.center_position[1]-1] = 'r'
            gameArea_rod[rod.center_position[0]][rod.center_position[1]] = 'r'
            gameArea_rod[rod.center_position[0]][rod.center_position[1]+1] = 'r'
        else:
            gameArea_rod[rod.center_position[0]-1][rod.center_position[1]] = 'r'
            gameArea_rod[rod.center_position[0]][rod.center_position[1]] = 'r'
            gameArea_rod[rod.center_position[0]+1][rod.center_position[1]] = 'r'

        for row in gameArea_rod:
            print(row)

    def check_valid_position(self, rod):
        if rod.horizontal:
            if ((self.gameArea[rod.center_position[0]][rod.center_position[1]] == "#") or
                    (self.gameArea[rod.center_position[0]][rod.center_position[1] + 1] == "#") or
                    (self.gameArea[rod.center_position[0]][rod.center_position[1] - 1] == "#")):
                print('Invalid position!')
                return False
            else:
                print('Valid position!')
                return True
        else:
            if ((self.gameArea[rod.center_position[0]][rod.center_position[1]] == "#") or
                    (self.gameArea[rod.center_position[0] + 1][rod.center_position[1]] == "#") or
                    (self.gameArea[rod.center_position[0] - 1][rod.center_position[1] - 1] == "#")):
                print('Invalid position!')
                return False
            else:
                print('Valid position!')
                return True
