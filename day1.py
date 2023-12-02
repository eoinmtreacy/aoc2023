f = open("code.txt", "r")

lines = f.readlines()

nums = []

numbers = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

checking = list(numbers.keys())

for l,line in enumerate(lines):
    print(line)
    new = []
    for check in checking:
        if check in line:
            for i, check in enumerate(line):
                    try:
                        new.append((numbers[check],i))
                    except:
                         pass
    new.sort(key=lambda x : x[1])
    addition = new[0][0] + new[-1][0]
    if l == 999:
        pass
    nums.append(addition)
    print(addition)

sum = 0

for num in nums:
    sum += int(num)

print(sum)