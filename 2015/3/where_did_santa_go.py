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

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
'''

EXAMPLES = [
		('^v', 3),
		('^>v<', 3),
		('^v^v^v^v^v', 11) 
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
		santa_position = '0,0'
		robo_position = '0,0'
		visited = {santa_position: True}

		santa_move = True
		for direction in data:
			if santa_move:
				santa_position = travel(direction, visited, santa_position)
			else:
				robo_position = travel(direction, visited, robo_position)

			santa_move = not santa_move

		assert num == len(visited)
		print('ok')

	with open('input.txt') as fil:
		santa_position = '0,0'
		robo_position = '0,0'
		visited = {santa_position: True}
		santa_move = True

		directions = fil.read()
		for direction in directions:
			if santa_move:
				santa_position = travel(direction, visited, santa_position)
			else:
				robo_position = travel(direction, visited, robo_position)

			santa_move = not santa_move

	print(len(visited))


if __name__ == '__main__':
	main()
