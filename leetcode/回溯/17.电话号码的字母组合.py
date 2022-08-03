#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        digits = [letter_map.get(c, "") for c in digits]

        def dfs(digits, start, track):
            if start==len(digits):
                res.append(track)
                return
            
            letters = digits[start]
            for j in letters:
                dfs(digits, start+1, track+j)
        
        dfs(digits, 0, "")
        return res


# @lc code=end

