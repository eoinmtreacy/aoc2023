f = open("code.txt", "r")

lines = f.readlines()

nums = []

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    new = ""

    for digit in digits:
        if digit in line:
            new = new + str(digits.index(digit))
    for letter in letters:
        if digit in line:
            new = new + str(letters.index(letter))
            
    new = new[0] + new[-1]
    nums.append(new)

sum = 0

for num in nums:
    sum += int(num)
    print(num, end = " ")

print(sum)