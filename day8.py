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

def main():
    instr, nodes = read_file("code.txt")
    nodes = parse_nodes(nodes)

    print(instr, nodes)

    current = "AAA"
    count = 0
    step = 0

    while current != "ZZZ":
        for node in nodes:
            if node[0] == current:  
                
                count += 1
                start = 1 if instr[step % len(instr)] == "L" else 2
                step += 1
                current = node[start]
                print(node)
                break

    print(count)

if __name__ == "__main__":
    main()

# 3523 too low
# 3524 too low