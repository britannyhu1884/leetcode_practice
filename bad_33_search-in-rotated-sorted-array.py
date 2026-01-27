class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 情况 1：左半部分是有序的 [left...mid]
            if nums[left] <= nums[mid]:
                # 判断 target 是否在左边这个有序区间内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左边
                else:
                    left = mid + 1   # 在右边
            
            # 情况 2：右半部分是有序的 [mid...right]
            else:
                # 判断 target 是否在右边这个有序区间内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右边
                else:
                    right = mid - 1  # 在左边
                    
        return -1