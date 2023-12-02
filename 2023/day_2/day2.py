import sys

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13


# Part 1
def p1(lines):
    count = 0
    for line in lines:
        [tag, game] = line.split(": ")
        game_id = tag.replace("Game ", "")
        sets = game.split("; ")
        poss_set = []
        for i, set in enumerate(sets):
            cubes = set.split(", ")
            possible = []
            for i, cube in enumerate(cubes):
                [num, color] = cube.split(" ")
                if color == "green" and int(num)<=13 or color == "red" and int(num)<=12 or color == "blue" and int(num)<=14: 
                    possible.append(True)
                else:
                    possible.append(False)
            poss_set.append(False if False in possible else True)
        # print(poss_set)
        if False not in poss_set:
            count+=int(game_id)
    # print(count)



# Part 2
def p2(lines):
    count = 0
    for line in lines:
        [tag, game] = line.split(": ")
        game_id = tag.replace("Game ", "")
        sets = game.split("; ")
        poss_set = []
        MIN_GREEN, MIN_RED, MIN_BLUE = 1,1,1 
        for i, set in enumerate(sets):
            cubes = set.split(", ")
            possible = []
            for i, cube in enumerate(cubes):
                [num, color] = cube.split(" ")
                if color == "green" and int(num)>MIN_GREEN:
                    MIN_GREEN = int(num)
                if color == "red" and int(num)>MIN_RED:
                    MIN_RED = int(num)  
                if color == "blue" and int(num)>MIN_BLUE:
                    MIN_BLUE = int(num) 
                
            #calc power here
        # poss_set.append([MIN_BLUE, MIN_GREEN, MIN_RED])
        count += MIN_BLUE* MIN_GREEN* MIN_RED
    print(count)



if __name__ == "__main__":
    with open(sys.argv[1], "r") as f, open(sys.argv[2], "w") as out:
        lines = f.read().splitlines()
        solution = p1(lines)
        solution2 = p2(lines)
        # out.write("Part 1: " + str(solution) + "\n")
        # out.write("Part 2: " + str(solution2) + "\n")
