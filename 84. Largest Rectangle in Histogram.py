class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # corner case to pop out the acsending order stack
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:  # matain ascending order
                h = heights[stack.pop()]  # because it has been pop out
                w = i - stack[-1] - 1  # stack[-1] is the left bouundary and i is the right boundary
                maxArea = max(maxArea, h * w)
            stack.append(i)

        return maxArea