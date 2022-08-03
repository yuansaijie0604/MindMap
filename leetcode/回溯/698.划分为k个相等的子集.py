#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        思路：一个个桶装
        """
        if k > len(nums): return False

        sum_ = sum(nums)
        if sum_%k != 0: return False

        target = sum_ / k

        visited = [0] * len(nums)
        
        def backtrace(k, nums, index, target, visited, bucket):
            """
            bucket:当前桶中的数据和
            visited:记录哪些数据已经用过了
            """
            if k == 0: return True # 每个桶都装好了
            
            if bucket == target:
                # 装下一个桶
                if backtrace(k-1, nums, 0, target, visited, 0):
                    return True

            for i in range(index, len(nums)):
                if visited[i] == 1 or bucket + nums[i] > target:
                    continue
                visited[i] = 1
                bucket += nums[i]
                if backtrace(k, nums, i+1, target, visited, bucket):
                    return True
                bucket -= nums[i]
                visited[i] = 0

            return False

        return backtrace(k, nums, 0, target, visited, 0)


a = Solution()
a.canPartitionKSubsets([4,3,2,3,5,2,1], 4)

# @lc code=end

