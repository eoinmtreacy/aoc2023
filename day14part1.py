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

def main():
    raw_rocks = read_file("code.txt")
    rocks = parse_vertical(raw_rocks)
    print(sum([load(rock) for rock in rocks]))

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)