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
        self.dist_list = []

    def __repr__(self):
        return f'{self.loc}'

    def dist(self, other):
        dist = abs(self.loc[0] - other.loc[0]) + abs(self.loc[1] - other.loc[1])
        self.dist_list.append(dist)
        return dist

def create_galaxies(map):
    galaxies = []
    for y, m in enumerate(map):
        for x, each in enumerate(m):
            if each != ".":
                galaxies.append(Galaxy(y, x))
    return galaxies

def sum_dists(galaxies):
    total = 0
    for galaxy in galaxies:
        total += sum([galaxy.dist(each) for each in galaxies])
    return total/2

def sum_diff(galaxies, expanded):
    total = 0
    for i, galaxy in enumerate(galaxies):
        for d in range(len(galaxy.dist_list)):
            total += (expanded[i].dist_list[d] - galaxy.dist_list[d]) / 2
    return total

def main():

    MILLION = 1000000

    f = open("code.txt")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]

    galaxies = create_galaxies(lines)

    expanded_map = expand(lines)
    expanded_galaxies = create_galaxies(expanded_map)

    for i,g in enumerate(galaxies):
        new_loc = (((expanded_galaxies[i].loc[0] - g.loc[0]) * 999999) + g.loc[0], ((expanded_galaxies[i].loc[1] - g.loc[1]) * 999999) + g.loc[1])
        g.loc = new_loc
    
    print(sum_dists(galaxies))
    # print(sum_diff(galaxies, expanded_galaxies) * 999999 + sum_dists(galaxies))

if __name__ == "__main__":
    main()

# 447,745,088,302 too high
# 447,736,000,000 too high
# 447,744,640,566 == dists * 999,999
# 198,408,337,639 too low