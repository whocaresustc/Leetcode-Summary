# https://www.youtube.com/watch?v=v05R1OIIg08

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtracking(index, prefix, cur_value, prev):
            if index == len(num) and cur_value == target:
                res.append(prefix)
                return None

            for j in range(index + 1, len(num) + 1):
                next_part = num[index:j]
                n = int(next_part)
                if next_part != '0' and num[index] == '0':  # prevent "0*" as a number, but 0 + 0, 0 - 0, 0 * 0 are allowed
                    continue

                if index == 0:
                    backtracking(j, next_part, n, n)
                else:
                    backtracking(j, prefix + '+' + next_part, cur_value + n, n)
                    backtracking(j, prefix + '-' + next_part, cur_value - n, -n)
                    backtracking(j, prefix + '*' + next_part, cur_value - prev + prev * n, prev * n)

        res = []
        backtracking(0, "", 0, 0)
        return res