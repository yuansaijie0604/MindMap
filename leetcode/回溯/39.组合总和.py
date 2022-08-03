#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(track, start, target):
            if target==0:
                res.append(track[:])
            for i in range(start, len(candidates)):
                if candidates[i] > target: break
                track.append(candidates[i])
                dfs(track, i, target-candidates[i]) # 从i开始，代表可以重复取当前数值
                track.pop(-1)

        dfs([], 0, target)
        
        return res

# @lc code=end

