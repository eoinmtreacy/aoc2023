f = open("code.txt", "r")

lines = f.readlines()

# 140 chars on a line, 140 lines

# 360007 too low
# 426397 too low

matrix = []

symbols = "$%@/-&+=*#"

for line in lines:
    matrix.append(line[:-1])

def print_surround(matrix, y, x, length):

    for i in range(-1, length + 1, 1):
        if y - 1 >= 0 and x + i < 140:
            print(matrix[y - 1][x + i], end = "")
    print()
    
    if x - 1 >= 0:
        print(matrix[y][x - 1], end = "")

    if x + length < 140:
        print(matrix[y][x + length], end = "")

    print()

    for i in range(length, -2, -1):
        if y + 1 < 140 and x + length < 140:
            print(matrix[y + 1][x + i], end = "")

    print()

print_surround(matrix, 1, 133, 3)
    