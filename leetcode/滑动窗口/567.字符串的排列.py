#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
from collections import defaultdict
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        
        windows = defaultdict(int)
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            
            while right-left >= len(s1):
                if valid == len(need):
                    return True
                k = s2[left]
                left += 1
                if k in need:
                    if windows[k] == need[k]:
                        valid -= 1
                    windows[k] -= 1

        return False

# @lc code=end

