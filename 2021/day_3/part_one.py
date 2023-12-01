import sys

def calc_power2(report:list, size:int)->int:	
	count = [0]*size					
	for num in report:
		for i,bit in enumerate(num):
			if bit=='1':
				count[i]+=1
	most_common =''.join(['1' if c>len(report)//2 else '0' for c in count])
	temp = int(most_common,2)
	temp2 = temp ^ (2 ** (len(most_common) + 1)-1)
	least_common = bin(temp2)[3:]
	return int(most_common,2)* int(least_common,2)	 	

def calc_power(report: list, size: int)->int:
	most_common = ''
	least_common = ''
	for i in range(0, size):
		count = 0
		for num in report:
			if num[i] == '1':
				count+=1
		if count > len(report)//2:
			most_common+='1'
			least_common+='0'
		else:
			most_common+='0'
			least_common+='1'
	return int(most_common,2) * int(least_common,2)

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
		content = [line.strip() for line in f]
		solution = calc_power2(content, len(content[0]))
		out.write(str(solution))
