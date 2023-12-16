from time import time

def read_file(name):

    return [line for line in open(name).read().split("\n")]

def parse_vertical(rocks):
    verticals = []
    for i in range(0,len(rocks[0])):
        verticals.append(''.join([rock[i] for rock in rocks])[::-1])
    return verticals

def make_chunks(rock):
    chunks = []
    skip = -1
    for i, each in enumerate(rock):
        if i >= skip:
            if each != "#":
                step = 0
                contig = ''

                while i + step < len(rock) and rock[i + step] != "#":
                    contig = contig + rock[i + step]
                    step += 1
                chunks.append(contig)
                skip = i + step

            else:
                step = 0
                contig = ''

                while i + step < len(rock) and rock[i + step] == "#":
                    contig = contig + rock[i + step]
                    step += 1
                chunks.append(contig)
                skip = i + step
    return chunks

def load(rock):

    chunks = make_chunks(rock)
    weight = 0
    load = 0
    for chunk in chunks:
        rollers = chunk.count("O")
        weight += len(chunk)
        if rollers != 0:
            for r in range(0, rollers):
                load += weight - r
    return load

class Rock:
    def __init__(self, s, y, x):
        self.s = s
        self.y = y
        self.x = x

    def __repr__(self):
        return f'{self.s} Y: {self.y}, X: {self.x}'
    
    def east_west(self, other):
        return self.x < other.x
    
    def north_south(self, other):
        return self.x < other.x

class Roller(Rock):
    def __init__(self, s, y, x, lever):
        super().__init__(s, y, x)
        self.lever = lever

    @property
    def load(self):
        return self.y * self.lever

class Brick(Rock):
    def __init__(self, s, y, x):
        super().__init__(s, y, x)

    def east_west(self, other):
        return False
    
    def north_south(self, other):
        return False

class Pebble(Rock):
    def __init__(self, s, y, x):
        super().__init__(s, y, x) 

def make_objs(raw_rocks):
    obj_matrix = []
    for y, rocks in enumerate(raw_rocks):
        x_ax = []
        for x, rock in enumerate(rocks):
            if rock == "O":
                x_ax.append(Roller(rock, y, x, len(raw_rocks)))
            elif rock == "#":
                x_ax.append(Brick(rock, y, x))
            elif rock == ".":
                x_ax.append(Pebble(rock, y, x))
        obj_matrix.append(x_ax)

    return obj_matrix


def main():
    raw_rocks = read_file("code.txt")
    rocks = make_objs(raw_rocks)
    for rock in rocks:
        print()
        for r in rock:
            print(r.s, end = "")

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)