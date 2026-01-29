class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(path, target, candidates, p):
            if sum(path) == target:
                res.append(path)
                return
            if sum(path) > target:
                return 
            for i in range(p, len(candidates)):
                helper(path + [candidates[i]], target, candidates, i)
            return 
        helper([], target,candidates, 0)
        return res
    
# 剪枝优化
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 先排序，这是剪枝的前提
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(remain, start, path):
            # target 刚好减到 0，说明找到了一个组合
            if remain == 0:
                res.append(path)
                return

            for i in range(start, n):
                # 2. 核心剪枝：如果当前数字已经大于剩余目标量
                # 因为数组有序，后面的数字必然也大，直接 break 结束当前层的循环
                if remain < candidates[i]:
                    break
                
                # 3. 继续搜索：传递新的剩余值，并限制下一次搜索的起点为 i（允许重复使用）
                backtrack(remain - candidates[i], i, path + [candidates[i]])

        backtrack(target, 0, [])
        return res