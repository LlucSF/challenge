class Node:
    """
    A node class for A* Pathfinding including a rod instance
    """

    def __init__(self, parent=None, state=None, rod=None):
        self.parent = parent
        self.state = state
        self.rod = rod

        # Parameters for the A* algorithm
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        """
        defining the '==' operator between Node instances
        """
        return self.state == other.state