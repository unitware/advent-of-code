#!/usr/bin/python3


def calc(values):
    '''
    >>> calc([1])
    1
    >>> calc([1,-2])
    -1
    '''
    freq = 0
    for x in values:
        freq += x
    return freq

def find_frequency(values):
    '''
    >>> find_frequency([-6, +3, +8, +5, -6])
    5
    >>> find_frequency([-1, 1])
    0
    >>> find_frequency([+3, +3, +4, -2, -4])
    10
    >>> find_frequency([+7, +7, -2, -7, -4])
    14
    '''
    histogram = {0: True}
    freq = 0
    while True:
        for x in values:
            freq += x
            if freq in histogram:
                return freq
            else:
                histogram[freq] = True


def get_input(filename='2018/1/input.txt'):
    lines = []
    with open(filename) as fil:
        for line in fil.readlines():
            op = line[0]

            value = int(line[1:].strip())
            lines.append(value if op == '+' else -value)
    return lines

def main():
    print('part a:', calc(get_input()))
    print('part b:', find_frequency(get_input()))

if __name__ == '__main__':
    main()
