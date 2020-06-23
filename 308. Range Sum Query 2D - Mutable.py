# Have to use segment tree?
class NumMatrix(object):
    def __init__(self, matrix):
        for row in matrix:  # calculate presum for each row
            for col in range(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):

        original = self.matrix[row][col]

        if col != 0:  # don't understand?
            original -= self.matrix[row][col - 1]

        diff = original - val

        for y in range(col, len(self.matrix[0])):  # only need to update one row
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):  # preSum[col2] - preSum[col1]
        sum = 0
        for x in range(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum