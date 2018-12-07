# -*- coding: utf-8 -*-
"""
HackerRank - Arrays: Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation

Created on Thu Dec  6 22:18:06 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all elements in input array.

    Time complexity: O(n)
        - Traverse array elements
    Space complexity: O(n)
        - Collect updated array
    """

    def rotate_left(self, n, d, a):
        """
        Modify input array using specified number of left rotations.

        :param list[int] a: input array of integers
        :param int d: number of left rotations required
        :return: modified array
        :rtype: list[int]
        """
        if not a:
            return list()
        elif not d:
            return a

        z = a[d:]
        z.extend(a[:d])
        return z

class Solution2:
    """
    Iteration over all elements in input array.

    Time complexity: O(n * d)
        - Traverse array elements
    Space complexity: O(n)
        - Collect updated array
    """

    def rotate_left(self, n, d, a):
        """
        Modify input array using specified number of left rotations.

        :param list[int] a: input array of integers
        :param int d: number of left rotations required
        :return: modified array
        :rtype: list[int]
        """
        if not a:
            return list()
        elif not d:
            return a

        for d in range(0, d, 1):
            a = self.execute_rotation(n, a)

        return a

    def execute_rotation(self, n, a):
        """
        Modify input array by one left rotation.

        :param list[int] a: input array of integers
        :return: modified array
        :rtype: list[int]
        """
        if not a:
            return list()

        p = a[0]

        for i in range(0, n - 1, 1):
            a[i] = a[i + 1]

        a[-1] = p

        return a

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n, d = [int(x)
                for x
                in inputs[0].split()]

        if inputs[0][1] == "":
            a = list([list()])
        else:
            a = [int(x)
                 for x
                 in inputs[1].split()]

        return n, d, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, d, a = Input()\
              .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .rotate_left(n, d, a)
    print(*z,
          sep = " ")


## END OF FILE