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

def gen_seed_ranges(seeds):
    total = 0
    for i in range(0,len(seeds), 2):
        total += (seeds[i] + seeds[i + 1]) - seeds[i]
    print(total)

    seed_ranges = []
    for i in range(0,len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i + 1]])

    seed_ranges.sort(key = lambda x : x[0])
    return seed_ranges, total

def return_new_seed(seed, map):
    # if in any map, return index of destination map else return seed number
    for line in map:
        dest, source, count = line[0], line[1], line[2]
        if source <= seed < count + source:
            step = seed - source
            seed = dest + step
            break
    return seed

def main():
    # seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc
    seeds, maps = make_maps("code.txt")
    seed_ranges, total = gen_seed_ranges(seeds)

    print (seed_ranges)
    closest = 0
    count = 0

    for seeds in seed_ranges:   
        for seed in range(seeds[0], seeds[1]):
            for map in maps:
                seed = return_new_seed(seed, map)
                count += 1
            if count % 1000000 == 0:
                    print(count/total)
            if seed < closest or closest == 0:
                closest = seed

    print(closest)

if __name__ == "__main__":
    main()
