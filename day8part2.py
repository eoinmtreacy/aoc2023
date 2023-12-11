from math import lcm

def read_file(name):
    f = open(name)
    lines = f.read()
    return lines.split("\n\n")[0], lines.split("\n\n")[1].split("\n")

def parse_nodes(nodes):
    return_nodes = []
    for node in nodes:
        where, to = node.split("=")
        left, right = to.split(",")
        left, right = left[2:], right[:-1]
        return_nodes.append((where[:-1], left, right[1:]))
    return return_nodes

class Node:
    def __init__(self, instr, current, count, step, start = 1):
        self.instr = instr
        self.current = current
        self.count = count
        self.step = step
        self.start = start

    def __repr__(self):
        return f'{self.current}'

    def traverse_map(self, map):

        while self.current[0][-1] != "Z":
            for m in map:
                if m[0] == self.current[self.start]:
                    self.count += 1
                    self.step += 1
                    self.start = 1 if self.instr[self.step % len(self.instr)] == "L" else 2
                    self.current = m
                    break
        return self.count
    
def gen_nodes(nodes, instr):
    a_nodes = []
    for node in nodes:
        if node[0][-1] == "A":
            a_nodes.append(Node(instr, node, 0, 0))
    return a_nodes

def main():
    instr, raw_nodes = read_file("code.txt")
    map = parse_nodes(raw_nodes)

    nodes = gen_nodes(map, instr)

    print([node.traverse_map(map) for node in nodes])

    print(lcm(11653,19783, 19241, 16531,12737,14363))
if __name__ == "__main__":
    main()

# 129,260,005,219 too low 
