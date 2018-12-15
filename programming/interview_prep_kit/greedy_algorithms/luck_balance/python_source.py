# -*- coding: utf-8 -*-
"""
HackerRank - Luck Balance
https://www.hackerrank.com/challenges/luck-balance

Created on Fri Dec 14 22:45:27 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Sort and iteration over input array.

    Time complexity: O(n * k)
        - Amortized sort input array and iterate over array elements
    Space complexity: O(1)
        - Update constant number of pointers and sort array in-place
    """

    def find_max_luck(self, n, k, a):
        """
        Determines maximum luck after optimal contest results.

        :param int n: number of tuples as contests in input array
        :param int k: max number of important contests to lose
        :param list[tuple[int, int]] a: input array of tuples as contests
        :return: maximum final luck after optimal contest results
        :rtype: int
        """
        if not a:
            return 0

        # Sort contests by significance and increasing luck value
        a = self.sort_contests(n, k, a)

        p = 0

        for i in range(0, n, 1):
            # Iterate over sorted contests

            if (a[i][1] == 1 and
                i < n - k):
                # Decrease luck by winning contest with low luck impact
                p -= a[i][0]

            else:
                # Increase luck by losing contest
                p += a[i][0]

        return p

    def sort_contests(self, n, k, a):
        """
        Collects "k" important contests with greatest luck at end of array.
        Interpolates bubble sort algorithm.

        :param int n: number of tuples as contests in input array
        :param int k: max number of important contests to collect
        :param list[tup[int, int]] a: input array of tuples as contests
        :return: updated input array of tuples as contests
        :rtype: list[tuple[int, int]]
        """
        if not a:
            return list()

        for j in range(0, k, 1):

            # Initialize pointer for early sort exit
            is_sorted = True

            for i in range(0, n - j - 1, 1):

                if a[i][1] == 0:
                    # Ignore unimportant contest tuple
                    continue

                elif (a[i + 1][1] == 0 or
                      a[i][0] > a[i + 1][0]):
                    # Swap target and proceeding contest tuple
                    a[i], a[i + 1] = a[i + 1], a[i]

                    is_sorted = False

            if is_sorted:
                # Complete sorting of input array
                return a

        # Complete sorting of input array
        return a

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: number of elements and target elements and input array
        :rtype: tuple[int, int, list[tuple[int, int]]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n, k = [int(x)
                for x
                in inputs[0].split()]

        if n == 0:
            a = list([tuple()])
        else:
            a = [tuple(map(int, inputs[i].split()))
                 for i
                 in range(1, n + 1, 1)]

        return n, k, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, k, a = Input()\
              .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_max_luck(n, k, a)
    print(z)


## END OF FILE