import sys
def check_bingo(pos, numbers, mat_width):
	marked_dics = [[{},{}] for i in range(0,len(pos))]
	sum_marked = [0]*len(pos)
	winner_boards = []
	last_score = 0 	
	for num in numbers:
		#print('ganharam', winner_boards)
		#print('pos', len(pos))
		#print('n winners', len(winner_boards))
		
		if len(winner_boards) == len(pos):
			#print('acabou')
			#print('leaderboard', winner_boards)
			#print('winners', winner_boards.sort())
			break
		for mat_index, mat in enumerate(pos):
			if mat_index in winner_boards:
				continue
			dic_line = marked_dics[mat_index][0]
			dic_col = marked_dics[mat_index][1]
			if not num in mat:
				continue
			i,j = mat[num]
			if i in dic_line:
				dic_line[i] += 1
			else:
				dic_line[i] = 1
			if j in dic_col:
				dic_col[j] += 1
			else:
 				dic_col[j] = 1
			sum_marked[mat_index] += int(num)
			for key, value in dic_line.items():
				if value == mat_width:
					#print('num', num)
					#print('linha', key)
					#print('winner', mat)
					winners_coord = [(key,j) for j in range(0,mat_width)]
					winner = 0
					not_marked = 0
					for key, value in mat.items():
						if value not in winners_coord:
							not_marked += int(key)
						else:
							winner += int(key)
					#print('soma marked',sum_marked[mat_index])
					#print('soma winner',winner)
					last_score = (int(not_marked)-int(sum_marked[mat_index])+int(winner))*int(num)
					winner_boards += [mat_index]
					#print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
			for key, value in dic_col.items():
				if value == mat_width:
					winners_coord = [(i,key) for i in range(0,mat_width)]
					winner = 0
					not_marked = 0
					for key, value in mat.items():
						if value not in winners_coord:
							not_marked += int(key)
						else:
							winner += int(key)
					#print('num', num)
					#print('coluna', key)
					#print('winner', mat)
					#print('soma marked', sum_marked[mat_index])
					#print('soma winner', winner)
					last_score = (int(not_marked)-int(sum_marked[mat_index])+int(winner))*int(num)
					if mat_index not in winner_boards:
						winner_boards += [mat_index]
					#print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
	return last_score

def solution(content):
	numbers = content[0].split(',')
	pos = []
	init_matrix = []
	mat_index = -1
	line_index = 0
	marked_dic = []
	mat_width = 0
	for _, line in enumerate(content[1:]):
		if line == '':
			mat_index += 1
			line_index = 0
			pos.append({})
		else:
			for col_index, num in enumerate(filter(lambda x: x!='', line.split(' '))):
				if num == '':
					col_index -= 1
				else:	
					pos[mat_index][num] = (line_index, col_index)
			line_index += 1
		#print('pos', pos)
		#print('mat_index', mat_index)
		#print('line_index', line_index)
		#print('line', line)

	print('result', check_bingo(pos, numbers, line_index))




if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
		content = [line.strip() for line in f]
		solution(content)
		#out.write(str(solution))
