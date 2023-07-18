class Rod:
    """
    Class to handle all movements of the rod
    """

    def __init__(self):
        self.center_position = [1, 2]  # The rod always starts in the top left corner and considering the walls
        self.horizontal = True
        self.movements_dict = {"up": [-1, 0],
                               "down": [1, 0],
                               "left": [0, -1],
                               "right": [0, 1]}

    def rotate(self):
        if self.horizontal:
            self.horizontal = False
        else:
            self.horizontal = True

    def move(self, key):
        self.center_position[0] += self.movements_dict[key][0]
        self.center_position[1] += self.movements_dict[key][1]
