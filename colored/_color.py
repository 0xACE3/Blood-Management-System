

class Color:

    def __init__(self, rgb_value):

        self.red = rgb_value[0]
        self.green = rgb_value[1]
        self.blue = rgb_value[2]

    def __repr__(self):
        return f"\033[38;2;{self.red};{self.green};{self.blue}m"


