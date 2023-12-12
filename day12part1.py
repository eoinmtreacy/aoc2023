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
    
    @property
    def perms(self):
        return len(self.groups), self.total
    
    def decision(self):
        step = 0
        contig = ''
        for i, each in enumerate(self.groups):
            if each == "?":
                contig = contig + each
            else:
                return contig

def main():
    lines = read_file("test.txt")
    rows = create_rows(lines)
    for row in rows:
        print(row.decision())

if __name__ == "__main__":
    main()
