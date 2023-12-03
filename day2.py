f = open("code.txt", "r")

lines = f.readlines()

r, g, b = 12, 13, 14

ids = []

for line in lines:

    valid = True
    blue, red, green = 0, 0, 0
    chunk = line.split()
    id = chunk[1][:-1]

    games = line.split(":")[1].split(";")
    for game in games:
        
        colors = game.split(",")
        print(colors)
        for color in colors:
            stripped = color.strip()
            if "blue" in stripped:
                blue = int(stripped.split()[0])
            if "green" in stripped:
                green = int(stripped.split()[0])
            if "red" in stripped:
                red = int(stripped.split()[0])
                
            try:
                if blue > b: 
                    valid = False
                    break
            except:
                pass

            try:
                if red > r: 
                    valid = False
                    break
            except:
                pass

            try:
                if green > g: 
                    valid = False
                    break
            except:
                pass

    if valid:
        ids.append(int(id))

print(sum(ids))