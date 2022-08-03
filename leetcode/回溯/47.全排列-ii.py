#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

from typing import List
# @lc code=start

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False]*len(nums)

        def dfs(track):
            if len(track) == len(nums):
                res.append(track[:])
            
            for i in range(len(nums)):
                if used[i]==True: continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                    continue
                used[i]=True
                track.append(nums[i])
                dfs(track)
                track.pop(-1)
                used[i]=False

        dfs([])
        return res

# @lc code=end

