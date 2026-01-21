class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return  []
        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def helper(i, digits, path):
            if len(path) == len(digits):
                result.append(path)
                return 
            for j in range(len(digit_to_char[digits[i]])):
                helper(i + 1, digits, path + digit_to_char[digits[i]][j])
        helper(0, digits, "")
        return result
                
# 完美，打败100%，嘻嘻