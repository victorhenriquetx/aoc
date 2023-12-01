import sys

def calc_bit_freq(report:list, bit_position:int)->dict:	
	count = 0					
	for num in report:
		if num[bit_position]=='1':
			count+=1
	if count>=len(report)/2:
		most_common = '1'
		least_common = '0'
	else:
		most_common = '0'
		least_common = '1'
	return {'most_common':most_common, 'least_common':least_common}	 	

def filter_bit_numbers(report:list, bit_size:int, bit_criteria:str)->int:
	report_seq = report
	for i in range(0, bit_size):
		if len(report_seq)==1:
			break;
		bit_freq = calc_bit_freq(report_seq, i)
		report_seq =[x for x in report_seq if x[i]==bit_freq[bit_criteria]]
	return report_seq[0]

def calc_life_support(report:list, bit_size:int)->int:
	oxigen_rating = filter_bit_numbers(report, bit_size, 'most_common')
	co2_rating = filter_bit_numbers(report, bit_size, 'least_common')
	return int(oxigen_rating,2)* int(co2_rating,2)	

		
if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
		content = [line.strip() for line in f]
		solution = calc_life_support(content, len(content[0]))
		out.write(str(solution))
