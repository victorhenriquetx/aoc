import sys


def follow_course(coords:list)->int:
    horiz_pos = 0
    depth = 0
    for coord in coords:
        direction, units = coord
        if direction == 'forward':
            horiz_pos += int(units)
        elif direction == 'down':
            depth += int(units)
        elif direction == 'up':
            depth -= int(units)
    return depth * horiz_pos

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        content = [line.split(' ') for line in f]
        solution = follow_course(content)
        out.write(str(solution))
