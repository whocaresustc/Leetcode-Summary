# Solution 1: DFS with list as marker
# Time O(N!^N) Space O(N)
class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        # Initialize to False
        self.cols = [[False] * 10 for i in range(9)]
        self.rows = [[False] * 10 for i in range(9)]
        self.boxes = [[False] * 10 for i in range(9)]
        # For every existing number, mark it to True
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    self.rows[i][val] = True
                    self.cols[j][val] = True
                    self.boxes[i // 3 + j // 3 * 3][val] = True
        self.fill(board, 0, 0)

    def fill(self, board, x, y):
        if y == 9:
            return True
        # Move in the row direction
        nx = (x + 1) % 9
        ny = y + (nx == 0) * 1
        if board[x][y] != ".":
            return self.fill(board, nx, ny)
            # if board[x][y] == '.'
        # Backtracking
        for i in range(1, 10):
            if not self.rows[x][i] and not self.cols[y][i] and not self.boxes[x // 3 + y // 3 * 3][i]:
                self.rows[x][i] = True
                self.cols[y][i] = True
                self.boxes[x // 3 + y // 3 * 3][i] = True
                board[x][y] = str(i)
                if self.fill(board, nx, ny):
                    return True
                self.rows[x][i] = False
                self.cols[y][i] = False
                self.boxes[x // 3 + y // 3 * 3][i] = False
                board[x][y] = '.'
        return False

# Solution 2: DFS with set as marker: something is wrong!
#Time O(N!^N) Space O(N)
class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        [cols, rows, boxes] = [collections.defaultdict(set)] * 3
        # For every existing number, mark it to True
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i // 3 + j // 3 * 3].add(val)
        self.fill(board, 0, 0, rows, cols, boxes)

    def fill(self, board, x, y, rows, cols, boxes):
        if y == 9:
            return True
        # Move in the row direction
        nx = (x + 1) % 9
        ny = y + (nx == 0) * 1
        if board[x][y] != ".":
            return self.fill(board, nx, ny, rows, cols, boxes)
            # if board[x][y] == '.'
        # Backtracking
        for i in range(1, 10):
            if i not in rows[x] and i not in cols[y] and i not in boxes[x // 3 + y // 3 * 3]:
                rows[x].add(i)
                cols[y].add(i)
                boxes[x // 3 + y // 3 * 3].add(i)
                board[x][y] = str(i)
                if self.fill(board, nx, ny, rows, cols, boxes):
                    return True
                rows[x].remove(i)
                cols[y].remove(i)
                boxes[x // 3 + y // 3 * 3].remove(i)
                board[x][y] = '.'
        return False