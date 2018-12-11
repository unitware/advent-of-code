'''
--- Day 10: The Stars Align ---
It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle, and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly enough that it takes hours to align them, but have so much momentum that they only stay aligned for a second. If you blink at the wrong time, it might be hours before another message appears.

You can see these points of light floating in the distance, and record their position in the sky and their velocity, the relative change in position per second (your puzzle input). The coordinates are all given from your perspective; given enough time, those positions and velocities will move the points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.

For example, suppose you note the following points:

position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative) or right (positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position. So, a point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this point's initial position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........

After 1 second:
......................
......................
..........#....#......
........#.....#.......
..#.........#......#..
......................
......#...............
....##.........#......
......#.#.............
.....##.##..#.........
........#.#...........
........#...#.....#...
..#...........#.......
....#.....#.#.........
......................
......................

After 2 seconds:
......................
......................
......................
..............#.......
....#..#...####..#....
......................
........#....#........
......#.#.............
.......#...#..........
.......#..#..#.#......
....#....#.#..........
.....#...#...##.#.....
........#.............
......................
......................
......................

After 3 seconds:
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................

After 4 seconds:
......................
......................
......................
............#.........
........##...#.#......
......#.....#..#......
.....#..##.##.#.......
.......##.#....#......
...........#....#.....
..............#.......
....#......#...#......
.....#.....##.........
...............#......
...............#......
......................
......................
After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will take many more seconds to appear.

What message will eventually appear in the sky?
'''
import textwrap
import re

def parse_signed_int(data):
    '''
    >>> parse_signed_int(' 9')
    9
    >>> parse_signed_int(' -9')
    -9
    '''
    data = data.strip()

    try:
        if data[0] == '-':
            return -int(data[1:])
        else:
            return int(data)
    except ValueError:
        raise StopIteration()

reparse = re.compile(r'.*=<([^,]*),([^>]*)>.*=<([^,]*),([^>]*)>')
def parse_line(line):
    '''
    >>> parse_line('position=< 9,  1> velocity=< 0,  2>\\n')
    ((9, 1), (0, 2))
    >>> parse_line('position=< 7,  0> velocity=<-1,  0>\\n')
    ((7, 0), (-1, 0))
    >>> parse_line('position=< 3, -2> velocity=<-1,  1>\\n')
    ((3, -2), (-1, 1))
    >>> parse_line('\\n')
    Traceback (most recent call last):
        ...
    StopIteration
    '''
    match = reparse.match(line)
    if match is None:
        raise StopIteration()

    x, y, vx, vy = map(parse_signed_int, match.groups())
    return ((x, y), (vx, vy))

def get_input(filename='2018/10/input.txt'):
    with open(filename) as fil:
        for line in fil.readlines():
            yield parse_line(line)


def example_input():
    '''
    > >> list(example_input())
    '''
    lines = textwrap.dedent('''position=< 9,  1> velocity=< 0,  2>
            position=< 7,  0> velocity=<-1,  0>
            position=< 3, -2> velocity=<-1,  1>
            position=< 6, 10> velocity=<-2, -1>
            position=< 2, -4> velocity=< 2,  2>
            position=<-6, 10> velocity=< 2, -2>
            position=< 1,  8> velocity=< 1, -1>
            position=< 1,  7> velocity=< 1,  0>
            position=<-3, 11> velocity=< 1, -2>
            position=< 7,  6> velocity=<-1, -1>
            position=<-2,  3> velocity=< 1,  0>
            position=<-4,  3> velocity=< 2,  0>
            position=<10, -3> velocity=<-1,  1>
            position=< 5, 11> velocity=< 1, -2>
            position=< 4,  7> velocity=< 0, -1>
            position=< 8, -2> velocity=< 0,  1>
            position=<15,  0> velocity=<-2,  0>
            position=< 1,  6> velocity=< 1,  0>
            position=< 8,  9> velocity=< 0, -1>
            position=< 3,  3> velocity=<-1,  1>
            position=< 0,  5> velocity=< 0, -1>
            position=<-2,  2> velocity=< 2,  0>
            position=< 5, -2> velocity=< 1,  2>
            position=< 1,  4> velocity=< 2,  1>
            position=<-2,  7> velocity=< 2, -2>
            position=< 3,  6> velocity=<-1, -1>
            position=< 5,  0> velocity=< 1,  0>
            position=<-6,  0> velocity=< 2,  0>
            position=< 5,  9> velocity=< 1, -2>
            position=<14,  7> velocity=<-2,  0>
            position=<-3,  6> velocity=< 2, -1>''').splitlines()
    for line in lines:
        yield parse_line(line)


class Stars():
    def __init__(self, stars):
        self.stars = list(stars)

    def extents(self):
        '''
        >>> Stars([((1,1), (0,0)), ((2,2), (0,0))]).extents()
        (1, 1, 2, 2)
        >>> Stars([((3,1), (0,0)), ((2,2), (0,0))]).extents()
        (2, 1, 3, 2)
        '''
        minx = None
        miny = None
        maxx = None
        maxy = None
        for pos, _ in self.stars:
            x, y = pos
            minx = min(minx, x) if minx is not None else x
            maxx = max(maxx, x) if maxx is not None else x
            miny = min(miny, y) if miny is not None else y
            maxy = max(maxy, y) if maxy is not None else y
        return minx, miny, maxx, maxy

    def plot(self):
        '''
        >>> Stars([((1,1), (0,0)), ((2,2), (0,0))]).plot()
        '#.'
        '.#'
        >>> Stars([((3,1), (0,0)), ((2,2), (0,0))]).plot()
        '.#'
        '#.'
        >>> Stars([((-1,1), (0,0)), ((2,2), (0,0))]).plot()
        '#...'
        '...#'
        '''
        x1, y1, x2, y2 = self.extents()
        sky = [['.' for _ in range(1+x2-x1)] for _ in range(1+y2-y1)]

        cnt = 0
        for star in self.stars:
            pos, _ = star
            x, y = pos
            if not True:
                c = str(cnt)
                cnt += 1
            else:
                c = '#'
            sky[y - y1][x - x1] = c
        for y in range(1 + y2 - y1):
            line = ''
            for x in range(1 + x2 - x1):
                line += sky[y][x]
            print(repr(line))


    def move(self, time):
        new_stars = []
        for i in range(len(self.stars)):
            pos, vel = self.stars[i]
            x, y = pos
            vx, vy = vel
            x = x + time * vx
            y = y + time * vy
            pos = x, y

            self.stars[i] = (pos, vel)
        return self

        # for t in range(time):
        #     for i in range(len(self.stars)):
        #         pos, vel = self.stars[i]
        #         self.stars[i] = [sum(x) for x in zip(pos, vel)], vel
        # return self

    def plot_at(self, time):
        self.move(time)
        self.plot()

    def find_text(self, timeout=10):
        t = 0
        while timeout:
            t += 1
            timeout -= 1
            old_extent = self.extents()
            self.move(1)
            if self.extent_has_increased(old_extent):
                break
        if 0 == timeout:
            print('timeout')
        else:
            self.move(-1)
            self.plot()
            print(t-1)

    def extent_has_increased(self, old_extent):
        ox1, oy1, ox2, oy2 = old_extent
        nx1, ny1, nx2, ny2 = self.extents()
        oa = (ox2-ox1) * (oy2-oy1)
        na = (nx2-nx1) * (ny2-ny1)

#        print(oa, na)
        return oa < na

def test_example_auto():
    '''
    >>> Stars(example_input()).find_text()
    '#...#..###'
    '#...#...#.'
    '#...#...#.'
    '#####...#.'
    '#...#...#.'
    '#...#...#.'
    '#...#...#.'
    '#...#..###'
    3

    #part A and B
    >>> Stars(get_input()).find_text(timeout=1000000)
    '######..#####...#....#..######...####...#....#.....###.....###'
    '#.......#....#..#...#...#.......#....#..#...#.......#.......#.'
    '#.......#....#..#..#....#.......#.......#..#........#.......#.'
    '#.......#....#..#.#.....#.......#.......#.#.........#.......#.'
    '#####...#####...##......#####...#.......##..........#.......#.'
    '#.......#..#....##......#.......#.......##..........#.......#.'
    '#.......#...#...#.#.....#.......#.......#.#.........#.......#.'
    '#.......#...#...#..#....#.......#.......#..#....#...#...#...#.'
    '#.......#....#..#...#...#.......#....#..#...#...#...#...#...#.'
    '######..#....#..#....#..######...####...#....#...###.....###..'
    10645
    '''
    pass

def test_example():
    '''

    >>> Stars(example_input()).plot()
    '........#.............'
    '................#.....'
    '.........#.#..#.......'
    '......................'
    '#..........#.#.......#'
    '...............#......'
    '....#.................'
    '..#.#....#............'
    '.......#..............'
    '......#...............'
    '...#...#.#...#........'
    '....#..#..#.........#.'
    '.......#..............'
    '...........#..#.......'
    '#...........#.........'
    '...#.......#..........'

    >>> Stars(example_input()).plot_at(1)
    '........#....#....'
    '......#.....#.....'
    '#.........#......#'
    '..................'
    '....#.............'
    '..##.........#....'
    '....#.#...........'
    '...##.##..#.......'
    '......#.#.........'
    '......#...#.....#.'
    '#...........#.....'
    '..#.....#.#.......'

    >>> Stars(example_input()).plot_at(2)
    '..........#...'
    '#..#...####..#'
    '..............'
    '....#....#....'
    '..#.#.........'
    '...#...#......'
    '...#..#..#.#..'
    '#....#.#......'
    '.#...#...##.#.'
    '....#.........'

    >>> Stars(example_input()).plot_at(3)
    '#...#..###'
    '#...#...#.'
    '#...#...#.'
    '#####...#.'
    '#...#...#.'
    '#...#...#.'
    '#...#...#.'
    '#...#..###'

    >>> Stars(example_input()).plot_at(4)
    '........#....'
    '....##...#.#.'
    '..#.....#..#.'
    '.#..##.##.#..'
    '...##.#....#.'
    '.......#....#'
    '..........#..'
    '#......#...#.'
    '.#.....##....'
    '...........#.'
    '...........#.'

    '''
    pass
