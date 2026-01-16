class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(l, r, n, res):
            if l == r == n:
                result.append(res)
                return
            if l < n:
                helper(l + 1, r, n, res + "(")
            if r < n and l > r:
                helper(l, r + 1, n, res + ")")
        helper(0, 0, n, "")
        return result
    

# 还是用回溯法吧，感觉更直观一些
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        backtrack()
        return res
# 毛线，明明就一样简单好么。。。。
# 而且我忘记call function了，所以输出全是null，笑死