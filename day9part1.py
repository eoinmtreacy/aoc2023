def read_file(name):
    f = open(name)
    lines = f.readlines()
    lines = [[int(each) for each in line.split()] for line in lines]
    return lines

class Line:
    def __init__(self, line):
        self.reading = line
        self.intervals = self.calc_intervals()
    
    def __repr__(self):
        return f'{self.reading}'
    
    def calc_intervals(self):
        if max(self.reading) != 0:
            new_intervals = []
            
            for i in range(len(self.reading) - 1):
                new_intervals.append(self.reading[i + 1] - self.reading[i])

            return Line(new_intervals)
            
        else:
            return 0

def main():
    lines = read_file("test.txt")
    lines = [Line(line) for line in read_file("test.txt")]
    print(lines)
    
if __name__ == "__main__":
    main()