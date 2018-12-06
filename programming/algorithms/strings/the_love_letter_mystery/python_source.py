# -*- coding: utf-8 -*-
"""
HackerRank - The Love-Letter Mystery
https://www.hackerrank.com/challenges/the-love-letter-mystery

Created on Wed Dec  5 19:53:42 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all characters in array.

    Time complexity: O(n)
        - Amortized traverse all elements of array
    Space complexity: O(1)
        - Update constant number of pointers
    """

    def love_letter_mystery(self, n, a):
        """
        Evaluate required palindrome moves for each string in array.

        :param int n: number of strings in array
        :param list[int] a: array of input strings
        :return: minimum move counts for all input strings
        :rtype: list[int]
        """
        if (not n or
            not a):
            return list()

        z = [self.count_palindrome_moves(s)
             for s
             in a]

        return z

    def count_palindrome_moves(self, s):
        """
        Determine minimum character changes for palindrome transformation.

        :param str s: target string
        :return: minimum moves to transform target string into palindrome
        :rtype: int
        """
        if not s:
            return 0

        p = 0
        n = len(s)

        # Iterate over external pairs of characters
        for i in range(0, n // 2, 1):

            # Find left and right characters
            l = s[i]
            r = s[(n - 1) - i]

            if l == r:
                # Move to next character pair
                continue

            elif (l < r and
                  r != "a"):
                # Add changes for right character
                p += ord(r) - ord(l)

            elif (l > r and
                  l != "a"):
                # Add changes for left character
                p += ord(l) - ord(r)

            else:
                # Fails character conversion
                return -1

        return p

class Solution2:
    """
    Iteration over all characters in array.

    Time complexity: O(n)
        - Amortized traverse all elements of array
    Space complexity: O(k)
        - Amortized collect all characters in array for each input string
    """

    def love_letter_mystery(self, n, a):
        """
        Evaluate required palindrome moves for each string in array.

        :param int n: number of strings in array
        :param list[int] a: array of input strings
        :return: minimum move counts for all input strings
        :rtype: list[int]
        """
        if (not n or
            not a):
            return list()

        z = [self.count_palindrome_moves(s)
             for s
             in a]

        return z

    def count_palindrome_moves(self, s):
        """
        Determine minimum character changes for palindrome transformation.

        :param str s: target string
        :return: minimum moves to transform target string into palindrome
        :rtype: int
        """
        if not s:
            return 0

        a = list(x for x in s)

        l = 0
        r = len(a) - 1

        p = 0
        while l < r:

            if a[l] == a[r]:
                # No change required
                l += 1
                r -= 1

            elif (a[l] < a[r] and
                  a[r] != "a"):
                # Modify right character
                a[r] = chr(ord(a[r]) - 1)
                p += 1

            elif (a[l] > a[r] and
                  a[l] != "a"):
                # Modify left character
                a[l] = chr(ord(a[l]) - 1)
                p += 1

            else:
                # Found character less than "a"
                return -1

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: number of input strings and input array of strings
        :rtype: tuple[int, list[str]]
        """
        inputs = [x for x in sys_stdin]

        n = int(inputs[0])

        a = [str(x)\
             .strip("[]\n\"")
             for x
             in inputs[1:]]

        return n, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n, a = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .love_letter_mystery(n, a)
    print(*z, sep = "\n")


## END OF FILE