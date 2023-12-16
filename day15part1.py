from time import time

class Hash:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.label} {self.operator} {self.focal_length} {self.box_number}'

    @property
    def box_number(self):
        total = 0
        for char in self.name.split("=")[0].split("-")[0]:
            total += ord(char)
            total *= 17
            total = total % 256
        return total
    
    @property
    def label(self):
        return self.name.split("=")[0].split("-")[0]
    
    @property
    def focal_length(self):
        return self.name[-1] if self.operator == "=" else False
        
    @property
    def operator(self):
        return "=" if "=" in self.name else "-"

class Box:
    def __init__(self, name):
        self.name = name
        self.lenses = []

    def __repr__(self):
        return f'Box {self.name}: {[lens.name + " " + lens.power for lens in self.lenses]}, Power: {self.focusing_power}'
    
    @property
    def focusing_power(self):
        return (self.name + 1) * sum([(l + 1) * int(lens.power) for l, lens in enumerate(self.lenses)])
# 256 boxes numbered 0 to 255
    
class Lens:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __eq__(self, other):
        return self.name == other.name
    
    def __repr__(self):
        return f'{self.name} {self.power}'
    
# 9 lens ordered 1 to 9
    
# for each hash, identify the label, the box number and the focal length

def parse_hashes(boxes, hashes):

    for hash in hashes:
        new_lens = Lens(hash.label, hash.focal_length)

        if hash.operator == "-":
            boxes[hash.box_number].lenses = list(filter(lambda x : hash.label != x.name, boxes[hash.box_number].lenses))

        elif new_lens not in boxes[hash.box_number].lenses:
            boxes[hash.box_number].lenses.append(new_lens)

        else:
            for lens in boxes[hash.box_number].lenses:
                if lens == new_lens:
                    boxes[hash.box_number].lenses[boxes[hash.box_number].lenses.index(lens)] = new_lens

        print(new_lens)

def main():
    hashes = [Hash(hash) for hash in open("code.txt").read().split(",")]
    boxes = [Box(i) for i in range(256)]
    parse_hashes(boxes, hashes)
    print(sum([box.focusing_power for box in boxes]))

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)