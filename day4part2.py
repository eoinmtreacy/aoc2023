# open file
# read lines
# split line into two list: winning number i have

import time

def read_lines(name):
    f = open(name)
    lines = f.readlines()
    numbers = [line.split(":")[1][:-1] for line in lines]
    winners, have = [number.split("|")[0] for number in numbers], [number.split("|")[1] for number in numbers]
    winners, have = [win.split() for win in winners], [h.split() for h in have]
    return len(winners), winners, have

def count_winners(index, winners, have):
    # initialise new scratchies array
    max = len(winners)
    count = 0
    if index < max:
        for each in have[index]:
            if each in winners[index]:
                count += 1

    if not count:
        return count
    else:
        # print(count)
        return count + sum([count_winners(x, winners, have) for x in range(index + 1, index + count + 1)])

def main():
    start = time.time()
    index, winners, have = read_lines('code.txt')
    total = 0
    for i in range(index):
        inc = count_winners(i, winners, have)
        total += inc
    total += index
    print(total)
    end = time.time()
    print(end - start)

main()