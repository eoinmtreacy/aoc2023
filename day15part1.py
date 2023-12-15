from time import time

class Hash:
    def __init__(self, name):
        self.name = name

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
        pass
        
    
    @property
    def operator(self):
        return "=" if "=" in self.name else "-"

class Box:
    def __init__(self, name):
        self.name = name
        self.lenses = []

    def __repr__(self):
        return f'Box {self.name}:'
    
# 256 boxes numbered 0 to 255
    
class Lens:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __eq__(self, other):
        return self.name == other.name
    
# 9 lens ordered 1 to 9
    
# for each hash, identify the label, the box number and the lens number

def main():
    hashes = [Hash(hash) for hash in open("test.txt").read().split(",")]
    boxes = [Box(i) for i in range(256)]
    for hash in hashes:
        print(hash.box_number)

if __name__ == "__main__":
    start = time()
    main()
    print(time() - start)