class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特判：如果只有一行，或者行数大于字符串长度，直接返回原字符串
        if numRows < 2 or len(s) <= numRows:
            return s
        
        # 1. 初始化：为每一行创建一个列表
        # rows = ["", "", ""]
        rows = [""] * numRows
        
        cur_row = 0
        step = -1 # 步长：1 代表向下，-1 代表向上
        
        # 2. 遍历字符串
        for char in s:
            rows[cur_row] += char
            
            # 3. 关键点：碰到第一行或最后一行，反转方向
            # 如果到了第一行 (0) 或最后一行 (numRows - 1)
            if cur_row == 0 or cur_row == numRows - 1:
                step = -step # 反转方向：1 变 -1, -1 变 1
            
            cur_row += step
            
        # 4. 将所有行拼接起来
        return "".join(rows)