#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(track, start, target):
            if target==0:
                res.append(track[:])
            for i in range(start, len(candidates)):
                if candidates[i] > target: break
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                track.append(candidates[i])        
                dfs(track, i+1, target-candidates[i])
                track.pop(-1)
        
        dfs([], 0, target)
        return res
# @lc code=end

