from time import time

def read_file(name):
    
    return [[c for c in chunk.split("\n")] for chunk in open(name).read().split("\n\n")]

def parse_vertical(sands):
    verticals = []
    for i in range(0,len(sands[0])):
        verticals.append(''.join([sand[i] for sand in sands])[::-1])
    return verticals

def count_rows(sands, multiplier=100):
    # check horizontal
    current = ''
    for s, sand in enumerate(sands):
        if sand == current:
            if all([sands[s-1-i] == sands[s+i] if s-1-i > 0 and s + i < len(sands) else True for i in range(0, len(sands))]):
                return s * multiplier
        else:
            current = sand
    
    return 0 if multiplier == 1 else count_rows(parse_vertical(sands), 1)

def main():
    sand_maps = read_file("test.txt")
    print(sum([count_rows(sands) for sands in sand_maps]))

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)

# 34768 too high
# 30593 too high
# 27191 not right
# 22977 too low
