def make_maps(name):
    # open file
    f = open(name)
    # read lines
    # split on "\n\n"
    chunks = f.read().split(f"\n\n")
    maps = [chunk.split(":")[1].split(f"\n") for chunk in chunks]
    
    # discard first el of each list except the first one

    for map in maps[1:]:
        if not map[0]: 
            map.pop(0)
    
    # construct 3-dimensional array from each map
    maps = [[numbers.split() for numbers in map] for map in maps]
    # convert to integers
    maps = [[[int(number) for number in line] for line in map] for map in maps]

    return maps[0][0], maps[1:]

def map_seeds(seeds, map):
    
    def return_new_seed(seed, map):
        # if in any map, return index of destination map else return seed number
        for line in map:
            dest, source, count = line[0], line[1], line[2]
            if source <= seed < count + source:
                step = seed - source
                seed = dest + step
                break
        return seed

    return [return_new_seed(seed, map) for seed in seeds]


def main():
    # seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc
    seeds, maps = make_maps("code.txt")
    print(seeds)

    for map in maps:
        print(seeds)
        seeds = map_seeds(seeds, map)

    print(seeds)
    print(min(seeds))

if __name__ == "__main__":
    main()
