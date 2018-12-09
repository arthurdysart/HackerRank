# -*- coding: utf-8 -*-
"""
HackerRank - Minimum Absolute Difference in an Array
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

Created on Sun Dec  9 00:23:41 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Sort and iteration over array.

    Time complexity: O(n * log(n))
        - Amortized sort input array and iterate over array elements
    Space complexity: O(1)
        - Update constant number of pointers and sort array in-place
    """

    def find_min_abs_diff(self, n, a):
        """
        Determines minimum absolute difference between array elements.

        :param list[int] a: input array of integers
        :return: minimum absolute difference in array
        :rtype: int
        """
        if not a:
            return 0

        a.sort()

        p = float("inf")

        for i in range(0, n - 1, 1):

            p = min(abs(a[i] - a[i + 1]),
                    p)

        if p == float("inf"):
            return 0
        else:
            return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
        :rtype: list[int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n = int(inputs[0])

        if inputs[1] == "":
            a = list([list()])
        else:
            a = [int(x)
                 for x
                 in inputs[1].split(" ")]

        return n, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, a = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_min_abs_diff(n, a)
    print(z)


## END OF FILE