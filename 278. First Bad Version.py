class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        if isBadVersion(l):
            return l
        if isBadVersion(r):
            return r
        return -1


class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        if isBadVersion(l):
            return l

        return -1