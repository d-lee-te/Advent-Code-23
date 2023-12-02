import os    

def parseString(gLine, rm, gm, bm):
    f1, f2, f3 = False, False, False
    pos = True
    rL = []
    gL = []
    bL = []

    sgLine = gLine.split(": ")
    gameID = sgLine[0].strip()[4:]
    sgLine = sgLine[1]
    sgLine = sgLine.split("; ")
    
    for game in sgLine:
        rgb = game.strip()
        rgb = rgb.split(",")

        for color in rgb:
            col = color.strip()
            col = col.split()
            v = col[0]
            c = col[1]

            if c == "red":
                rL.append(int(v))
                if int(v) > rm:
                    f1 = True
            elif c == "green":
                gL.append(int(v))
                if int(v) > gm:
                    f2 = True
            elif c == "blue":
                bL.append(int(v))
                if int(v) > bm:
                    f3 = True

    if f1 or f2 or f3:
        pos = False

    rMin = max(rL)
    gMin = max(gL)
    bMin = max(bL)
    minCubes = rMin * gMin * bMin

    return (pos, gameID, minCubes)

current_directory = os.getcwd()
target = "puzzle_input.txt"
target_fpath = os.path.join(current_directory, target)


gList = []
with open(target_fpath, 'r') as file:
    gList = [line.rstrip('\n') for line in file.readlines()]


r, g, b = 12, 13, 14
idSum = []
cubePower = []
for game in gList:
    p, ID, minCubes = parseString(game, r, g, b)
    if p == True:
        idSum.append(int(ID))
    cubePower.append(minCubes)

print("Final Value: " + str(sum(idSum)) + " Min Cube Sum: " + str(sum(cubePower)))