from time import time

def read_file(name):

    return [line for line in open(name).read().split("\n")]

def parse_vertical(rocks):
    verticals = []
    for i in range(0,len(rocks[0])):
        verticals.append(''.join([rock[i] for rock in rocks])[::-1])
    return verticals

def load(rock):
    chunks = [r + "#" if "#" not in r else r for r in rock.split("#")]
    weight = 0
    load = 0
    for chunk in chunks:
        rollers = chunk.count("O")
        weight += len(chunk)
        if rollers != 0:
            for r in range(0, rollers):
                load += weight - r
    return load

def main():
    raw_rocks = read_file("test.txt")
    rocks = parse_vertical(raw_rocks)
    print(sum([load(rock) for rock in rocks]))

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)