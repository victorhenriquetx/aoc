import sys

def count_sum_of_measurements(measurements:list)->int:
    count = 0
    window = sum(measurements[:3])
    new_measurements_list = measurements[1:]
    for index,n in enumerate(new_measurements_list):
        if index+3 == len(measurements):
            return count
        else:
            new_window = sum(new_measurements_list[index:index+3])
            if new_window > window:
                count+=1
            window = new_window


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        content = [int(line) for line in f]
    
        solution = count_sum_of_measurements(content)
        
        out.write(str(solution))

