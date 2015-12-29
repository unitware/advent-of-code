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


-----
step 2

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

'''

EXAMPLES = [
        ('qjhvhtzxzqqjkmpb', True),
        ('xxyxx', True),
        ('uurcxstgmygtbstg', False),
        ('ieodomkazucvgmuy', False)
    ]



def it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice(sentence):
    '''
    >>> it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice('xyxy')
    True
    >>> it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice('aabcdefgaa')
    True
    >>> it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice('aaa')
    False
    >>> it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice('ieodomkazucvgmuy')
    False
    '''
    for i in range(len(sentence) - 3):
        if sentence[i+2:].count(sentence[i:i+2]):
            # print(i, sentence[i:i+2], sentence[i+2:])
            return True

    return False

def it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between(sentence):
    '''
    >>> it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between('xyx')
    True
    >>> it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between('abcdefeghi')
    True
    >>> it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between('aaa')
    True
    >>> it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between('abc')
    False
    '''
    for i in range(len(sentence) - 2):
        if sentence[i] == sentence[i+2]:
            return True

    return False

def sentence_is_nice(sentence):
    if it_contains_a_pair_of_any_two_letters_that_appears_at_least_twice(sentence) \
       and it_contains_at_least_one_letter_which_repeats_with_exactly_one_letter_between(sentence):
        return True

    return False


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
