# time O(m*n), use Stack
# this problem is based on 84. Largest Rectangle in Histogram
# Build a histogram for each row, each hist is built on the previous hist
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        hist = [0] * n
        max_area = 0

        for i in range(m):
            # update hist for each row
            for j in range(n):
                if matrix[i][j] == "0":  # reset to zerro no matter what is the previous histgram value
                    hist[j] = 0
                else:
                    hist[j] += 1
            max_area = max(max_area, self.maxAreaInHist(hist))
        return max_area

    def maxAreaInHist(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        #height.pop()
        return ans


"""The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building who is taller than the new one. The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings."""