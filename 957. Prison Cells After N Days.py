class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextday(cells):
            next_day_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):  # First and last are always 0
                if cells[i - 1] == cells[i + 1]:
                    next_day_cells[i] = 1
                else:
                    next_day_cells[i] = 0
            return next_day_cells

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:  # find a period
                N %= seen[c] - N  # seen[c] - N equals to period
            seen[c] = N  # Otherwise add to seen

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells