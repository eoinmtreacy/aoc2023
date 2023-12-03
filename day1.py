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

checks = list(numbers.keys())

for line in lines:
    print(line)
    new = ""
    
    for i in range(1,len(line) + 1):
        for check in checks:
            if check in line[:i]:
                new = new + numbers[check]
                break
        if len(new) > 0:
            break
    for i in range(1,len(line) + 1):
        for check in checks:
            if check in line[-i:]:
                new = new + numbers[check]
                break
        if len(new) > 1:
            break

    nums.append(new)
    print(new)

sum = 0

for num in nums:
    sum += int(num)

print(sum)