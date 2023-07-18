import copy

from rod import Rod


class Labyrinth:
    """
    Class to handle all functionalities of the labyrinth gameArea
    """

    def __init__(self, gameArea):
        """
        class constructor with the required structures to manage the gameArea
        """
        # First I will surround the gameArea with walls to avoid possible indexes out of list
        self.number_rows = len(gameArea) + 2
        self.number_columns = len(gameArea[0]) + 2
        self.gameArea = [['#'] * self.number_columns for i1 in range(self.number_rows)]
        self.goal_square = [self.number_rows - 2, self.number_columns - 2]

        # Filling the desired gameArea inside the enlarged version with walls
        for row in range(1, self.number_rows - 1):
            for column in range(1, self.number_columns - 1):
                self.gameArea[row][column] = gameArea[row - 1][column - 1]

        self.end_states = []
        if self.check_valid_position(Rod(center_position=[self.number_rows - 3, self.number_columns - 2],
                                         horizontal=False)):
            self.end_states.append([self.number_rows - 3, self.number_columns - 2, False])

        if self.check_valid_position(Rod(center_position=[self.number_rows - 2, self.number_columns - 3],
                                         horizontal=True)):
            self.end_states.append([self.number_rows - 2, self.number_columns - 3, True])
        if len(self.end_states) == 0:
            exit("BIG LABYRINTH ERROR: Labyrinth without the goal square!")

    def show_game_area(self):
        print("gameArea with walls")
        for row in self.gameArea:
            print(row)

    def show_game_area_with_rod(self, rod):
        print("gameArea with walls and rod")
        gameArea_rod = copy.deepcopy(self.gameArea)
        rod_positions = rod.get_all_positions()
        for block in rod_positions:
            gameArea_rod[block[0]][block[1]] = "r"

        for row in gameArea_rod:
            print(row)
        print("\n")

    def check_valid_position(self, rod):
        rod_positions = rod.get_all_positions()
        for block in rod_positions:
            if self.gameArea[block[0]][block[1]] == "#":
                return False
        return True
