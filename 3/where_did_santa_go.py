#!/usr/bin/python3

'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional 
grid of houses.

He begins by delivering a present to the house at his 
starting location, and then an elf at the North Pole 
calls him via radio and tells him where to move next. 
Moves are always exactly one house to the north (^), 
south (v), east (>), or west (<). After each move, he 
delivers another present to the house at his new location.

However, the elf back at the north pole has had a little 
too much eggnog, and so his directions are a little off, 
and Santa ends up visiting some houses more than once. 
How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
'''

EXAMPLES = [
		('>', 2),
		('^>v<', 4),
		('^v^v^v^v^v', 2) 
	]

def travel(direction, visited, lastpos):
	x, y = lastpos.split(',')
	x = int(x)
	y = int(y)

	if direction == '<':
		x -= 1
	elif direction == '>':
		x += 1
	elif direction == 'v':
		y -= 1
	elif direction == '^':
		y += 1

	newpos = '{x},{y}'.format(x=x, y=y)
	visited[newpos] = True

	return newpos


def main():
	for data, num in EXAMPLES:
		lastpos = '0,0'
		visited = {lastpos: True}

		for direction in data:
			lastpos = travel(direction, visited, lastpos)

		assert num == len(visited)
		print('ok')

	with open('input.txt') as fil:
		lastpos = '0,0'
		visited = {lastpos: True}
		for direction in fil.read():
			lastpos = travel(direction, visited, lastpos)

	print(len(visited))


if __name__ == '__main__':
	main()
