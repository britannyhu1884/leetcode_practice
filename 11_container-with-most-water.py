class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            l = j - i
            h = min(height[i], height[j])
            if l * h > res:
                res = l * h
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return res