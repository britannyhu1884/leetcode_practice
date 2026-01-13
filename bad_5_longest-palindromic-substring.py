
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand(left, right):
            # 向两边扩散，直到不满足回文条件
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回当前找到的回文串
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            # 情况 1: 奇数长度，中心是一个字符 (例如 "aba" 中的 'b')
            s1 = expand(i, i)
            # 情况 2: 偶数长度，中心是两个字符 (例如 "abba" 中的 'bb')
            s2 = expand(i, i + 1)
            
            # 更新最长结果
            res = max(res, s1, s2, key=len)
            
        return res
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        l = 1
        m = 0
        n = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # print(i, j)
                if i > j:
                    # print("step1")
                    continue
                if i == j:
                    # print("step2")
                    dp[i][j] = True
                    continue
                if (s[i] == s[j] and dp[i + 1][j - 1] == True) or (i + 1 == j and s[i] == s[j]):
                    # print("step3")
                    dp[i][j] = True
                    if j - i + 1 > l:
                        m = i 
                        n = j
                        l = j - i + 1
        return s[m: n+1]
# 哇，脑子不清醒的时候做题真的好差劲
