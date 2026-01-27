class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # 1. 寻找左边界
        left, right = 0, len(nums) - 1
        first_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:  # 关键：就算相等，也继续往左找
                if nums[mid] == target:
                    first_pos = mid  # 暂时记下这个位置，但还没完
                right = mid - 1      # 继续压榨左半部分
            else:
                left = mid + 1

        # 如果左边界都没找到，说明数组里根本没这个数，直接返回
        if first_pos == -1:
            return [-1, -1]

        # 2. 寻找右边界
        left, right = 0, len(nums) - 1
        last_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:  # 关键：就算相等，也继续往右找
                if nums[mid] == target:
                    last_pos = mid   # 暂时记下这个位置
                left = mid + 1       # 继续压榨右半部分
            else:
                right = mid - 1

        return [first_pos, last_pos]