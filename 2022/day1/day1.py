import sys

def count_calories(lines):
    arr = [0]
    elf = 0
    for l in lines:
        if l == '':
            elf+=1
            arr.append(0)
        else:
            arr[elf] += int(l)
    return max(arr)

def count_calories_2(lines):
    arr = [0]
    elf = 0
    for l in lines:
        if l == '':
            elf+=1
            arr.append(0)
        else:
            arr[elf] += int(l)
    arr.sort()
    return sum(arr[-3::])


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        lines = [lines.replace('\n','') for lines in f]
        solution = count_calories(lines)
        solution2 = count_calories_2(lines)
        out.write('Part 1: '+str(solution)+'\n')
        out.write('Part 2: '+str(solution2)+'\n')