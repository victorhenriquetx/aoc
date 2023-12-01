import sys

#TODO: Solve by calculating the sum of distances between crabs and the median
def solve(content):
    min_fuel = float('inf')
    for pos in range(0,len(content)):
      fuel = 0
      for i, crab in enumerate(content):
        fuel += abs(crab-pos)
      min_fuel = min(min_fuel, fuel)
    return min_fuel

#TODO: Solve by minimum sum between the ceil and floor of distances between crabs and the mean times the fuel
def solve_2(content):
    min_fuel = float('inf')
    memo_crab_fuel = {}
    for pos in range(0, len(content)):
      fuel = 0
      for i, crab in enumerate(content):
        dist = abs((crab-pos))
        crab_fuel = 0
        if dist in memo_crab_fuel:
          crab_fuel = memo_crab_fuel[dist]
        else:
          crab_fuel = (dist*(dist+1))/2
          memo_crab_fuel[dist] = crab_fuel  
        fuel += crab_fuel
      min_fuel = min(min_fuel, fuel)
    return min_fuel



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
      content = list(map(int, f.read().strip().split(',')))
      solution_part_one = solve(content)
      solution_part_two = solve_2(content)
      out.write('Part 1: '+str(solution_part_one)+'\n')
      out.write('Part 2: '+str(solution_part_two))