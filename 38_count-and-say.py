class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = "1"
        def helper(s):
            res = ""
            repeat = 1
            p = 0
            while p <= len(s) - 1:
                if p < len(s) - 1 and s[p] == s[p + 1]:
                    repeat += 1
                    p += 1
                else:
                    res = res + str(repeat) + s[p]
                    p += 1
                    repeat = 1
            return res
        while n > 1:
            res = helper(res)
            n -= 1
        return res
