def expand(map):
    # expand horizontally
    skip_index = -1
    for i, m in enumerate(map):
        if i != skip_index:
            empty_h = True
            for each in m:
                if each != ".":
                    empty_h = False
                    break
            if empty_h:
                map.insert(i, "." * (len(m)))
                skip_index = i + 1
    
    # expand vertically
    skip_index = -1
    for i in range(len(map[0]) + 1):
        if i != skip_index:
            empty_v = True
            for m in map:
                if m[i] != ".":
                    empty_v = False
                    break
            if empty_v:
                map = [m[:i] + "." + m[i:] for m in map]
                skip_index = i + 1

    return map

class Galaxy:
    def __init__(self, y, x):
        self.loc = (y, x)

    def __repr__(self):
        return f'{self.loc}'

    def dist(self, other):
        return abs(self.loc[0] - other.loc[0]) + abs(self.loc[1] - other.loc[1])

def create_galaxies(map):
    galaxies = []
    for y, m in enumerate(map):
        for x, each in enumerate(m):
            if each != ".":
                galaxies.append(Galaxy(y, x))
    return galaxies

def main():
    f = open("code.txt")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]

    map = expand(lines)
    galaxies = create_galaxies(map)

    total = 0
    for galaxy in galaxies:
        total += sum([galaxy.dist(each) for each in galaxies])
    print(total/2)

if __name__ == "__main__":
    main()