#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        window = defaultdict(int)
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            window[c] += 1
            while window[c] > 1:
                window[s[left]] -= 1
                left += 1
            maxlen = max(right-left+1, maxlen)
            right += 1
        
        return maxlen        


# @lc code=end

