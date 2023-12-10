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
        unique = len(set(self.cards))

        if unique == 1:
            return 7 # 5 of a kind
        if "J" in self.cards:
            if self.jacks == 4:
                return 7 # 5 of a kind
            elif self.jacks == 3 and unique == 2:
                return 7 # 5 of a kind
            elif self.jacks == 3 and unique == 3:
                return 6 # 4 of a kind
            elif self.jacks == 2 and unique == 2:
                return 7 # 5 of a kind
            elif self.jacks == 2 and unique == 3:
                return 6 # 4 of a kind
            elif self.jacks == 2 and unique == 4:
                return 4 # 3 of a kind
            elif self.jacks == 1 and unique == 2:
                return 7 # 5 of a kind
            elif self.jacks == 1 and unique == 3:
                if max(self.frequency.values()) == 3:
                    return 6 # 4 of a kind
                else:
                    return 5 # full house
            elif self.jacks == 1 and unique == 4:
                return 4 # 3 of a kind 
            elif self.jacks == 1 and unique == 5:
                return 2 # pair
        else:
            if unique == 1:
                return 7
            elif unique == 2:
                if max(self.frequency.values()) == 4:
                    return 6
                else:
                    return 5
            elif unique == 3:
                if max(self.frequency.values()) == 3:
                    return 4 # 3 of kind
                else:
                    return 3 # 2 pair
            elif unique == 4:
                return 2 # 1 pair
            else:
                return 1 # high card

    def __gt__(self, other):

        if self.strength > other.strength:
            return True
        elif self.strength < other.strength:
            return False

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
    hands = read_file("code.txt")
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
# 247899739 not right 