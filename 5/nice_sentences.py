#!/usr/bin/python3

'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or 
aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the 
other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), 
a double letter (...dd...), and none of the disallowed substrings.

aaa is nice because it has at least three vowels and a double letter,
even though the letters used by different rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
'''

import hashlib

EXAMPLES = [
        ('ugknbfddgicrmopn', True), 
        ('aaa', True),
        ('jchzalrnumimnmhp', False),
        ('haegwjzuvuyypxyu', False),
        ('dvszwmarrgswjxmb', False)
    ]

def it_contains_at_least_three_vowels(sentence):
    '''
    aeiou only
    >>> it_contains_at_least_three_vowels('abc')
    False
    >>> it_contains_at_least_three_vowels('aei')
    True
    >>> it_contains_at_least_three_vowels('aai')
    True
    >>> it_contains_at_least_three_vowels('aaa')
    True
    >>> it_contains_at_least_three_vowels('aou')
    True
    '''
    vows = 0
    for vowel in 'aeiou':
        vows += sentence.count(vowel)

    return vows >= 3


def it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row(sentence):
    '''
    >>> it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row('abc')
    False
    >>> it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row('abbc')
    True
    >>> it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row('abcc')
    True
    >>> it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row('aabc')
    True
    '''
    for i in range(len(sentence) - 1):
        if sentence[i] == sentence[i+1]:
            return True

    return False


def it_does_contain_any_of_the_strings_ab_cd_pq_or_xy(sentence):
    '''
    >>> it_does_contain_any_of_the_strings_ab_cd_pq_or_xy('aaa')
    False
    >>> it_does_contain_any_of_the_strings_ab_cd_pq_or_xy('abc')
    True
    >>> it_does_contain_any_of_the_strings_ab_cd_pq_or_xy('acd')
    True
    '''
    for pattern in ['ab', 'cd', 'pq', 'xy']:
        if pattern in sentence:
            return True

    return False


def sentence_is_nice(sentence):
    nice = False
    if it_contains_at_least_three_vowels(sentence) and \
       it_contains_at_leas_one_letter_that_is_repeated_twice_in_a_row(sentence):
       nice = True
       
    if it_does_contain_any_of_the_strings_ab_cd_pq_or_xy(sentence):
        nice = False

    return nice

def main():
    for data, nice in EXAMPLES:
        assert nice == sentence_is_nice(data)
        print('ok')

    num_nice = 0
    with open('input.txt') as fil:
        for line in fil.readlines():
            if sentence_is_nice(line):
                num_nice += 1

    print(num_nice)


if __name__ == '__main__':
    main()
