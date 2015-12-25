#!/usr/bin/python3

import sys
sys.setrecursionlimit(10000)

INPUT = 'short.txt'
INPUT = 'input.txt'

def climber(fil, floor, num):
	char = fil.read(1)
	if char == '(':
		floor += 1
	elif char == ')':
		floor -= 1
	else:
		return floor, num

	num += 1

	if floor < 0:
		return floor, num

	floor, num = climber(fil, floor, num)
	return floor, num


def main():
	with open(INPUT) as fil:
		floor, num = climber(fil, 0, 0)

	print('floor: {floor} num: {num}'.format(floor=floor, num=num))


if __name__ == '__main__':
	main()