# -*- coding: utf-8 -*-
"""
HackerRank - Two Strings
https://www.hackerrank.com/challenges/two-strings

Created on Sun Dec  9 11:21:29 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import defaultdict
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterate over all elements in input strings.

    Time complexity: O(max(n, m))
        - Amortized iterate over all elements in both input strings
    Space complexity: O(min(n, m))
        - Collect elements from shortest input string
    """

    def eval_str_pairs(self, A):
        """
        Evaluates possible common substring for all input string pairs.

        :param list[tup[str, str]] A: array of tuples of input string pairs
        :return: array of result strings
        :rtype: list[str]
        """
        if not A:
            return list()

        N = len(A)

        Z = [self.eval_substrings(*A[i])
             for i
             in range(0, N, 1)]

        return Z

    def eval_substrings(self, s1, s2):
        """
        Determines whether input strings share at least one common substring.

        :param str s1: first input string
        :param str s2: Second input string
        :return: string representing if strings share common substring
        :rtype: str
        """
        if (not s1 and
            not s2):
            return "YES"

        elif (not s1 or
              not s2):
            return "NO"

        if len(s1) > len(s2):
            # Set shortest (u) and longest (v) strings
            u = s2
            v = s1
        else:
            u = s1
            v = s2

        a = defaultdict(bool)

        for c in u:
            # Collect all elements of shortest string
            a[c] = True

        for c in v:
            # Iterate over longest string
            if a[c]:
                return "YES"

        # Found no common substring
        return "NO"

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: number of elements and arrays for input and target strings
        :rtype: tup[int, int, list[str], list[str]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n = int(inputs[0])

        A = [self.cast_tup(x, inputs)
             for x
             in range(0, n, 1)]

        return A

    def cast_tup(self, x, inputs):
        """
        Transforms target input strings into tuple of strings.

        :param int x: target array index
        :param list[int or str] inputs: array of standard input
        :return: tuple of target strings
        :rtype: tup[str, str]
        """
        if not inputs:
            return tuple(["", ""])
        
        n = len(inputs)

        if 2 * x + 1 < n:
            s1 = inputs[2 * x + 1]\
                 .strip("\" ")
        else:
            s1 = ""

        if 2 * x + 2 < n:
            s2 = inputs[2 * x + 2]\
                 .strip("\" ")
        else:
            s2 = ""

        return tuple([s1, s2])


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    A = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    Z = Solution()\
        .eval_str_pairs(A)
    print(*Z,
          sep = "\n")


## END OF FILE