#!/usr/bin/python

'''
--- Day 7: The Sum of Its Parts ---
You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
Visually, these requirements look like this:


  -->A--->B--
 /    \\      \
C      -->D----->E
 \\           /
  ---->F-----
Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:

Only C is available, and so it is done first.
Next, both A and F are available. A is first alphabetically, so it is done next.
Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
F is the only choice, so it is done next.
Finally, E is completed.
So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

--- Part Two ---
As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .
   1        C          .
   2        C          .
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE
Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these steps.

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?
'''

import textwrap

def get_input(filename='2018/7/input.txt'):
    with open(filename) as fil:
        for line in fil.readlines():
            yield line

def example_input():
    for line in textwrap.dedent(
        '''Step C must be finished before step A can begin.
        Step C must be finished before step F can begin.
        Step A must be finished before step B can begin.
        Step A must be finished before step D can begin.
        Step B must be finished before step E can begin.
        Step D must be finished before step E can begin.
        Step F must be finished before step E can begin.
        ''').splitlines():
        yield line


def parse_input(data):
    '''
    >>> parse_input(example_input())
    [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
    '''
    output = []
    for line in data:
        line = line.split()
        pre = line[1]
        nxt = line[7]
        output.append((pre, nxt))
    return output

def build_graph(steps):
    '''
    >>> build_graph(parse_input(example_input()))
    {'C': ['A', 'F'], 'A': ['B', 'D'], 'F': ['E'], 'B': ['E'], 'D': ['E'], 'E': []}
    '''
    graph = {}
    for pre, nxt in steps:
        if pre in graph:
            graph[pre].append(nxt)
        else:
            graph[pre] = [nxt]
        if not nxt in graph:
            graph[nxt] = []
    return graph

def is_blocked(node, graph):
    '''
    >>> is_blocked('A', build_graph(parse_input(example_input())))
    True
    >>> is_blocked('C', build_graph(parse_input(example_input())))
    False
    '''
    for a, pre in graph.items():
        for p in pre:
            if p == node:
                return True
    return False

def free_to_build(graph):
    '''
    >>> free_to_build(build_graph(parse_input(example_input())))
    ['C']
    '''
    free = []
    for node in graph:
        if not is_blocked(node, graph):
            free += node
    return free

def build_sleigh(graph):
    '''
    >>> build_sleigh(build_graph(parse_input(example_input())))
    'CABDFE'
    '''
    sequence = ''
    while graph:
        node = sorted(free_to_build(graph))[0]
        sequence += node
        del(graph[node])

    return sequence

def work_to_do(node, base_time=0):
    '''
    >>> work_to_do('A')
    1
    >>> work_to_do('Z')
    26
    >>> work_to_do('A', 60)
    61
    >>> work_to_do('Z', 60)
    86
    '''
    return ord(node) - ord('A') + 1 + base_time

def in_progress(node, workers):
    for work in workers:
        if work['node'] == node:
            return True
    return False

def build_sleigh_with_workers(num_workers, graph, base_time=0):
    '''
    >>> build_sleigh_with_workers(2, build_graph(parse_input(example_input())), 0)
    (15, 'CABFDE')
    '''
    workers = [{'node': None, 'remain': 0} for _ in range(num_workers)] #{node, sec_remaining}
    sequence = ''
    time = 0
    while graph:
        for work in workers:
            if work['remain']:
                work['remain'] -= 1

            if work['node'] and not work['remain']:
                #work on node is done
                del(graph[work['node']])
                sequence += work['node']
                work['node'] = None

        for work in workers:
            if not work['node']:
                nodes = sorted(free_to_build(graph))
                for node in nodes:
                    if not in_progress(node, workers):
                        work['node'] = node
                        work['remain'] = work_to_do(node, base_time)
                        break
        time += 1
    return time-1, sequence

def main():
    '''
    >>> main()
    Example A: CABDFE
    Part A: CGKMUWXFAIHSYDNLJQTREOPZBV
    Example B: 15
    Part B: 1046
    '''
    print('Example A:', build_sleigh(build_graph(parse_input(example_input()))))
    print('Part A:', build_sleigh(build_graph(parse_input(get_input()))))
    eb, _ = build_sleigh_with_workers(2, build_graph(parse_input(example_input())), 0)
    print('Example B:', eb)
    eb, _ = build_sleigh_with_workers(5, build_graph(parse_input(get_input())), 60)
    print('Part B:', eb)

#    data = get_input()

if __name__ == '__main__':
    main()
