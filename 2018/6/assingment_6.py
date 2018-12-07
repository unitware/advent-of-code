#!/usr/bin/python

'''
--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

--- Part Two ---
On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

..........
.A........
..........
...#%#..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.
In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:

Distance to coordinate A: abs(4-1) + abs(3-1) =  5
Distance to coordinate B: abs(4-1) + abs(3-6) =  6
Distance to coordinate C: abs(4-8) + abs(3-3) =  4
Distance to coordinate D: abs(4-3) + abs(3-4) =  2
Distance to coordinate E: abs(4-5) + abs(3-5) =  3
Distance to coordinate F: abs(4-8) + abs(3-9) = 10
Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?
'''

def get_input(filename='2018/6/input.txt'):
    with open(filename) as fil:
        for line in fil.readlines():
            yield line

def example_input():
    for line in ['1, 1\n',
                 '1, 6\n',
                 '8, 3\n',
                 '3, 4\n',
                 '5, 5\n',
                 '8, 9\n']:
        yield line


def parse_input(data):
    '''
    >>> parse_input(example_input())
    [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
    '''
    output = []
    for line in data:
        output.append(tuple(map(int, line.split(','))))
    return output

def is_inner_coords(pos, points):
    '''
    >>> is_inner_coords((3, 4), parse_input(example_input()))
    True
    >>> is_inner_coords((1, 1), parse_input(example_input()))
    False
    '''
    x, y = pos
    leftmost = True
    rightmost = True
    highest = True
    lowest = True

    for px, py in points:
        if px < x:
            leftmost = False
        elif px > x:
            rightmost = False

        if py < y:
            lowest = False
        elif py > y:
            highest = False

    return not (leftmost or rightmost or highest or lowest)


def find_inner_coords(points):
    '''
    >>> find_inner_coords(parse_input(example_input()))
    [(3, 4), (5, 5)]
    '''
    inner = []
    for point in points:
        if is_inner_coords(point, points):
            inner.append(point)
    return inner

def calc_distance(a, b):
    '''
    >>> calc_distance((1, 1), (1, 6))
    5
    >>> calc_distance((1, 1), (2, 6))
    6
    >>> calc_distance((1, 1), (1, 1))
    0
    '''
    ax, ay = a
    bx, by = b
    return abs(ax-bx) + abs(ay-by)

def get_playground(points):
    '''
    >>> get_playground(parse_input(example_input()))
    ((1, 1), (8, 9))
    '''
    minx = 1000000000000
    maxx = -minx
    miny = minx
    maxy = maxx
    for x, y in points:
        if minx > x:
            minx = x
        if miny > y:
            miny = y
        if maxx < x:
            maxx = x
        if maxy < y:
            maxy = y
    return ((minx, miny), (maxx, maxy))

def which_point_is_closest(pos, points):
    '''
    >>> which_point_is_closest((1, 1), parse_input(example_input()))
    (1, 1)
    '''
    min_distance = None
    closest_point = None
    for point in points:
        distance = calc_distance(pos, point)
        if min_distance is None or min_distance > distance:
            min_distance = distance
            closest_point = point

    return closest_point

def compute_an_area(pos, data, playground):
    '''
    >>> compute_an_area((3, 4), parse_input(example_input()), ((1, 1), (8, 9)))
    9
    '''
    (ax, ay), (bx, by) = playground
    closest = 0
    for x in range(ax, bx):
        for y in range(ay, by):
            if pos == which_point_is_closest((x, y), data):
                closest += 1
    return closest

def compute_areas(data):
    '''
    >>> compute_areas(parse_input(example_input()))
    [((3, 4), 9), ((5, 5), 17)]
    '''
    inner = find_inner_coords(data)
    playground = get_playground(data)
    results = []
    for pos in inner:
        results.append((pos, compute_an_area(pos, data, playground)))
    return results

def find_max_area(areas):
    '''
    >>> find_max_area([((3, 4), 9), ((5, 5), 17)])
    17
    '''
    min_area = None
    for p, area in areas:
        if min_area is None or area > min_area:
            min_area = area
    return min_area

def sum_distances_from_point(pos, points):
    '''
    >>> sum_distances_from_point((4, 3), parse_input(example_input()))
    30
    '''
    distance = 0
    for point in points:
        distance += calc_distance(pos, point)

    return distance

def compute_area_with_max_distance(max_distance, points):
    '''
    >>> compute_area_with_max_distance(32, parse_input(example_input()))
    16
    '''
    (ax, ay), (bx, by) = get_playground(points)
    area = 0
    for x in range(ax, bx):
        for y in range(ay, by):
            if max_distance > sum_distances_from_point((x, y), points):
                area += 1
    return area

def main():
    '''
    >>> main()
    Example A: 17
    Part A: 5626
    Example B: 16
    Part B: 46554
    '''
    data = example_input()
    areas = compute_areas(parse_input(data))
    print('Example A:', find_max_area(areas))

    data = get_input()
    areas = compute_areas(parse_input(data))
    print('Part A:', find_max_area(areas))

    print('Example B:', compute_area_with_max_distance(32, parse_input(example_input())))
    print('Part B:', compute_area_with_max_distance(10000, parse_input(get_input())))

if __name__ == '__main__':
    main()
