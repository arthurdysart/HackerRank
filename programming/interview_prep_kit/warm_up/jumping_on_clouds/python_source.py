# -*- coding: utf-8 -*-
"""
HackerRank - Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds

Created on Mon Nov 12 21:23:14 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all characters in array.
    Time complexity: O(n)
        - Traverse array with at least one single-space jump
    Space complexity: O(1)
        - Requires constant number of pointers
    """

    def jump_clouds(self, n, a):
        """
        Determine minimum number of jumps to traverse array.

        :param int n: number of elements in array
        :param list[int] a: array of safe and dangerous spaces
        :return: minimum number of movements to traverse array
        :rtype: int
        """
        if (not n or
            not a):
            return -1

        # Initialize jump counter and location pointer
        c = 0
        p = 0
        while p < n - 3:
            if a[p + 2] == 0:
                # Complete two jumps
                p += 2
                c += 1
            elif a[p + 1] == 0:
                # Complete one jump
                p += 1
                c += 1
            else:
                return -1
        # Complete final jump
        return c + 1

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: length of array and input array
        :rtype: tuple[int, list[int]]
        """
        inputs = [x for x in sys_stdin]
        n = int(inputs[0])
        a = [int(x) for x in inputs[1].split()]
        return n, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, a = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .jump_clouds(n, a)
    print(z)


## END OF FILE