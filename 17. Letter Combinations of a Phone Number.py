# Similar to 77 combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        return self.helper(digits, 0, "", [])

    def helper(self, digits, index, combination, res):
        if index == len(digits):
            res.append(combination)
            return

        for letter in self.mapping[digits[index]]:
            self.helper(digits, index + 1, combination + letter, res)

        return res
