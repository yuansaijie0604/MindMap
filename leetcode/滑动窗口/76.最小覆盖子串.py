#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
import sys
from collections import defaultdict
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        need = defaultdict(int)
        for c in t:
            need[c] += 1

        minlen = sys.maxsize
        res = None
        windows = defaultdict(int)
        valid = 0   # 记录窗口是否满足了所有条件
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right-left < minlen:
                    minlen = right-left
                    res = s[left:right]
                
                k = s[left]
                left += 1
                if k in need:
                    if windows[k] == need[k]:
                        valid -= 1
                    windows[k] -= 1

        # return res
        return res if res else ""

# @lc code=end

