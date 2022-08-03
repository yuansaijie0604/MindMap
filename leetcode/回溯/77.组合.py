#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(n, start, track):
            if len(track) == k:
                res.append(track[:])

            for i in range(start, n+1):
                track.append(i)
                dfs(n, i+1, track)
                track.pop(-1)
                

        dfs(n, 1, [])
        return res

# @lc code=end

