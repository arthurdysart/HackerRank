# -*- coding: utf-8 -*-
"""
HackerRank - Repeated String
https://www.hackerrank.com/challenges/repeated-string

Created on Mon Nov 12 22:05:52 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all characters in string.
    Time complexity: O(len(s))
        - Traverse string to identify "a" characters
    Space complexity: O(1)
        - Requires constant number of pointers
    """

    def count_repeated_string(self, s, x):
        """
        Determine minimum number of jumps to traverse array.

        :param int x: number of times to repeat string
        :param str s: string which infinitely repeats
        :return: total number of "a" characters in repeated string
        :rtype: int
        """
        if (not x or
            not s):
            return -1

        # Calculate multiplier and string remainder
        f, r = divmod(x, len(s))

        e = sum(1 for c in s[:r] if c == "a")
        p = sum(1 for c in s if c == "a")

        return f * p + e
            

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: repeated string and number of queried elements
        :rtype: tuple[str, int]
        """
        inputs = [x for x in sys_stdin]
        s = inputs[0].strip()
        x = int(inputs[1])
        return s, x


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    s, x = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_repeated_string(s, x)
    print(z)


## END OF FILE