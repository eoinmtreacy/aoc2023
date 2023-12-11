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

def traverse_maze(start, maze):
    # save origin
    origin = (start.x, start.y)
    # choose first option
    start.x, start.y = start.find_options(maze)[0].x, start.find_options(maze)[0].y
    count = 1
    # count ++

    # while start.x, start.y != origin
    while (start.x, start.y) != origin:
        for option in start.find_options(maze):
            if option.visited == False:
                option.visited = True
                print(option)
                start.x, start.y = option.x, option.y
                count += 1
                break

    return count

def main():
    lines = read_file("test.txt")
    maze = create_maze(lines)

    for m in maze:
        for each in m:
            if each.s == "S":
                start = each

    print(traverse_maze(start, maze))

if __name__ == "__main__":
    main()
