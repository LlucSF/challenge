from labyrinth import *
from node import *
from typing import List


class GameEngine:
    """
    Class to handle all functionalities of the labyrinth gameArea
    """

    def __init__(self, game_area: List, verbose=False):
        """
           :param List game_area: List that contains the labyrinth
           :param Bool verbose: Flag to produce output more information on the computations
        """
        self.labyrinth = Labyrinth(game_area)
        self.rod = Rod()
        self.starting_state = self.rod.center_position + [self.rod.horizontal]
        self.verbose = verbose

    def solve_game(self):
        """
        Function to solve the game problem
        """
        self.labyrinth.show_game_area_with_rod(self.rod)
        path_list = []
        for end_state in self.labyrinth.end_states:
            path_list.append(self.astar(start_state=self.starting_state, end_state=end_state))

        if path_list[0] == -1:
            print("Maze without a solution!")
            return -1
        else:
            path_len = []
            for path in path_list:
                path_len.append(len(path) - 1)
            min_path = min(path_len)
            print("Maze solved. Minimum number of transformations is: {}".format(min_path))
            return min_path

    def astar(self, start_state: List, end_state: List):
        """
        Implementation of the A* algorithm. Returns a list as a path from the given start_state to the given end_state.
        """
        # State counter for verbose output
        state_counter = 0

        # Create start and end node
        start_node = Node(parent=None, state=start_state, rod=self.rod)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(parent=None, state=end_state)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.state)
                    current = current.parent
                return path  # Return reversed path

            # Generate children
            children = []
            for new_position in current_node.rod.state_changes_dict.keys():  # Using the dictionary with all transformations
                # Creating a new rod using the current-node's rod and applying the new position transformation
                children_rod = copy.deepcopy(current_node.rod)

                # Creating new state using the dictionary keyword
                children_rod.change_state(new_position)

                # Make sure is a valid transformation before continuing
                if not self.labyrinth.check_valid_position(children_rod):
                    continue

                # Print game area with rod in case of verbose
                state_counter += 1
                if self.verbose:
                    print('Showing node iteration {} with transformation: {}'.format(state_counter, new_position))
                    self.labyrinth.show_game_area_with_rod(children_rod)

                # Create new node using the confirmed rod
                new_node = Node(parent=current_node, state=children_rod.state, rod=children_rod)

                # Append children
                children.append(new_node)

            # Loop through children
            for child in children:
                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        break
                else:
                    # Create the f, g, and h values
                    child.g = current_node.g + 1
                    # H: Manhattan distances to end point
                    child.h = abs(child.state[0] - end_node.state[0]) + abs(
                        child.state[1] - end_node.state[1])
                    child.f = child.g + child.h

                    # Child is already in the open list
                    for open_node in open_list:
                        # check if the new path to children is worst or equal
                        # than one already in the open_list (by measuring g)
                        if child == open_node and child.g >= open_node.g:
                            break
                    else:
                        # Add the child to the open list
                        open_list.append(child)
        return -1
