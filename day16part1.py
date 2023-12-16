from time import time

class Tile:
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x
        self.visited = False
        self.vectors = []

    def __repr__(self):
        return f'{self.name} Y: {self.y}, X: {self.x}'
    
    def add_vector(self, visitor):
        if (visitor.name, visitor.velocity) not in self.vectors:
            self.vectors.append(visitor.velocity)
            return True
        else:
            return False
        
    def affect_vector(self, other):
        return other.velocity
    
class Beam(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)
        self.velocity = (0,1)
        self.active = True

class Vert(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)

    def affect_vector(self, other):
        if other.velocity == (0, 1) or other.velocity == (0, -1):
            return (-1, 0)

class Horz(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)

    def affect_vector(self, other):
        if other.velocity == (1, 0) or other.velocity == (0, 1):
            return (0, -1)

class Forw(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)

    def affect_vector(self, other):
        if other.velocity == (0, 1):
            return (-1, 0)
        elif other.velocity == (1, 0):
            return (0, -1)
        elif other.velocity == (0, -1):
            return (1, 0)
        elif other.velocity == (-1, 0):
            return (0, 1)
        

class Back(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)

    def affect_vector(self, other):
        if other.velocity == (0, 1):
            return (-1, 0)
        elif other.velocity == (1, 0):
            return (0, -1)
        elif other.velocity == (0, -1):
            return (1, 0)
        elif other.velocity == (-1, 0):
            return (0, 1)

class Dot(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, x, y)

def parse_matrix(matrix):
    tiles = []
    for y, row in enumerate(matrix):
        x_axis = []
        for x, each in enumerate(row):
            if each == "|":
                new = Vert(each, y, x)
            elif each == "-":
                new == Horz(each, y, x)
            elif each == "/":
                new = Forw(each, y, x)
            elif each == "\\":
                new = Back(each, y, x)
            elif each == ".":
                new = Dot(each, y, x)
            x_axis.append(new)
        tiles.append(x_axis)
    return tiles

def traverse_matrix(beams, matrix):
    while True:
    # if at least some beams are active 
        if not all([beams.active for beam in beams]):
            # for each beam, check current tile
            for beam in beams:
            # if not visited, tile.visited = True, tile.vectors(visitor)
                current = matrix[beam.y][beam.x]
                if beam.velocity in current.vectors:
                    beam.active = False
                # tile.affect_vector(visitor)
                # if tile.name = "|", beams.append(Beam going south)
                # elif tile.name = "-", beams.append(Beam going west)
            # else beam.active = False
        else:
            break


def main():
    matrix = open("test.txt").read().split("\n")
    matrix = parse_matrix(matrix)
    print(matrix[0][0].__name__)

if __name__ == "__main__":
    start = time()
    main()
    # print(time() - start)