from sys import argv

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13    

def build_game_map(lines):
    game_map = {}
    for line in lines:
        [tag, game] = line.replace("Game ", "").split(": ")
        game_map[int(tag)]=[{
            cube.split()[1]: int(cube.split()[0]) 
                for cube in set.split(",")}
                    for set in game.split(";")]
    return game_map

# Part 1
def p1(game_map):
    return sum([id for id, sets in game_map.items() if all([
                cubes.get("green",0)<=MAX_GREEN and
                cubes.get("red",0)<=MAX_RED and
                cubes.get("blue",0)<=MAX_BLUE 
                    for cubes in sets])])

# Part 2
def p2(game_map):
    return sum(
            max(map(lambda x: x.get("green",0), sets)) * 
            max(map(lambda x: x.get("red",0), sets)) *
            max(map(lambda x: x.get("blue",0), sets))
                for _,sets in game_map.items())

if __name__ == "__main__":
    with open(argv[1], "r") as f, open(argv[2], "w") as out:
        lines = f.read().splitlines()
        game_map = build_game_map(lines)
        solution = p1(game_map)
        solution2 = p2(game_map)
        out.write("Part 1: " + str(solution) + "\n")
        out.write("Part 2: " + str(solution2) + "\n")
