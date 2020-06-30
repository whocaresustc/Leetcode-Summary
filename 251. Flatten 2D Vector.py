class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.v = v

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            val = self.v[self.row][self.col]
            self.col += 1  # don't forget
            return val
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            # start a new row
            self.row += 1
            self.col = 0
        return False