# Two sum O(N) O(N)


# Check 1497. Check If Array Pairs Are Divisible by k
# The difference in 1497 is once used need to delete it from lookup table


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lookup = collections.defaultdict(int)
        count = 0
        for time in time:
            key = -time % 60
            count += lookup[key]
            lookup[time % 60] += 1
        return count


