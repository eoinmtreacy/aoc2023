# open file
# read lines
# split line into two list: winning number i have
def read_lines(name):
    f = open(name)
    lines = f.readlines()
    numbers = [line.split(":")[1][:-1] for line in lines]
    winners, have = [number.split("|")[0] for number in numbers], [number.split("|")[1] for number in numbers]
    winners, have = [win.split() for win in winners], [h.split() for h in have]
    return [x for x in range(len(winners))], winners, have

def count_winners(index, winners, have):
    # initialise new scratchies array
    count = 0
    for each in have:
        if each in winners:
            count += 1

    if not count:
        return count
    else:
        return count + sum([count_winners(x) for x in range(count)])

def main():
    index, winners, have = read_lines('test.txt')
    
main()