# -*- coding: utf-8 -*-
"""
HackerRank - Hash Tables: Ransom Note
https://www.hackerrank.com/challenges/ctci-ransom-note

Created on Sun Dec  9 10:27:29 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import defaultdict
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterate over all elements in input and target arrays.

    Time complexity: O(n * m)
        - Amortized iterate over all elements in both input and target arrays
    Space complexity: O(n + m)
        - Collect elements from both input and target arrays using hash maps
    """

    def eval_word_count(self, n, m, a, t):
        """
        Determines whether target array is subset of input array.

        :param int n: number of elements in input array
        :param int m: number of elements in target array
        :param list[str] a: input array of strings
        :param list[str] t: target array of strings
        :return: string representing if target array is subset of input array
        :rtype: str
        """
        if not t:
            return "Yes"

        elif (t and
              not a):
            return "No"

        c = defaultdict(int)

        for i in range(0, n, 1):
            # Populate hash map for input strings
            c[a[i]] += 1

        for j in range(0, m, 1):
            # Iterate over all target strings

            if c[t[j]] > 0:
                # Decement available input string count
                c[t[j]] -= 1

            else:
                # Found unavailable target string
                return "No"

        # Found all target strings
        return "Yes"

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

        n, m = [int(x)
                for x
                in inputs[0].split()]

        a = self.cast_arr(inputs[1])

        t = self.cast_arr(inputs[2])

        return n, m, a, t

    def cast_arr(self, sub_input):
        """
        Transforms input string into array of strings.

        :param str sub_input: target string
        :return: array of parsed strings
        :rtype: list[str]
        """
        if not sub_input:
            return list()

        if sub_input == "":
            a = list()

        else:
            a = [str(x).strip()
                 for x
                 in sub_input.split()]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, m, a, t = Input()\
                 .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .eval_word_count(n, m, a, t)
    print(z)


## END OF FILE