f = open("test.txt", "r")

lines = f.readlines()

# 140 chars on a line, 140 lines

# 360007 too low
# 426397 too low
# 573677 too high
# 575609 too high

def check_surround(matrix, y, x, length, X):
    symbols = "$%@/-&+=*#"

    for i in range(-1, length, 1):
        if y - 1 >= 0 and x + i > 0 and x + i < X:
            if matrix[y - 1][x + i] in symbols:
                return True
    
    if x - 1 >= 0:
        if matrix[y][x - 1] in symbols:
            return True

    if x + length < X:
        if matrix[y][x + length] in symbols:
            return True

    for i in range(length - 1, -2, -1):
        if y + 1 < X and x + i > -1:
            if matrix[y + 1][x + i]:
                return True
    
    return False

matrix = []

for line in lines:
    matrix.append(line[:-1])

X = len(matrix[0])
print(X)

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        # iterate through the matrix until it encounters a number with no preceding number

        number = ""

        if matrix[i][j] in "0123456789" and  j - 1 >= 0 and matrix[i][j - 1] not in "0123456789":
            size = 1
            counting = True
            number = number + matrix[i][j]
            # determine size of the number, will affect adjacent squares inspected
            while counting:
                if j + size < X and matrix[i][j + size] in "0123456789":
                    number = number + matrix[i][j + size]
                    size += 1
                else:
                    counting = False
            print(i,j, number)
            
            if check_surround(matrix, i, j, len(number), X):
                total += int(number)

print(total)

            
