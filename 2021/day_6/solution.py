import sys

def solve(content, days):
  num_fish = [0 for _ in range(0,9)]
  for fish in content:
    num_fish[fish] += 1

  for i in range(days):
    new_fish = num_fish[0]
    for index,num in enumerate(num_fish):
      if index!=8:
        num_fish[index] = num_fish[index+1]
    num_fish[6] += new_fish
    num_fish[8] = new_fish

  return sum(num_fish)


if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
    content = list(map(int, f.read().strip().split(',')))
    # solution_part_1 = solve(content, 80)
    solution_part_2 = solve(content, 9999999)
    # out.write('Part 1: '+str(solution_part_1)+'\n')
    out.write('Part 2: '+str(solution_part_2))