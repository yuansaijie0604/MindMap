#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        这个nums是无序的，且求子序列，不能排序，所以不能采用之前的去重方案
        需要一个set记录访问过的数值
        注意：深度遍历中每一层都会有一个全新的visited用于记录本层元素是否重复使用
        """
        res = []
        len_ = len(nums)
        track = []

        def dfs(start):
            if len(track)>=2:
                res.append(track[:])

            visited = set()
            for i in range(start, len_):
                if (track and nums[i] < track[-1]) or nums[i] in visited:
                    continue
                track.append(nums[i])
                visited.add(nums[i])
                dfs(i+1)
                track.pop(-1)
        
        dfs(0)
        return res
            
# @lc code=end

