import sys

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13    

# Part 1
def p1(line):
    [tag, game] = line.split(": ")
    game_id = int(tag.replace("Game ", ""))
    for set in game.split("; "):
        poss = 1
        for cube in set.split(", "):
            [num, color] = cube.split(" ")
            if color == "green" and int(num)<=13 or color == "red" and int(num)<=12 or color == "blue" and int(num)<=14: 
                poss *= 1
            else:
                poss *= 0
        game_id *= poss
    return game_id

# Part 2
def p2(line):
    game = line.split(": ")[1]
    min_green, min_red, min_blue = 1,1,1 
    for set in game.split("; "):
        for cube in set.split(", "):
            [num, color] = cube.split(" ")
            num = int(num)
            if color == "green" and num>min_green:
                min_green = num
            if color == "red" and num>min_red:
                min_red = num  
            if color == "blue" and num>min_blue:
                min_blue = num 
    return min_blue*min_green*min_red



if __name__ == "__main__":
    with open(sys.argv[1], "r") as f, open(sys.argv[2], "w") as out:
        lines = f.read().splitlines()
        solution = sum(map(p1, lines))
        solution2 = sum(map(p2, lines))
        out.write("Part 1: " + str(solution) + "\n")
        out.write("Part 2: " + str(solution2) + "\n")
