f = open("code.txt", "r")

lines = f.readlines()

# 140 chars on a line, 140 lines

# 360007 too low
# 426397 too low

matrix = []

symbols = "$%@/-&+=*#"

for line in lines:
    matrix.append(line[:-1])

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        # iterate through the matrix until it encounters a number with no preceding number

        valid = False
        number = ""

        try:
            if matrix[i][j] in "0123456789" and matrix[i][j - 1] not in "0123456789" and j - 1 >= 0:
                size = 1
                counting = True
                number = number + matrix[i][j]
                # determine size of the number, will affect adjacent squares inspected
                while counting:
                    if matrix[i][j + size] in "0123456789":
                        number = number + matrix[i][j + size]
                        size += 1
                    else:
                        counting = False
                try:
                    # print(matrix[i - 1][j - 1], matrix[i][j - 1])
                    if matrix[i - 1][j - 1] in symbols or matrix[i][j - 1] in symbols and i - 1 >= 0 and j -1 >= 0:
                        valid = True
                except:
                    pass

                try:
                    for k in range(0, size + 1):
                        # print(matrix[i - 1][j + k])
                        if matrix[i - 1][j + k] in symbols and i - 1 >= 0:
                            valid = True
                            break
                except:
                    pass
                
                try:
                    # print(matrix[i][j + size])
                    if matrix[i][j + size] in symbols:
                        valid = True
                except:
                    pass

                try:
                    for k in range(size + 1, 0, -1):
                        # print(matrix[i + 1][j + k])
                        if matrix[i + 1][j + k] in symbols:
                            valid = True
                            break
                except:
                    pass

                if valid:
                    total += int(number)

        except:
            pass

print(total)

            
