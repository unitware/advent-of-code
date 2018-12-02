#!/usr/env python

def get_input(filename='2018/2/input.txt'):
    with open(filename) as fil:
        lines = fil.readlines()

    return lines

def count_c_in_str(c, string):
    '''
    >>> count_c_in_str('a', 'abc')
    1
    >>> count_c_in_str('a', 'apa')
    2
    '''
    count = 0
    for tmp in string:
        if c == tmp:
            count += 1
    return count

def calc_checksum(identifier):
    '''
    >>> calc_checksum('abcdef')
    (0, 0)
    >>> calc_checksum('bababc')
    (1, 1)
    >>> calc_checksum('abbcde')
    (1, 0)
    >>> calc_checksum('abcccd')
    (0, 1)
    >>> calc_checksum('aabcdd')
    (1, 0)
    >>> calc_checksum('abcdee')
    (1, 0)
    >>> calc_checksum('ababab')
    (0, 1)
    '''
    twos = 0
    threes = 0

    while identifier:
        char = identifier[0]
        identifier = identifier[1:]

        count = count_c_in_str(char, identifier)

        if count == 0:
            continue
        elif count == 1:
            twos = 1
        elif count == 2:
            threes = 1

        identifier = [x for x in identifier if x != char]

    return (twos, threes)

def sum_all_checksums(checksums):
    '''
    >>> sum_all_checksums([(0,0), (1,0)])
    (1, 0)
    >>> sum_all_checksums([(0,2), (1,0)])
    (1, 2)
    >>> sum_all_checksums([(3,4), (5,6)])
    (8, 10)
    '''
    twos, threes = (0,0)
    for a,b in checksums:
        twos += a
        threes += b
    return twos, threes


def stripped(a, b):
    '''
    >>> stripped('apa', 'aba')
    'aa'
    >>> stripped('abcd', 'abce')
    'abc'
    '''
    res = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            res += a[i]
    return res

def diff(a, b):
    '''
    >>> diff('a', 'a')
    0
    '''
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d

def find_close(ids):
    '''
    >>> find_close(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'])
    'fgij'
    '''
    for a in ids:
        for b in [b for b in ids if b != a]:
            if diff(a, b) == 1:
                return stripped(a, b)
    return None

def main():
    identifiers = get_input()
    checksums = map(calc_checksum, identifiers)
    a,b = sum_all_checksums(checksums)
    print(a*b)
    print(find_close(identifiers))
    
if __name__ == '__main__':
    main()
