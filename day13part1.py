from time import time

def read_file(name):
    
    return [[c for c in chunk.split("\n")] for chunk in open(name).read().split("\n\n")]

def parse_vertical(sands):
    verticals = []
    for i in range(0,len(sands[0])):
        verticals.append(''.join([sand[i] for sand in sands])[::-1])
    return verticals

def count_rows(sands, multiplier=1):
    # check horizontal
    for s, sand in enumerate(sands):
        if sand in sands[s+1:]:
            current = sand
            count = 1
            for each in sands[s+1:]:
                if each == current:
                    count += 1
                    return(multiplier * count + s)
                else:
                    count += 1
                    current = each
    return 0


def main():
    sand_maps = read_file("test.txt")
    total = 0
    print(count_rows(sand_maps[0]))

if __name__ == "__main__":
    start = time()
    main()
    # print(time() - start)