class Solution:
    def maximumSwap(self, num):
        A = list(str(num))
        last = {int(x): i for i, x in enumerate(A)}

        for i, x in enumerate(A):
            for d in range(9, int(x), -1):  # descending order
                if last.get(d, 0) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(A))
        return num