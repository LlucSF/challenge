import copy

from rod import *
class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, state=None, rod=None):
        self.parent = parent
        self.state = state
        self.rod = copy.deepcopy(rod)

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state