#!/usr/bin/python

'''
--- Day 5: Alchemical Reduction ---
You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)

--- Part Two ---
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
'''
import operator

def get_input(filename='2018/5/input.txt'):
#    output = ''
    with open(filename) as fil:
        for stuff in fil.read():
            for c in stuff:
                yield c
 #           output += stuff
 #   return list(output)

def same_material(a, b):
    '''
    >>> same_material('a', 'b')
    False
    >>> same_material('A', 'b')
    False
    >>> same_material('a', 'A')
    True
    >>> same_material('A', 'A')
    True
    '''
    return a.lower() == b.lower()

def reacts_with(a, b):
    '''
    >>> reacts_with('a', 'a')
    False
    >>> reacts_with('a', 'A')
    True
    >>> reacts_with('a', 'B')
    False
    '''
    return same_material(a, b) and a != b

def reduce_one_pass(data, remove_material=None):
    '''
    >>> reduce_one_pass('dabAcCaCBAcCcaDA')
    'dabAaCBAcaDA'
    >>> reduce_one_pass('dabAcCaCBAcCcaDA', 'a')
    'dbCBcD'
    >>> reduce_one_pass('dabCBAcCcaDA')
    'dabCBAcaDA'
    >>> reduce_one_pass('dabCBAcaDA')
    'dabCBAcaDA'
    >>> reduce_one_pass('dabAaCBAcCcaDA')
    'dabCBAcaDA'
    '''
    output = ''
    skip = True
    for nxt in data:
        if remove_material and nxt.lower() == remove_material.lower():
            continue
        # print(output, c, nxt)
        if skip:
            skip = False
        elif not reacts_with(c, nxt):
            output += c
        else:
            skip = True
        c = nxt
    if not skip:
        output += c
    return output

def reduce_all(data, remove_material=None):
    '''
    >>> reduce_all('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    '''
    last_len = 1
    length = 0
    while last_len != length:
        data = reduce_one_pass(data, remove_material)
        last_len = length
        length = len(data)
    return data

def test_material_remove(data, material):
    '''
    >>> test_material_remove('dabAcCaCBAcCcaDA', 'a')
    ('dbCBcD', 6)
    >>> test_material_remove('dabAcCaCBAcCcaDA', 'b')
    ('daCAcaDA', 8)
    >>> test_material_remove('dabAcCaCBAcCcaDA', 'c')
    ('daDA', 4)
    >>> test_material_remove('dabAcCaCBAcCcaDA', 'd')
    ('abCBAc', 6)
    '''
    data = reduce_all(data, material)
    return data, len(data)
def get_materials(data):
    '''
    >>> get_materials('aCbBd')
    'abcd'
    '''
    materials = ''
    for c in data:
        if c.lower() not in materials:
            materials += c.lower()
    return ''.join(sorted(materials))


def main():
    '''
    >>> main()
    Part A: 11252
    Part B: n 6118
    '''
    data = get_input()
    resultA = reduce_all(data).strip()

    print('Part A:', len(resultA))

    results = {}
    for m in get_materials(resultA):
        results[m] = len(reduce_all(resultA, m))

    minimum = min(results.items(), key=operator.itemgetter(1))[0]
    print('Part B:', minimum, results[minimum])


if __name__ == '__main__':
    main()
