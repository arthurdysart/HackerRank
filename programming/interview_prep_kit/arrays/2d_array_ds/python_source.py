# -*- coding: utf-8 -*-
"""
HackerRank - 2D array - DS
https://www.hackerrank.com/challenges/2d-array

Created on Thu Dec  6 21:57:16 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from itertools import product
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all subarrays in input array.

    Time complexity: O(n * m)
        - Traverse relevant array elements
    Space complexity: O(1)
        - Requires constant number of pointers
    """

    def calc_max_hourglass_sum(self, a):
        """
        Calculate maximum sum for hourglass subsets from input array.

        :param list[int] a: input array
        :return: maximum hourglass sum
        :rtype: int
        """
        if not a:
            return 0

        # Check for insuffient array size
        elif (len(a) < 3 or
              len(a[0]) < 3):
            return 0

        p = float("-inf")

        # Set boundary limits for hourglass center
        n = len(a) - 1
        m = len(a[0]) - 1

        for i in range(1, n, 1):
            for j in range(1, m, 1):

                # Collect maximum sum
                p = max(self.sum_elements(i, j, a),
                        p)

        if p == float("-inf"):
            return 0
        else:
            return p

    def sum_elements(self, i, j, a):
        """
        Calculate sum for input hourglass subset with center (i, j).
        
        :param int i: abcissa for hourglass center
        :param int j: ordinate for hourglass center
        :param list[list[int]] a: input 2D array
        :return: sum of elements in hourglass subset
        :rtype: int
        """
        # Populate options for ordinate and abscissa
        u = (i - 1, i + 1)
        v = (j - 1, j, j + 1)

        # Calculate sum of outer elements
        s = sum(a[x][y]
                for (x, y)
                in product(u, v))

        # Add sum to center element value
        return a[i][j] + s

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\"\n").split(" ")
                  for x
                  in sys_stdin]

        if inputs[0][0] == "":
            a = list([list()])
        else:
            a = [list(map(int, x))
                 for x
                 in inputs]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .calc_max_hourglass_sum(a)
    print(z)


## END OF FILE