#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # def compute(nums, track):
        #     if len(nums) == 0:
        #         res.append(track)

        #     for i in range(len(nums)):
        #         track.append(nums[i]) # 选择
        #         compute(nums[:i]+nums[i+1:], track.copy())  # python语言会改变track，导致撤销选择出现问题，所以记得用copy, 空间复杂度变高了。
        #         track.pop(-1) # 撤销选择
        
        # compute(nums, [])

        # def change(first=0):
        #     if first == len(nums):
        #         # res.append(nums) # 同上错误，可查阅python语言的值传递和引用传递
        #         res.append(nums[:])
        #         return

        #     for i in range(first, len(nums)):
        #         nums[first], nums[i] = nums[i], nums[first]
        #         change(first+1)
        #         nums[first], nums[i] = nums[i], nums[first]
        
        # change()

        def dfs(track):
            if len(track) == len(nums):
                res.append(track[:])

            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                dfs(track)
                track.pop(-1)

        dfs([])

        return res

# @lc code=end

