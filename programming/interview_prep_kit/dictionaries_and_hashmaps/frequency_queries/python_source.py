# -*- coding: utf-8 -*-
"""
HackerRank - Frequency Queries
https://www.hackerrank.com/challenges/frequency-queries

Created on Sun Dec  9 14:01:48 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import defaultdict
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterate over all elements in input array.

    Time complexity: O(n)
        - Iterate over all elements in input array
    Space complexity: O(max(n, k))
        - Amortized collect all elements in hash maps
    """

    def eval_freq_queries(self, a):
        """
        Executes queries and evaluates presence of target frequences.

        :param list[tup[int, int]] a: array of queries as integer tuples
        :return: array of integer results from target frequency evaluation
        :rtype: list[int]
        """
        if not a:
            return list()

        t = list()

        # Initialize value-frequency and frequency-presence hash maps
        d = defaultdict(int)
        f = defaultdict(int)

        for i, v in a:

            if i == 1:
                # Add target value to hash maps

                if f[d[v]] > 0:
                    # Remove element from frequency hash map
                    f[d[v]] -= 1

                d[v] += 1
                f[d[v]] += 1

            elif (i == 2 and
                  d[v] > 0):
                # Remove target value from hash maps

                f[d[v]] -= 1

                d[v] -= 1
                f[d[v]] += 1

            elif i == 3:
                # Evaluate whether target frequency is present

                if f[v] > 0:
                    t.append(1)

                else:
                    t.append(0)

        return t

class Solution2:
    """
    Iterate over all elements in input array.

    Time complexity: O(n)
        - Iterate over all elements in input array
    Space complexity: O(max(n, k))
        - Amortized iterate over all items in frequency-presence hash map
    """

    def eval_freq_queries(self, a):
        """
        Executes queries and evaluates presence of target frequences.

        :param list[tup[int, int]] a: array of queries as integer tuples
        :return: array of integer results from target frequency evaluation
        :rtype: list[int]
        """
        if not a:
            return list()

        t = list()
        d = defaultdict(int)

        # Create hash map of code-operation pairs
        o = {1: (lambda x, d = d: d.update([(x, d[x] + 1)])),

             2: (lambda x, d = d: d.update([(x, d[x] - 1)])
                                  if d[0] >= 0
                                  else None),

             3: (lambda x, d = d, t = t: t.append(1)
                                         if x in d.values()
                                         else t.append(0))}

        for i, v in a:
            o[i](v)

        return t

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of queries as integer tuples
        :rtype: list[tup[int, int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n = int(inputs[0])

        a = [self.cast_tup(inputs[x])
             for x
             in range(1, n + 1, 1)]

        return a

    def cast_tup(self, sub_input):
        """
        Transforms target input string into tuple of integers.

        :param int x: target array index
        :param str sub_input: target string from standard input
        :return: tuple of parsed integers
        :rtype: tup[int, int]
        """
        if not sub_input:
            return tuple()

        t = tuple(int(x)
                  for x
                  in sub_input.split())

        return t


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .eval_freq_queries(a)
    print(*z,
          sep = "\n")


## END OF FILE