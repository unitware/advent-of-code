#!/usr/env python

'''
--- Day 2: Inventory Management System ---
You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

Your puzzle answer was 4693.

--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

Your puzzle answer was pebjqsalrdnckzfihvtxysomg.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

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
