#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, track):
            """
            可用的左括号数量为 left 个，可用的右括号数量为 rgiht 个
            """
            if left==0 and right==0:
                res.append(track)
                return

            if right < left: return
            if right < 0 or left < 0: return

            track += '('
            dfs(left-1, right, track)
            track = track[:-1]

            track += ')'
            dfs(left, right-1, track)
            track = track[:-1]
        
        dfs(n, n, "")
        return res

# @lc code=end

