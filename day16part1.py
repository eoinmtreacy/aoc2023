from time import time

class Tile:
    def __init__(self, name, y, x):
        self.name = name
        self.y = y
        self.x = x
        self.visited = False
        self.vectors = []

    def __repr__(self):
        return f'{self.name} Y: {self.y}, X: {self.x} {self.visited}'
    
    def add_vector(self, visitor):
        if (visitor.velocity) not in self.vectors:
            self.vectors.append(visitor.velocity)
            return True
        else:
            return False
        
    def affect_vector(self, other):
        return other.velocity
    
class Beam(Tile):
    def __init__(self, name, y, x, velocity):
        super().__init__(name, y, x)
        self.velocity = velocity
        self.active = True

    def __repr__(self):
        return f'{self.name} {self.y}, {self.x} {"Active" if self.active else "Inactive"}'

class Vert(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def affect_vector(self, other):
        if other.velocity == (0, 1) or other.velocity == (0, -1):
            return (-1, 0)
        else:
            return other.velocity

class Horz(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, y, x)

    def affect_vector(self, other):
        if other.velocity == (1, 0) or other.velocity == (-1, 0):
            return (0, -1)
        else:
            return other.velocity

class Forw(Tile):
    def __init__(self, name, y, x):
        super().__init__(name, y, x)

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
        super().__init__(name, y, x)

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
        super().__init__(name, y, x)

def parse_matrix(matrix):
    tiles = []
    for y, row in enumerate(matrix):
        x_axis = []
        for x, each in enumerate(row):
            if each == "|":
                new = Vert(each, y, x)
            elif each == "-":
                new = Horz(each, y, x)
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
        if not any([beam.active for beam in beams]):
            break
        else:
            # for each beam, check current tile
            for beam in list(filter(lambda x : x.active, beams)):

            # if not visited, tile.visited = True, tile.vectors(visitor)
                if beam.y < 0 or beam.x < 0 or beam.y >= len(matrix) or beam.x >= len(matrix[0]):
                    beam.active = False
                    break

                current = matrix[beam.y][beam.x]
                if beam.velocity in current.vectors:
                    beam.active = False

                else:
                    current.vectors.append(beam.velocity)
                    current.visited = True
                    
                    # if tile.name = "|", beams.append(Beam going south)

                    if current.name == "|" and (beam.velocity == (0,1) or beam.velocity == (0,-1)):
                        beams.append(Beam("beam", current.y + 1, current.x, (1, 0)))

                    # elif tile.name = "-", beams.append(Beam going west)
                    elif current.name == "-" and (beam.velocity == (1,0) or beam.velocity == (-1, 0)):
                        beams.append(Beam("beam", current.y, current.x + 1, (0, 1)))

                    # tile.affect_vector(visitor)
                    beam.velocity = current.affect_vector(beam)
                    
                    # increment beam
                    beam.y += beam.velocity[0]
                    beam.x += beam.velocity[1]
    print(beams)
    return matrix


def main():
    matrix = open("test.txt").read().split("\n")
    parsed_matrix = parse_matrix(matrix)
    traversed_matrix = traverse_matrix([Beam("beam", 0, 0, (0, 1))], parsed_matrix)
    for t in traversed_matrix:
        print()
        for each in t:
            print("#" if each.visited else ".", end="")

    # print(sum([sum([1 if tile.visited else 0 for tile in row]) for row in traversed_matrix]))

if __name__ == "__main__":
    start = time()
    main()
    # print(time() - start)