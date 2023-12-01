import sys


def count_increases(measurements:list)->int:
    count = 0
    for index,_ in enumerate(measurements):
        if index+1 == len(measurements):
            return count
        elif measurements[index+1]>measurements[index]:
            count += 1



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        content = [int(line) for line in f]
        solution = count_increases(content)
        out.write(str(solution))
