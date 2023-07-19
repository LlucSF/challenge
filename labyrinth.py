import copy
from rod import Rod


class Labyrinth:
    """
    Class to handle all functionalities of the labyrinth game area
    """

    def __init__(self, game_area):
        """
        class constructor with the required structures to manage the game area
        """
        # First I will surround the gameArea with walls to avoid possible indexes out of list
        self.number_rows = len(game_area) + 2
        self.number_columns = len(game_area[0]) + 2
        self.game_area = [['#'] * self.number_columns for i1 in range(self.number_rows)]
        self.goal_square = [self.number_rows - 2, self.number_columns - 2]

        # Filling the desired gameArea inside the enlarged version with walls
        for row in range(1, self.number_rows - 1):
            for column in range(1, self.number_columns - 1):
                self.game_area[row][column] = game_area[row - 1][column - 1]

        # Checking the two possible end states (horizontally and vertically filling the goal square).
        self.end_states = []
        if self.check_valid_position(Rod(center_position=[self.number_rows - 3, self.number_columns - 2],
                                         horizontal=False)):
            self.end_states.append([self.number_rows - 3, self.number_columns - 2, False])

        if self.check_valid_position(Rod(center_position=[self.number_rows - 2, self.number_columns - 3],
                                         horizontal=True)):
            self.end_states.append([self.number_rows - 2, self.number_columns - 3, True])
        if len(self.end_states) == 0:
            exit("SEVERE LABYRINTH ERROR: Labyrinth without goal square!")

    def show_game_area(self):
        """
        function to print the game area
        """
        print("gameArea with walls")
        for row in self.game_area:
            print(row)

    def show_game_area_with_rod(self, rod):
        """
        function to print the game area including the rod as 'r'
        """
        print("gameArea with walls and rod")
        game_area_rod = copy.deepcopy(self.game_area)
        rod_positions = rod.get_all_positions()
        for block in rod_positions:
            game_area_rod[block[0]][block[1]] = "r"
        for row in game_area_rod:
            print(row, '  ')
        print('')

    def check_valid_position(self, rod):
        """
        function to check if a rod state is valid for the current labyrinth
        """
        rod_positions = rod.get_all_positions()
        for block in rod_positions:
            if self.game_area[block[0]][block[1]] == "#":
                return False
        return True
