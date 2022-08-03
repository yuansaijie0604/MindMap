#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(track, start, target):
            if target==0 and len(track)==k:
                res.append(track[:])
            if len(track)>k or target<0:
                return
            
            for i in range(start, 10):
                # if i in track: continue
                track.append(i)
                dfs(track, i+1, target-i)
                track.pop(-1)
        dfs([], 1, n)
        return res

# @lc code=end

