#!/usr/env python

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
