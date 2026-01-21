class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            first = nums[i]
            m = i + 1
            n = len(nums) - 1
            while m < n:
                if nums[i] + nums[m] + nums[n] == target:
                    return target
                if abs(nums[i] +  nums[m] + nums[n] - target) < res:
                    res = abs(nums[i] +  nums[m] + nums[n] - target)
                    result = nums[i] +  nums[m] + nums[n]
                if nums[i] +  nums[m] + nums[n] > target:
                    n -= 1
                elif nums[i] +  nums[m] + nums[n] < target:
                    m += 1
        return result

# 还是双指针，和3sum类似，不过要记录最小差值
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # 1. 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # --- 极致剪枝开始 ---
            # 当前能凑出的最小三数之和
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum > target:
                # 后面只会越来越大，如果最小的都比 target 大，
                # 看看这个 min_sum 是否比之前的 closest 更接近，然后直接结束整个循环
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                break 
                
            # 当前 i 能凑出的最大三数之和
            max_sum = nums[i] + nums[n-2] + nums[n-1]
            if max_sum < target:
                # 当前 i 搭配最大的两个都够不着 target，更新 closest_sum 后直接跳过当前的 i
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                continue
            # --- 极致剪枝结束 ---

            # 2. 双指针
            m, r = i + 1, n - 1
            while m < r:
                current_sum = nums[i] + nums[m] + nums[r]
                if current_sum == target:
                    return target
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    m += 1
                    # 可以在这里也加上跳过重复 m 的逻辑，更进一步提速
                    while m < r and nums[m] == nums[m-1]: m += 1
                else:
                    r -= 1
                    while m < r and nums[r] == nums[r+1]: r -= 1
                    
        return closest_sum