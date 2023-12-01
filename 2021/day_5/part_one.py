import sys

def pretty_print(diagram):
	for line in diagram:
		print([str(point) for point in line])


def solve(coords, size_x, size_y):
	diagram = [['*' for _ in range(0,size_x)] for _ in range(0,size_y)]
	points = []
	for coord in coords:
		start, end = coord
		x0,y0 = start
		x1,y1 = end
		dx = x1-x0
		dy = y1-y0
		if dx == dy or dx == -dy:
			continue
		if dx == 0:
			#same line horizontal
			if dy>0:
				new_points = [(x0,y) for y in range(y0,y1+1)]
				points+= new_points
			elif dy<0:
				new_points = [(x0,y) for y in range(y1,y0+1)]
				points+= new_points
		elif dy == 0:
			#same line vertical
			if dx>0:
				new_points = [(x,y0) for x in range(x0,x1+1)]
				points+= new_points
			if dx<0:
				new_points = [(x,y0) for x in range(x1,x0+1)]
				points+= new_points
	
	# build diagram
	for point in points:
		x0, y0 = point
		if diagram[y0][x0] == '*':
			diagram[y0][x0] = 1
		elif diagram[y0][x0] >= 1:
			diagram[y0][x0] += 1
	
	count = 0
	# count number the of points greater than 1 
	for line in diagram:
		for point in line:
			if point != "*" and point>1:
				count+=1

	# pretty_print(diagram)
	return count

def parse_input(content):
	coords = []
	size_x = 0
	size_y = 0
	for nums in content:
		a,b = nums
		x0,y0 = map(int,a.strip().split(','))
		x1,y1 = map(int,b.strip().split(','))
		size_x = max([x0,x1, size_x])
		size_y = max([y0,y1,size_y])		
		coords+=[[(x0,y0),(x1,y1)]]
	return coords, size_x, size_y


if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
		content = [line.strip().split('->') for line in f]
		coords, size_x, size_y = parse_input(content)
		solution = solve(coords, size_x+1, size_y+1)
		out.write(str(solution))