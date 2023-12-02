import sys

def count_calories(lines):
    """
    This function counts the calories consumed by each elf, and returns the maximum calorie count.

    :param lines: a list of strings representing the calorie intake for each elf
    :return: the maximum calorie count among all elves
    """
    arr = [0]
    elf = 0
    arr = [0 if l == '' else arr[elf] + int(l) for l in lines]
    return max(arr)

def count_calories_2(lines):
    """
    This function counts the calories consumed by each elf, and returns the sum of the top three calorie counts.

    :param lines: a list of strings representing the calorie intake for each elf
    :return: the sum of the top three calorie counts among all elves
    """
    arr = [0]
    elf = 0
    arr = [0 if l == '' else arr[elf] + int(l) for l in lines]
    arr.sort()
    return sum(arr[-3::])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        lines = [lines.replace('\n','') for lines in f]
        solution = count_calories(lines)
        solution2 = count_calories_2(lines)
        out.write('Part 1: '+str(solution)+'\n')
        out.write('Part 2: '+str(solution2)+'\n')
