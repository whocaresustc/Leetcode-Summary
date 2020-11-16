# O(L(N-L)) O(1) N: len(haystack) L: len(needle)
class Solution:
    def strStr(self, source, target):
        # Write your code here
        if len(target) == 0:
            return 0

        if len(target) > len(source):  # avoid this case go to the for loop
            return -1

        for i in range(len(source) - len(target) + 1):
            if source[i:len(target) + i] == target:
                return i
        return -1


#  Method 2: two pointers  time: best O(N) worst O(L(N-L))

"""Drawback of the previous algorithm is that one compares absolutely all substrings of length L with the needle. 
There is no need to that.

First, let's compare only substrings which starts from the first character in the needle substring. 
Second, let's compare the characters one by one and stop immediately in the case of mismatch."""



# Method 3: sliding window + hashing
"""The idea is simple: move along the string, generate hash of substring in the sliding window and compare it with the reference hash of the needle string."""


# Method 4: KMP need to know?
