class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0  # 判空防止越界
        
        digit = 0
        sign = 1    # 改为数字，方便最后相乘
        flag = 0    # 0:起始状态, 1:数字状态, 2:符号状态
        
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                digit = int(s[i]) + digit * 10
                flag = 1
            elif s[i] in ['+', '-'] and flag == 0:
                # 只有在还没遇到数字也没遇到符号时，才允许出现符号
                sign = -1 if s[i] == '-' else 1
                flag = 2 # 标记已经处理过符号了
            else:
                # 遇到非数字字符，或者在数字/符号后又遇到符号，直接结束
                break
        
        # 应用符号
        res = sign * digit
        
        # 处理 32 位整数越界
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if res > MAX_INT: return MAX_INT
        if res < MIN_INT: return MIN_INT
        
        return res