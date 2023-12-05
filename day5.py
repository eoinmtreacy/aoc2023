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
            source = list(range(line[1], line[1] + line[2]))
            dest = list(range(line[0], line[0] + line[2]))
            if seed in source:
                # TODO add more efficient in range check
                seed = dest[source.index(seed)]
                break
        return seed

        # for each seed in list

    return [return_new_seed(seed, map) for seed in seeds]


def main():
    make_maps("code.txt")
    # seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc
    seeds, maps = make_maps("code.txt")
    print(seeds)

    # for map in maps:
    #     seeds = map_seeds(seeds, map)

    print(min(seeds))
    # if location > closest, closest = location

if __name__ == "__main__":
    main()