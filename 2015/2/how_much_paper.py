#!/usr/bin/python3

'''
Usage:
  how_much_paper.py
  how_much_paper.py -s

Options:
  -h --help    Show help stuff
  -s --simple  Run a few simle examples
'''

from docopt import docopt
import sys

EXAMPLES = [
		('2x3x4', 58, 34),
						# requires 2*6 + 2*12 + 2*8 = 52 square feet of 
		            	# wrapping paper plus 6 square feet of slack, for
		            	# a total of 58 square feet.
						# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon 
						# to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for 
						# a total of 34 feet.
		('1x1x10', 43, 14) 
						# requires 2*1 + 2*10 + 2*10 = 42 square feet of 
						# wrapping paper plus 1 square foot of slack, 
						# for a total of 43 square feet.
						# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon
						# to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for 
						# a total of 14 feet.
	]


def prepare(data):
	l, w, h = data.split('x')
	
	l = int(l)
	w = int(w)
	h = int(h)

	return l, w, h

	
def calc_box_paper(l, w, h):
	lw = l * w 
	wh = w * h
	hl = h * l
	
	return 2*lw + 2*wh + 2*hl + min(lw, wh, hl)

def calc_box_ribbon(l, w, h):
	knot = l * w * h
	circ = 2 * (l + w + h - max(l, w, h))
	return knot + circ

def main():
	args = docopt(__doc__)

	if args['--simple']:
		for data, paper, ribbon in EXAMPLES:
			l, w, h = prepare(data)
			assert paper == calc_box_paper(l, w, h)
			assert ribbon == calc_box_ribbon(l, w, h)
			print('ok')

	else:
		paper = 0
		ribbon = 0
		with open('input.txt') as fil:
			for line in fil.readlines():
				l, w, h = prepare(line)
				paper += calc_box_paper(l, w, h)
				ribbon += calc_box_ribbon(l, w, h) 

		print(paper, ribbon)


if __name__ == '__main__':
	main()
