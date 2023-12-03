f = open("code.txt", "r")

lines = f.readlines()

# 140 chars on a line, 140 lines

matrix = []

symbols = "$%@/-&+=*#"

for line in lines:
    matrix.append([line[:-1]])

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        # iterate through the matrix until it encounters a number with no preceding number

        valid = False
        number = ""

        try:

            if matrix[i][j] in "0123456789" and matrix[i][j - 1] not in "0123456789":
                size = 1
                counting = True
                number = number + matrix[i][j]
                # determine size of the number, will affect adjacent squres inspected
                while counting:
                    if matrix[i][j + size] in "0123456789":
                        number = number + matrix[i][j]
                        size += 1
                    else:
                        counting = False

                if matrix[i - 1][j - 1] in symbols or matrix[i][j - 1] in symbols:
                    valid = True


                for k in range(0, size + 1):
                    if matrix[i - 1][j + k] in symbols:
                        valid = True
                        break
                
                if matrix[i][j + size] in symbols:
                    valid = True
                try:
                    for k in range(size + 1, 0, -1):
                        if matrix[i + 1][j - k] in symbols:
                            valid = True
                            break
                except:
                    pass

                if valid:
                    total += int(number)

        except:
            pass

print(total)

            
