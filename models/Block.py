class Block:
    def __init__(self, width, height, coords):
        self.width = width
        self.height = height
        self.coords = coords

    def __str__(self):
        return f"[{self.width}, {self.height}, {self.coords}]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.width == other.width
                and self.height == other.height
                and self.coords == other.coords)

    def __ne__(self, other):
        return (self.width != other.width
                or self.height != other.height
                or self.coords != other.coords)