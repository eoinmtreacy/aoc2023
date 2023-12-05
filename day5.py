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

    return maps


# for each seed in list

# if in any map, return index of destination map else return seed number

# if location > closest, closest = location

def main():
    make_maps("code.txt")
    seeds, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2hum, hum2loc = make_maps("code.txt")

if __name__ == "__main__":
    main()