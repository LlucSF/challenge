from labyrinth import Labyrinth
from rod import Rod


class GameEngine:
    """
    Class to handle all functionalities of the labyrinth gameArea
    """

    def __init__(self, gameArea):
        self.labyrinth = Labyrinth(gameArea)
        self.rod = Rod()
        self.solution_queue = []
        self.graph = []

    def solve_game(self):
        self.labyrinth.show_game_area()
        self.labyrinth.show_game_area_with_rod(self.rod)
        self.labyrinth.check_valid_position(self.rod)
