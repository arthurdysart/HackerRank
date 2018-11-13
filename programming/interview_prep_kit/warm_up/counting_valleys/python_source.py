# -*- coding: utf-8 -*-
"""
HackerRank - Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys

Created on Mon Nov 12 19:39:34 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all characters in string.
    Time complexity: O(n)
        - Traverse all elevation changes
    Space complexity: O(1)
        - Requires constant number of pointers
    """

    def count_valleys(self, n, s):
        """
        Determine number of valleys in hiker trail.
        
        :param int n: number of steps in trail
        :param str s: string representation of elevation change
        :return: number of valleys
        :rtype: int
        """

        v = 0
        p = 0
        for i in range(n):
            if s[i] == "D":
                if p == 0:
                    # Increment number of valleys
                    v += 1
                # Decrement pointer downhill
                p -= 1
            else:
                # Increment pointer uphill
                p += 1
        return v

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: number and string representation of elevation changes
        :rtype: tuple[int, str]
        """
        inputs = [x for x in sys_stdin]
        n = int(inputs[0])
        s = inputs[1]
        return n, s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, s = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_valleys(n, s)
    print(z)


## END OF FILE