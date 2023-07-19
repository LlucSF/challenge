class Rod:
    """
    Class to handle all movements and proprieties of the rod
    """

    def __init__(self, center_position=[1, 2], horizontal=True):
        self.center_position = center_position  # List with the position of the central block of the rod (always [1, 2] with walls)
        self.horizontal = horizontal  # Bool indicating the rod direction. True -> horizontal
        self.state = self.center_position + [self.horizontal]  # State of the rod used in the A* network

        # Dictionary to easily implement changes in state
        self.state_changes_dict = {"up": [-1, 0, False],
                                   "down": [+1, 0, False],
                                   "left": [0, -1, False],
                                   "right": [0, +1, False],
                                   "rotate": [0, 0, True]}

    def get_all_positions(self):
        """
        Function to get the position of each block.
        """
        if self.horizontal:
            sideA_position = self.center_position.copy()
            sideA_position[1] -= 1

            sideB_position = self.center_position.copy()
            sideB_position[1] += 1
        else:
            sideA_position = self.center_position.copy()
            sideA_position[0] -= 1

            sideB_position = self.center_position.copy()
            sideB_position[0] += 1
        return [sideA_position, self.center_position, sideB_position]

    def change_state(self, state_change_key):
        """
        Function to implement a state change using the dictionary of state changes.
        """
        change = self.state_changes_dict[state_change_key]
        self.center_position[0] = self.center_position[0]+change[0]
        self.center_position[1] = self.center_position[1]+change[1]
        if change[2]:
            self.horizontal = not self.horizontal
        self.state = self.center_position + [self.horizontal]
