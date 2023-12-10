class Hand:
    def __init__(self, cards, bid):
        self.ranking = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        self.cards = cards
        self.bid = bid

    def __str__(self):
        return f'{self.cards} {self.bid}'

    @property
    def frequency(self):
        frequency = {}
        for card in self.cards:
            if card in frequency:
                frequency[card] += 1
            else: 
                frequency[card] = 1
        return frequency
    
    @property
    def jacks(self):
        count = 0
        for card in self.cards:
            if card == "J":
                count += 1
        return count
    
    @property
    def strength(self):
        items = sorted(list(self.frequency.items()), key = lambda x : x[1])
        print(items)

        if items[-1][0] == "J" and items[-1][1] != 5:
            strength = sorted(self.frequency.values())[1] + self.jacks
            if strength > 5:
                strength = 5
            return strength
        elif items[-1][0] == "J" and items[-1][1] == 5:
            return 5

        else:
            try:
                strength = sorted(self.frequency.values())[0] + self.jacks
                return strength
            except:
                return 5

    
    def __gt__(self, other):
        freq1, freq2 = sorted(list(self.frequency.values())), sorted(list(other.frequency.values()))

        if self.strength > other.strength:
            return True
        elif self.strength < other.strength:
            return False
        
        try:
            if freq1[-2] > freq2[-2]:
                return True
            elif freq1[-2] < freq2[-2]:
                return False
        except:
            for c, card in enumerate(self.cards):
                if self.ranking.index(card) > other.ranking.index(other.cards[c]):
                    return True
                elif self.ranking.index(card) < other.ranking.index(other.cards[c]):
                    return False
            return False

def read_file(name):
    f = open(name)
    lines = f.readlines()
    hands = [Hand(line.split()[0], line.split()[1]) for line in lines]
    return hands

def main():
    hands = read_file("test.txt")
    hands.sort()

    total = 0
    for i, hand in enumerate(hands):
        total += int(hand.bid) * (i + 1)
        print(i + 1, hand)
    print(total)

if __name__ == "__main__":
    main()

# 248066910 too high part 2 

# 248878724 too high
# 247262832 too low

# 247567454 not right 