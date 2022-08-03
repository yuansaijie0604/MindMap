#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        need = defaultdict(int)
        for c in p:
            need[c] += 1
        
        res = []
        windows = defaultdict(int)
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                
                k = s[left]
                left += 1
                if k in need:
                    if windows[k] == need[k]:
                        valid -= 1
                    windows[k] -= 1

        return res

# @lc code=end

