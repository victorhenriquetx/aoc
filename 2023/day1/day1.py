import sys

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# Part 1
# Find all digits in the line
def p1(line):
    digits = [c for c in line if c.isdigit() for line in lines]
    return int(digits[0] + digits[-1])


# Part 2
# Replace all "valid digit" words with their first and last letter and their index
# Ex: eight -> e8t
def p2(line):
    for i, n in enumerate(words, 1):
        line = line.replace(n, n[0] + str(i) + n[-1])
    return p1(line)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f, open(sys.argv[2], "w") as out:
        lines = f.read().splitlines()
        solution = sum(map(p1, lines))
        solution2 = sum(map(p2, lines))
        out.write("Part 1: " + str(solution) + "\n")
        out.write("Part 2: " + str(solution2) + "\n")
