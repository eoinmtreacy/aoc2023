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
        go = False
        for r in self.reading:
            if r != 0:
                go = True
                break
            
        if go:
            new_intervals = []
            for i in range(len(self.reading) - 1):
                new_intervals.append(self.reading[i + 1] - self.reading[i])
            return Line(new_intervals)
        else:
            return 0
        
    @property
    def predict_next_inc(self):
        if self.intervals == 0:
            return 0
        else:
            return self.intervals.reading[-1] + self.intervals.predict_next_inc

    def future_reading(self):
        return self.reading[-1] + self.predict_next_inc
    
def main():
    lines = [Line(line) for line in read_file("code.txt")]
    total = 0 
    for line in lines:
        total += line.future_reading()
    print(total)
    
if __name__ == "__main__":
    main()

# 1,681,758,967 too high (max != 0)
# 1,681,758,908 w/ loop to check if all not zero
# 891,209,680 too low (if not all)
# 886,195,462 (sum of all = 0)
# 1,8690,553 too low 
