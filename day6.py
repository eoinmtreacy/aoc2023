def read_file(name):
    f = open(name)
    times, records = f.readlines()
    times, records = [int(time) for time in times.split()[1:]], [int(record) for record in records.split()[1:]]
    return times, records

def calc_dists(time):
    return [t * (time - t) for t in list(range(time + 1))]

def count_betters(dist, record):
    return len([d for d in dist if d > record])

def mulitply(list):
    total = 1
    for each in list: total *= each
    return total

def main():
    times, records = read_file("code.txt")
    dists = [calc_dists(time) for time in times]

    for i, dist in enumerate(dists):
        print(count_betters(dist, records[i]))

    print(mulitply([count_betters(dist, records[i]) for i, dist in enumerate(dists)]))

if __name__ == "__main__":
    main()
