# open file
# read lines
# split line into two list: winning number i have
def read_lines(name):
    f = open(name)
    lines = f.readlines()
    numbers = [line.split(":")[1][:-1] for line in lines]
    winners, have = [number.split("|")[0] for number in numbers], [number.split("|")[1] for number in numbers]
    winners, have = [win.split() for win in winners], [h.split() for h in have]
    return winners, have


def count_winners(winners, have):
    # initialise total
    total = 0

    # for each number in my numbers, if number in winnings numbers, count += 1
    for i, line in enumerate(have):
        count = -1
        for number in line:
            if number in winners[i]:
                count += 1

        # sum of each line = 2**count
        # add sum of each line to total
        if count > -1:
            total += 2**count
            print(2**count)
        
    return total

def main():
    winners, have = read_lines('code.txt')
    print(count_winners(winners, have))
    
main()