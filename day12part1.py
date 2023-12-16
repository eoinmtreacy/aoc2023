import itertools
import time

def read_file(name):
    f = open(name)
    return f.readlines()

def create_rows(lines):
    return [Row(line) for line in lines]

class Row:
    def __init__(self, line):
        self.groups = line.split()[0]
        self.numbers = [int(number) for number in line.split()[1].split(",")]
        self.total = sum(self.numbers)

    def __repr__(self):
        return f'{self.groups} {self.numbers}'
    
    def chunks(self, perm):
        chunks = []
        skip = -1
        for i, each in enumerate(perm):
            if i > skip:
                if each == "#":
                    step = 0
                    contig = ''

                    while i + step < len(perm) and perm[i + step] == "#":
                        contig = contig + perm[i + step]
                        step += 1
                    chunks.append(contig)
                    skip = i + step
        return chunks
    
    @property
    def perms(self):
        chars = '#.'
        perms = []
        for p in map(iter, itertools.product(chars, repeat=self.groups.count('?'))):
            perms.append(''.join(c if c != '?' else next(p) for c in self.groups))
        return perms
    
    @property
    def valid_perms(self):
        count = 0
        for perm in self.perms:
            valid = True
            chunks = self.chunks(perm)

            if len(chunks) == len(self.numbers):
                for c, chunk in enumerate(chunks):
                    if len(chunk) != self.numbers[c]:
                        valid = False 
                        break
            else:
                valid = False

            if valid: 
                count += 1
        return count


def main():
    lines = read_file("code.txt")
    rows = create_rows(lines)
    print(sum([row.valid_perms for row in rows]))

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)

# 7175 too high 