
# https://www.youtube.com/watch?v=v05R1OIIg08
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtracking(i: int = 0, prefix: str = '', value: int = 0, prev: int = 0):
            if i == len(num) and value == target:
                result.append(prefix)
                return None
            for j in range(i + 1, len(num) + 1):
                string = num[i:j]
                number = int(string)
                if string != '0' and num[i] == '0':
                    continue
                if not prefix:
                    backtracking(j, string, number, number)
                else:
                    backtracking(j, prefix + '+' + string, value + number, number)
                    backtracking(j, prefix + '-' + string, value - number, -number)
                    backtracking(j, prefix + '*' + string, value - prev + prev * number, prev * number)

        result = []
        backtracking()
        return result