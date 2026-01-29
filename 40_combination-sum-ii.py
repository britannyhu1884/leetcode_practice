class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(left, path, p):
            if left == 0:
                res.append(path)
                return 
            for i in range(p, len(candidates)):
                if left < candidates[i]:
                    break
                if i > p and candidates[i] == candidates[i - 1]:
                    continue
                helper(left - candidates[i], path + [candidates[i]], i + 1)
            return
        helper(target, [], 0)
        return res
    
# 参考了题解，主要是去重的部分 if i > p and candidates[i] == candidates[i - 1]:
# 下面是原始的错误写法：
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(left, path, p):
            if left == 0:
                res.append(path)
            for i in range(p, len(candidates)):
                if left < candidates[i]:
                    break
                if i - 1 >= 0 and candidates[i - 1] == candidates[i]:
                    continue
                helper(left - candidates[i], path + [candidates[i]], i + 1)
            return
        helper(target, [], 0)
        return res