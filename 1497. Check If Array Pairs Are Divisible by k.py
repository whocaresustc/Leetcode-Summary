class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ## RC ##
        ## APPROACH : 2 SUM ## (X + Y) % K == 0 => X%K = -Y%K
        ## LOGIC ##
        ## 1. Store the remainders in the hashmap and check if the current number has remaining remainder available in the hashset ##

        lookup = collections.defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = -num % k
            if key in lookup and lookup[key] >= 1:
                count += 1
                lookup[key] -= 1
            else:
                lookup[(num % k)] += 1
        return count == len(arr) // 2
