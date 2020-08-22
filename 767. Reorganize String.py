# Similar to 621 Task scheduler
# Greedy
class Solution:
    def reorganizeString(self, S):
        count = collections.Counter(S)
        digit0 = count.most_common(1)[0][0]
        max_count = count.most_common(1)[0][1]

        if 2 * max_count - 1 > len(S):  # if there not enough character to fill in
            return ""

        ans = [digit0 for _ in range(max_count)]

        i = 0
        for digit in count:
            if digit != digit0:
                for _ in range(count[digit]):
                    ans[i % len(ans)] += digit
                    i += 1

        return ''.join(ans)


from heapq import *
from collections import defaultdict


class Solution:
    def reorganizeString(self, str):
        charFrequencyMap = defaultdict(int)
        for char in str:
            charFrequencyMap[char] += 1

        maxHeap = []

        for char, frequency in charFrequencyMap.items():
            heappush(maxHeap, (-frequency, char))

        previousChar, previousFrequency = None, 0
        resultString = []
        while maxHeap:
            frequency, char = heappop(maxHeap)
            # add the previous entry back in the heap if its frequency is greater than zero
            if previousChar and -previousFrequency > 0:
                heappush(maxHeap, (previousFrequency, previousChar))
            # append the current character to the result string and decrement its count
            resultString.append(char)
            previousChar = char
            previousFrequency = frequency + 1  # decrement the frequency
        return ''.join(resultString) if len(resultString) == len(str) else ""