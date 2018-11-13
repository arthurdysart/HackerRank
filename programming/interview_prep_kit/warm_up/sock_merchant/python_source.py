# -*- coding: utf-8 -*-
"""
HackerRank - Sock Merchant
https://www.hackerrank.com/challenges/sock-merchant

Created on Mon Nov 12 22:29:31 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import Counter
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all elements of array.
    Time complexity: O(n)
        - Traverse all elements of array
    Space complexity: O(n)
        - Amortized Counter object contains all unique socks
    """

    def count_sock_pairs(self, n, a):
        """
        Determine minimum number of matching sock pairs.

        :param int n: number of individual socks
        :param list[int] a: array of all socks
        :return: maximum number of matching pairs of socks
        :rtype: int
        """
        if (not n or
            not a):
            return -1
  
        c = Counter(a)
    
        p = 0
        for i, q in c.items():
            p += q // 2
        return p

class Solution2:
    """
    Iteration over all elements in array.
    Time complexity: O(n)
        - Traverse all elements of array
    Space complexity: O(n)
        - Amortized dictionary contains all unique socks
    """

    def count_sock_pairs(self, n, a):
        """
        Determine minimum number of matching sock pairs.

        :param int n: number of individual socks
        :param list[int] a: array of all socks
        :return: maximum number of matching pairs of socks
        :rtype: int
        """
        if (not n or
            not a):
            return -1
  
        c = {}
        p = 0
        for i in range(n):
            t = a[i]
            if t in c:
                # Increase total sock count
                c[t] += 1
                if c[t] % 2 == 0:
                    # Increase sock pair count
                    p += 1
            else:
                c[t] = 1
        return p


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
        .count_sock_pairs(n, a)
    print(z)


## END OF FILE