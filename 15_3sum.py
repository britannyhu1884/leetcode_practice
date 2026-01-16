class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = 0

        def helper(i, j, t, nums):
            while i < j:
                if nums[i] + nums[j] == -nums[t]:
                    return i, j
                elif nums[i] + nums[j] > nums[t]:
                    j -= 1
                else:
                    i += 1
            return
        while t < len(nums) - 2:
            if helper(t + 1, len(nums) - 1, t, nums):
                i, j = helper(t + 1, len(nums) - 1, t, nums)
                res.append([nums[t], nums[i], nums[j]])
            t += 1
        return res
# 错了很多次，主要是没有去重，还有双指针多解没有解决，会少结果
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left,right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res