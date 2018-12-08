# -*- coding: utf-8 -*-
"""
HackerRank - New Year Chaos
https://www.hackerrank.com/challenges/new-year-chaos

Created on Sat Dec  8 13:06:33 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration using bubble sort algorithm (with optimized exit condition).

    Time complexity: O(n ** 2)
        - Amortized iterate over array elements at most "n" times
    Space complexity: O(n)
        - Update array for bribe counts
    """

    def find_min_bribes(self, A):
        """
        Modifies input array using specified number of left rotations.

        :param list[tup[int, list[int]]] A: array of subproblem parameters
        :return: array of subproblem results
        :rtype: list[int or str]
        """
        if not A:
            return list()

        N = len(A)

        Z = [self.count_bribes(*A[x])
             for x
             in range(0, N, 1)]

        return Z

    def count_bribes(self, n, a):
        """
        Determines number of bribes required to create input sequence.
        Interpolates bubble sort algorithm.

        :param int n: number of elements in input array
        :param list[int] a: input array of integers
        :return: number of required bribes or error result
        :rtype: int or str
        """
        if (not n or
            not a):
            return 0

        # Initialize counter for bribes
        b = [0 for x in range(0, n, 1)]

        for j in range(0, n, 1):
            # Reset flag for correctly ordered elements
            is_sorted = True

            for i in range(0, n - j - 1, 1):

                if a[i] > a[i + 1]:
                    # Found target value which requires bribe

                    if b[a[i] - 1] == 2:
                        # Found target value with too many bribes
                        return "Too chaotic"

                    else:
                        # Set flag requiring additional sorting
                        is_sorted = False
                        # Increase number of bribes for target value
                        b[a[i] - 1] += 1
                        # Swap target value with next value
                        a[i], a[i + 1] = a[i + 1], a[i]

            if is_sorted:
                # No additional bribes required
                return sum(b)

        return sum(b)

class Solution2:
    """
    Iteration using bubble sort algorithm.

    Time complexity: O(n ** 2)
        - Amortized iterate over array elements at most "n" times
    Space complexity: O(n)
        - Update array for bribe counts
    """

    def find_min_bribes(self, A):
        """
        Modifies input array using specified number of left rotations.

        :param list[tup[int, list[int]]] A: array of subproblem parameters
        :return: array of subproblem results
        :rtype: list[int or str]
        """
        if not A:
            return list()

        N = len(A)

        Z = [self.count_bribes(*A[x])
             for x
             in range(0, N, 1)]

        return Z

    def count_bribes(self, n, a):
        """
        Determines number of bribes required to create input sequence.
        Interpolates bubble sort algorithm.

        :param int n: number of elements in input array
        :param list[int] a: input array of integers
        :return: number of required bribes or error result
        :rtype: int or str
        """
        if (not n or
            not a):
            return 0

        # Initialize counter for bribes
        b = [0 for x in range(0, n, 1)]

        # Execute bubble sort
        for j in range(0, n, 1):
            for i in range(0, n - j - 1, 1):

                if a[i] > a[i + 1]:
                    # Found target value which requires bribe

                    if b[a[i] - 1] == 2:
                        # Found target value with too many bribes
                        return "Too chaotic"

                    else:
                        # Increase number of bribes for target value
                        b[a[i] - 1] += 1
                        # Swap target value with next value
                        a[i], a[i + 1] = a[i + 1], a[i]

        return sum(b)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of subproblem parameters
        :rtype: list[tup[int, list[int]]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        A = [self.collect_param(x, inputs)
             for x
             in range(0, int(inputs[0]), 1)]
        
        return A

    def collect_param(self, x, inputs):
        """
        Collects sets of parameters from standard input.
        
        :param int x: index of subproblem parameters
        :param list[str]: array of raw strings from standard input
        :return: number of elements and corresponding subproblem array
        :rtype: tup[int, list[int]]        
        """
        
        n = int(inputs[2 * x + 1])

        if inputs[2 * x + 2] == "":
            a = list([list()])
        else:
            a = [int(x)
                 for x
                 in inputs[2 * x + 2].split()]

        return n, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    A = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    Z = Solution()\
        .find_min_bribes(A)
    print(*Z,
          sep = "\n")


## END OF FILE