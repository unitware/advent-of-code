#!/usr/env python

'''
--- Day 4: Repose Record ---
You've sneaked into another supply closet - this time, it's across from the prototype suit manufacturing lab. You need to sneak inside and fix the issues with the suit, but there's a guard stationed outside the lab, so this is as close as you can safely get.

As you search the closet for anything that might help, you discover that you're not the first person to want to sneak in. Covering the walls, someone has spent an hour starting every midnight for the past few months secretly observing this guard post! They've been writing down the ID of the one guard on duty that night - the Elves seem to have decided that one guard was enough for the overnight shift - as well as when they fall asleep or wake up while at their post (your puzzle input).

For example, consider the following records, which have already been organized into chronological order:

[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.

Visually, these records show that the guards are asleep at these times:

Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.

Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).

While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

--- Part Two ---
Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)
'''

import operator
import textwrap


def get_input(filename='2018/4/input.txt'):
    with open(filename) as fil:
        for line in fil.readlines():
            yield line

class GuardSleep():
    '''
    Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.
    >>> print(GuardSleep(10).falls('00:05').wakes('00:25'))
    10: 20
    >>> print(GuardSleep(10).falls('00:05').wakes('00:25').falls('00:30').wakes('00:55'))
    10: 45
    '''
    def __init__(self, guard):
        self.guard = guard
        self.sleeps = []
        self.fell_time = None
        self.total = 0
        self._histogram = None

    def falls(self, time):
        self.fell = int(time[-2:])
        return self

    def wakes(self, time):
        awoke = int(time[-2:])
        self.sleeps.append((self.fell, awoke))
        self.total += awoke - self.fell
        return self

    def histogram(self):
        '''
        >>> GuardSleep(1).falls('00:01').wakes('00.03').sleeps
        [(1, 3)]
        >>> GuardSleep(1).falls('00:01').wakes('00.03').histogram()._histogram
        {1: 1, 2: 1}
        >>> GuardSleep(1).falls('00:01').wakes('00.04').falls('00:02').wakes('00.03').sleeps
        [(1, 4), (2, 3)]
        >>> GuardSleep(1).falls('00:01').wakes('00.04').falls('00:02').wakes('00.03').histogram()._histogram
        {1: 1, 2: 2, 3: 1}
        '''
        self._histogram = {}
        for f, a in self.sleeps:
            for minute in range(f,a):
                try:
                    self._histogram[minute] += 1
                except KeyError:
                    self._histogram[minute] = 1
        return self

    def max_minute(self):
        '''
        >>> GuardSleep(1).falls('00:01').wakes('00.04').falls('00:02').wakes('00.03').max_minute()
        2
        >>> GuardSleep(1).falls('00:01').wakes('00.04').falls('00:02').wakes('00.03').falls('00:03').wakes('00.06').falls('00:05').wakes('00.07').falls('00:03').wakes('00.04').max_minute()
        3
        '''
        if not self._histogram:
            self.histogram()
        if not self._histogram:
            return 0
        return max(self._histogram.items(), key=operator.itemgetter(1))[0]

    def max_minute_value(self):
        if not self._histogram:
            self.histogram()
        if not self._histogram:
            return 0
        return self._histogram[self.max_minute()]

    def __str__(self):
        return f'{self.guard}: {self.total}'


def create_guard_database(watchlist):
    guards = {}
    current = None
    for date, time, guard, op in watchlist:
        if op == 'Guard':
            current = guards.get(guard, GuardSleep(guard))
            guards[guard] = current
        else:
            getattr(current, op)(time)
    return guards

def assingment_a(lines):
    watchlist = sorted(map(parse, lines))
    guards = create_guard_database(watchlist)

    maximum = None
    for guard in guards:
        if not maximum:
            maximum = guards[guard]

        if guards[guard].total > maximum.total:
            maximum = guards[guard]

    return maximum.guard, maximum.max_minute(), maximum.guard * maximum.max_minute()

def assignment_b(lines):

    watchlist = sorted(map(parse, lines))
    guards = create_guard_database(watchlist)
    maximum = None

    for guard in guards:
        if not maximum:
            maximum = guards[guard]

        if guards[guard].max_minute_value() > maximum.max_minute_value():
            maximum = guards[guard]

    return maximum.guard, maximum.max_minute(), maximum.guard * maximum.max_minute()


def test_example():
    '''
    >>> test_example()
    (10, 24, 240)
    (99, 45, 4455)
    '''
    lines = textwrap.dedent(
    '''[1518-11-01 00:00] Guard #10 begins shift
    [1518-11-01 00:05] falls asleep
    [1518-11-01 00:25] wakes up
    [1518-11-01 00:30] falls asleep
    [1518-11-01 00:55] wakes up
    [1518-11-01 23:58] Guard #99 begins shift
    [1518-11-02 00:40] falls asleep
    [1518-11-02 00:50] wakes up
    [1518-11-03 00:05] Guard #10 begins shift
    [1518-11-03 00:24] falls asleep
    [1518-11-03 00:29] wakes up
    [1518-11-04 00:02] Guard #99 begins shift
    [1518-11-04 00:36] falls asleep
    [1518-11-04 00:46] wakes up
    [1518-11-05 00:03] Guard #99 begins shift
    [1518-11-05 00:45] falls asleep
    [1518-11-05 00:55] wakes up
    ''')
    print(assingment_a(lines.splitlines()))
    print(assignment_b(lines.splitlines()))


def parse(line):
    '''
    >>> parse('[1518-11-01 00:00] Guard #10 begins shift')
    ('11-01', '00:00', 10, 'Guard')
    >>> parse('[1518-11-01 00:05] falls asleep')
    ('11-01', '00:05', None, 'falls')
    >>> parse('[1518-11-01 00:25] wakes up')
    ('11-01', '00:25', None, 'wakes')

    >>> sorted(map(parse, ['[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-01 00:25] wakes up', '[1518-11-01 00:05] falls asleep']))
    [('11-01', '00:00', 10, 'Guard'), ('11-01', '00:05', None, 'falls'), ('11-01', '00:25', None, 'wakes')]
    '''
    line = line.split()
    date = line[0][-5:]
    time = line[1][:5]
    op = line[2]
    guard = int(line[3][1:]) if op == 'Guard' else None
    return date, time, guard, op


def main():
    '''
    >>> main()
    part A:  (2753, 28, 77084)
    part B:  (1213, 19, 23047)
    '''

    if False:
        watchlist = sorted(map(parse, get_input()))

        #verify that sleeps occur during midnight hour
        for date, time, guard, op in watchlist:
            if op == 'falls' or op == 'wakes':
                if time[:3] != '00:':
                    print(date, time)

    print('part A: ', assingment_a(get_input()))
    print('part B: ', assignment_b(get_input()))

if __name__ == '__main__':
    main()
