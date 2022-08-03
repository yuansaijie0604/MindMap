#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import SupportsBytes


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """
    #     subset[1,2,3] = subset[1,2] + [[x,3] for x in subset[1,2]]
    #     """
    #     if not nums: return [[]]

    #     last = nums.pop(-1)
    #     res = self.subsets(nums)

    #     for i in range(len(res)):
    #         res.append(res[i]+[last])

    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        思路：回溯
        """ 
        res = []

        def dfs(nums, start, track):
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                dfs(nums, i+1, track)
                track.pop(-1)
            return
        
        dfs(nums, 0, [])

        return res


# @lc code=end

