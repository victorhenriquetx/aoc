import sys

def solve(content):
  count = 0
  for segment in content:
      if len(segment) in [2,3,4,7]:
        count+=1
  return count
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
      content = ' '.join([line.strip().split(' | ')[1] for line in f]).split(' ')
      solution_part_one = solve(content)
      # solution_part_two = solve_2(content)
      out.write('Part 1: '+str(solution_part_one)+'\n')
      # out.write('Part 2: '+str(solution_part_two))