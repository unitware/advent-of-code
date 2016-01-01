#!/usr/bin/python3

'''
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a 
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed 
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights 
at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights 
by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

'''

import doctest

EXAMPLES = [
        ('turn on 0,0 through 0,0', 1),
        ('toggle 0,0 through 999,999', 2000000)
    ]


class light:
    def __init__(self):
        self.state = 0

    def turn_on(self):
        self.state += 1 

    def turn_off(self):
        if self.state > 0:
            self.state -= 1


    def toggle(self):
        self.state += 2

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)


class light_array:
    array = None

    def __init__(self, n=1000):
        '''
        >>> light_array(2).array
        [[0, 0], [0, 0]]
        '''
        self.array = []
        for y in range(n):
            line = []
            for x in range(n):
                line.append(light())
            self.array.append(line)


    def _split_command(self, line):
        '''
        >>> light_array()._split_command('turn on 1,2 through 3,4')
        ('turn on', (1, 2), (3, 4))
        >>> light_array()._split_command('turn off 1,2 through 3,4')
        ('turn off', (1, 2), (3, 4))
        >>> light_array()._split_command('toggle 1,2 through 3,4')
        ('toggle', (1, 2), (3, 4))
        '''
        for cmd in ['turn on', 'turn off', 'toggle']:
            if cmd in line:
                rest = line[len(cmd):]
                
                #cmd = getattr(__main__, cmd.replace(' ', '_'))

                start, _, stop = rest.split()
                x, y = start.split(',')
                start = (int(x), int(y))

                x, y = stop.split(',')
                stop = (int(x), int(y))

                return cmd, start, stop

        raise Exception('no known command')


    def count_lights(self):
        cnt = 0
        for x in self.array:
            for y in x:
                cnt += y.state

        return cnt


    def execute_command(self, command):
        '''
        >>> array = light_array(2); array.execute_command('turn on 1,1 through 1,1'); array.execute_command('toggle 0,1 through 1,1'); array.array
        [[0, 0], [2, 3]]
        >>> array = light_array(2); array.execute_command('toggle 1,1 through 1,1');  array.array
        [[0, 0], [0, 2]]
        '''
        cmd, start, stop = self._split_command(command)
        x1, y1 = start
        x2, y2 = stop
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                getattr(self.array[y][x], cmd.replace(' ', '_'))()




def main():
    doctest.testmod()
    
    for data, num in EXAMPLES:
        array = light_array()
        array.execute_command(data)
        assert num == array.count_lights()
        print('ok')

    array = light_array()
    with open('input.txt') as fil:
        for line in fil.readlines():
            array.execute_command(line)

    cnt = array.count_lights()
    print(cnt)
    assert cnt == 15343601


if __name__ == '__main__':
    main()
