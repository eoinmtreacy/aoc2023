def read_file(name):
    f = open(name)
    times, records = f.readlines()
    times, records = [time for time in times.split()[1:]], [record for record in records.split()[1:]]
    time, record = int("".join(times)), int("".join(records))
    return time, record

def calc_dists(time):
    return [t * (time - t) for t in list(range(time + 1))]

def count_betters(dist, record):
    return len([d for d in dist if d > record])

def mulitply(list):
    total = 1
    for each in list: total *= each
    return total

def main():
    time, record = read_file("code.txt")
    print(time, record)

    print(count_betters(calc_dists(time), record))

    # print(mulitply([count_betters(dist, records[i]) for i, dist in enumerate(dists)]))

if __name__ == "__main__":
    main()
