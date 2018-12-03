#!/usr/env python

'''
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

Your puzzle answer was 101196.

--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?

Your puzzle answer was 243.

Both parts of this puzzle are complete! They provide two gold stars: **

'''

def get_input(filename='2018/3/input.txt'):
    with open(filename) as fil:
        lines = fil.readlines()

    return lines

class Fabric():
    '''
    >>> Fabric(3,3).add((1,1),(1,1)).plot().count()
    . . .
    . x .
    . . .
    0
    >>> Fabric(3,3).add((0,0),(1,1)).plot().count()
    x . .
    . . .
    . . .
    0
    >>> Fabric(3,3).add((2,2),(1,1)).plot().count()
    . . .
    . . .
    . . x
    0
    >>> Fabric(4,3).add((2,2),(2,1)).plot().count()
    . . . .
    . . . .
    . . x x
    0
    >>> Fabric(4,5).add((1,0),(3,3)).add((0,2), (2,2)).plot().count()
    . x x x
    . x x x
    x o x x
    x x . .
    . . . .
    1
    '''
    def __init__(self, x, y):
        self.matrix = [['.' for i in range(x)] for i in range(y)]

    def add(self, pos, size):
        x, y = pos
        dx, dy = size
        for cy in range(y, y+dy):
            for cx in range(x, x+dx):
                self.matrix[cy][cx] = 'x' if self.matrix[cy][cx] == '.' else 'o'
        return self

    def is_overlapping(self, pos, size):
        '''
        >>> Fabric(2,2).add((0,0),(1,1)).add((0,0),(1,1)).is_overlapping((0,0), (1,1))
        True
        >>> Fabric(2,2).add((0,0),(1,1)).is_overlapping((1,0), (1,1))
        False
        >>> Fabric(4,5).add((1,0),(3,3)).add((0,2), (2,2)).add((2,3), (2,2)).plot().is_overlapping((2,3), (2,2))
        . x x x
        . x x x
        x o x x
        x x x x
        . . x x
        False
        >>> Fabric(8,8).add((1,3), (4,4)).add((3,1), (4,4)).add((5,5), (2,2)).is_overlapping((5,5), (2,2))
        False
        '''
        x, y = pos
        dx, dy = size
        for cy in range(y, y+dy):
            for cx in range(x, x+dx):
                if self.matrix[cy][cx] == 'o':
                    return True
        return False

    def plot(self):
        for line in self.matrix:
            print(' '.join(line))
        return self

    def count(self):
        count = 0
        for line in self.matrix:
            for x in [x for x in line if x == 'o']:
                count += 1
        return count

def transform(piece):
    '''
    >>> transform('#123 @ 3,2: 5x4')
    (123, (3, 2), (5, 4))
    '''
    p = piece.split()
    idn = p[0].strip('#')
    posx, posy = p[2].strip(':').split(',')
    sx, sy = p[3].split('x')
    return (int(idn), (int(posx), int(posy)), (int(sx), int(sy)))

def main():
    pieces = get_input()
    pieces = list(map(transform, pieces))

    f = Fabric(1000,1000)
    for idn, pos, size in pieces:
        f.add(pos, size)
    print(f.count())

    for idn, pos, size in pieces:
        if not f.is_overlapping(pos, size):
            print(idn)


if __name__ == '__main__':
    main()
