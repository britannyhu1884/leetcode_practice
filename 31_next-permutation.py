class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: 从后往前找第一个升序对
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # Step 2: 如果找到了，找第一个比它大的数交换
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 i 和 j
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: 反转 i+1 到末尾
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# 参考了题解，写得更简洁了一些
# 主要是交换和反转的部分
# 并不是用backtrack去穷举所有可能性，而是直接找到下一个排列
# 先找到第一个升序对，然后交换后面最小的比它大的数（第一个升序对的右边的所有数据都是降序的），再反转后面的部分