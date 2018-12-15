# -*- coding: utf-8 -*-
"""
HackerRank - Greedy Florist
https://www.hackerrank.com/challenges/greedy-florist

Created on Sat Dec 15 13:51:20 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Sort and iteration over input array.

    Time complexity: O(n * log(n))
        - Amortized sort input array in-place
    Space complexity: O(1)
        - Update constant number of pointers and sort array in-place
    """

    def find_minimum_cost(self, m, k, a):
        """
        Determines minimum cost of "n" flowers by "k" people.

        :param int m: number of flowers to purchase
        :param int k: number of people to purchase flowers
        :param list[int] a: input array of integers as flower prices
        :return: minimum cost for flowers
        :rtype: int
        """
        if not a:
            return 0

        # Sort input array with largest values in front
        a.sort(reverse = True)

        # Initialize pointers for multiplier counter and value
        i = k
        f = 1

        p = 0
        for j in range(0, m, 1):

            p += a[j] * f
            i -= 1

            if i == 0:
                # Increase cost multiplier value and reset counter
                f += 1
                i = k

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: numbers of flowers and people and input array of costs
        :rtype: tuple[int, int, list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        m, k = [int(x)
                for x
                in inputs[0].split()]

        if inputs[1] == "":
            a = list()
        else:
            a = [int(x)
                 for x
                 in inputs[1].split()]

        return m, k, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    m, k, a = Input()\
              .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_minimum_cost(m, k, a)
    print(z)


## END OF FILE