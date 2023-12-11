from day10pipes import *

def read_file(name):
    f = open(name)
    return f.readlines()

def create_maze(lines):
    maze = []
    for y, line in enumerate(lines):
        x_axis = []
        for x, each in enumerate(line):
            if each == "|":
                tile = Vertical(x, y, each)
            elif each == "-":
                tile = Horizontal(x, y, each)
            elif each == "L":
                tile = North_East(x, y, each)
            elif each == "J":
                tile = North_West(x, y, each)
            elif each == "7":
                tile = South_West(x, y, each)
            elif each == "F":
                tile = South_East(x, y, each)
            elif each == ".":
                tile = Ground(x, y, each)
            elif each == "S":
                tile = Start(x, y, each)
            x_axis.append(tile)
        maze.append(x_axis)
    return maze

def main():
    lines = read_file("test.txt")
    maze = create_maze(lines)
    
    for m in maze:
        for each in m:
            if each.s == "S":
                for option in each.find_options(maze):
                    print(option)

if __name__ == "__main__":
    main()
